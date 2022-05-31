from scapy.all import *
import codecs
from suffix_tree import Tree

p = rdpcap("/home/aleksandr/new_storage/DDOS/datasets/MYTEST.pcap")
print(len(p))
tree = Tree()
# b = hexstr(p[0])
# print(b[len(b) * 3 // 4::])
for i in range(len(p)):
    pkt = p[i]
    a = hexstr(pkt)
    a = a[len(a) * 3 // 4::]
    tree.add(i, a)

print(tree.find('a'))
