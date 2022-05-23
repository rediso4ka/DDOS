from scapy.all import *

p = rdpcap("/home/aleksandr/new_storage/DDOS/datasets/LEGIT.pcap")
print(p)
print(len(p))
pkt = p[0]
print(pkt)
print(type(pkt))
a = str(hexdump(pkt))
print(a)
print(type(a))
