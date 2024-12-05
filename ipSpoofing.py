from scapy.all import *

# Constructing a packet
packet = IP(src="192.168.1.5", dst="192.168.1.1")/ICMP()

# Display packet details
print("Constructed Packet Details:")
packet.show()

# Display raw packet data in hex format
print("\nHexdump of the packet:")
hexdump(packet)
