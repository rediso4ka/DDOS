from scapy.all import *
import codecs
from suffix_tree import Tree

p1 = rdpcap("/home/aleksandr/new_storage/DDOS/datasets/MYTEST.pcap")
print(len(p1))
tree = Tree()
for i in range(len(p1)):
    pkt = p1[i]
    a = hexstr(pkt)
    a = a[len(a) * 3 // 4::]
    tree.add(i, a)

# print(tree.find('a'))

# print(p1.summary())


pkt = Dot11()
dns = pkt[Dot11]
print(dns)
dns = dns.payload
print(dns)

print(Ether(p1[0]))
DNS = p1[0][IP]
print(DNS)

p2 = rdpcap("/home/aleksandr/new_storage/DDOS/datasets/LEGIT.pcap")
print(p2[2])
# legit_tree = Tree()
# for i in range(len(p2)):
#     pkt = p2[i]
#     a = hexstr(pkt)
#     a = a[len(a) * 3 // 4::]
#     legit_tree.add(i, a)
