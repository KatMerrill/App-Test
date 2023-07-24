


# Various Lengths of Msgs or Hdrs
DEFAULT_MTU = (1500 - (20 + 8))
MSG_TYPE_LEN = 4           # length of msg type
VERSION_LEN = 4            # length of version in packet

# Different AMT Message Types
AMT_RELAY_DISCO = 1        # relay discovery
AMT_RELAY_ADV = 2          # relay advertisement
AMT_REQUEST = 3            # request
AMT_MEM_QUERY = 4          # memebership query
AMT_MEM_UPD = 5            # membership update
AMT_MULT_DATA = 6          # multicast data
AMT_TEARDOWN = 7           # teardown (not currently supported)


# Addresses
LOCAL_LOOPBACK = "127.0.0.1"
MCAST_ANYCAST = "0.0.0.0"
MCAST_ALLHOSTS = "224.0.0.22"

# amt-relay.m2icast.net.  0       IN      A       162.250.137.254
# amt-relay.m2icast.net.  0       IN      A       162.250.136.101
# amt-relay.m2icast.net.  0       IN      A       198.38.23.145
# amt-relay.m2icast.net.  0       IN      A       164.113.199.110


from scapy.all import Packet, send
from scapy.contrib.igmpv3 import IGMPv3, IGMPv3gr, IGMPv3mr
from scapy.layers.inet import IP, UDP
import secrets
import socket
import struct
import sys


# IGMPv3 Query
# https://tools.ietf.org/html/rfc3376#section-4.1
# https://tools.ietf.org/html/rfc3376#section-4.1.1

# relay = "amt-relay.m2icast.net"
# hard-coded test source found from Multicast Menu
relay = "198.38.23.145"
source = "198.38.23.146" 
multicast = "232.198.38.5"
amt_port = 3006
udp_port = 5006

from scapy.all import (
    BitField,
    IPField,
    MACField,
    Packet,
    PacketListField,
    ShortField,
    XStrFixedLenField
)
class AMT_Discovery(Packet):
    name = "AMT_Discovery"
    fields_desc = [ 
        BitField("version", 0, VERSION_LEN),
        BitField("type", AMT_RELAY_DISCO, MSG_TYPE_LEN),
        BitField("rsvd", 0, 24),
        XStrFixedLenField("nonce", 0, 4)
    ]


class AMT_Relay_Advertisement(Packet):
    name = "AMT_Relay_Advertisement"
    fields_desc = [
        BitField("version", 0, VERSION_LEN),
        BitField("type", AMT_RELAY_ADV, MSG_TYPE_LEN),
        BitField("rsvd", 0, 24),
        XStrFixedLenField("nonce", 0, 4),
        IPField("relay_addr", MCAST_ANYCAST)
    ]


class AMT_Relay_Request(Packet):
    name = "AMT_Relay_Request"
    fields_desc = [ 
        BitField("version", 0, VERSION_LEN),
        BitField("type", AMT_REQUEST, MSG_TYPE_LEN),
        BitField("rsvd1", 0, 7),
        BitField("p_flag", 0, 1),
        BitField("rsvd2", 0, 16),
        XStrFixedLenField("nonce", 0, 4)
    ]


class AMT_Membership_Query(Packet):
    name = "AMT_Membership_Query"
    fields_desc = [
        BitField("version", 0, VERSION_LEN),
        BitField("type", AMT_MEM_QUERY, MSG_TYPE_LEN),
        BitField("rsvd1", 0, 6),
        BitField("l_flag", 0, 1),
        BitField("g_flag", 0, 1),
        MACField("response_mac", 0),
        XStrFixedLenField("nonce", 0, 4),
        PacketListField("amt_ip", None, IP),
        PacketListField("amt_igmpv3", None, IGMPv3)
    ]


class AMT_Membership_Update(Packet):
    name = "AMT_Membership_Update"

    fields_desc = [
        BitField("version", 0, VERSION_LEN),
        BitField("type", AMT_MEM_UPD, MSG_TYPE_LEN),
        BitField("rsvd1", 0, 8),
        MACField("response_mac", 0),
        XStrFixedLenField("nonce", 0, 4),
        PacketListField("amt_igmpv3", None, IGMPv3)
    ]


class AMT_Multicast_Data(Packet):
    name = "AMT_Multicast_Data"
    fields_desc = [
        BitField("version", 0, VERSION_LEN),
        BitField("type", AMT_MULT_DATA, 4),
        BitField("rsvd", 0, 8),
        PacketListField("amt_ip", None, IP)
    ]


class AMT_Teardown(Packet):
    name = "AMT_Teardown"
    fields_desc = [
        BitField("version", 0, VERSION_LEN),
        BitField("type", AMT_TEARDOWN, 4),
        BitField("rsvd", 0, 8),
        MACField("response_mac", 0),
        XStrFixedLenField("nonce", 0, 4),
        ShortField("gw_port_num", 0),
        IPField("gw_ip_addr", MCAST_ANYCAST)
    ]

# Set up socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
s.bind(('', amt_port))

# Configure IP and UDP layers
ip_top_layer = IP(dst=relay)
udp_top_layer = UDP(sport=amt_port, dport=2268)    
nonce = secrets.token_bytes(4)

# Send AMT relay discovery
amt_layer = AMT_Discovery()
amt_layer.setfieldval("nonce", nonce)
send(ip_top_layer / udp_top_layer / amt_layer)
data, _ = s.recvfrom(DEFAULT_MTU)

# Send AMT relay advertisement
amt_layer = AMT_Relay_Request()
amt_layer.setfieldval("nonce", nonce)
send(ip_top_layer / udp_top_layer / amt_layer)
data, _ = s.recvfrom(DEFAULT_MTU)

# Send AMT multicast membership query
membership_query = AMT_Membership_Query(data)
response_mac = membership_query.response_mac
req = struct.pack("=4sl", socket.inet_aton(multicast), socket.INADDR_ANY)
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, req)

amt_layer = AMT_Membership_Update()
amt_layer.setfieldval("nonce", nonce)
amt_layer.setfieldval("response_mac", response_mac)

options_pkt = Packet(b"\x00")
ip_layer2 = IP(src=MCAST_ANYCAST, dst=MCAST_ALLHOSTS, options=[options_pkt])

igmp_layer = IGMPv3()
igmp_layer.type = 34

igmp_layer2 = IGMPv3mr(records=[IGMPv3gr(maddr=multicast, srcaddrs=[source])])

send(ip_top_layer / udp_top_layer / amt_layer / ip_layer2 / igmp_layer / igmp_layer2)

# Loop for data
count = 0
notified = False
while True:
    data, _ = s.recvfrom(DEFAULT_MTU)

    try: 
        amt_packet = AMT_Multicast_Data(data)
        raw_udp = bytes(amt_packet[UDP].payload)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.sendto(raw_udp, (LOCAL_LOOPBACK, udp_port)) # send to local loopback
    except Exception as err:
        print(f"Error occurred in processing packet {err}")

    if count < 50:
        print(".", flush=True, end="")
        count += 1
    else:
        if not notified:
            notified = True

