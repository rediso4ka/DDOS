from scapy.all import *

p = rdpcap("/home/aleksandr/new_storage/DDOS/datasets/MYTEST.pcap")
print(p)
print(len(p))

print("\nSpecific packet:")
pkt = p[0]
print(pkt)
print(type(pkt))
hexdump(pkt)
tcpdump(pkt)
a = hexstr(pkt)
print(type(a))
print(a)
