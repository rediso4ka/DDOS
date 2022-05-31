from scapy.all import *
import codecs
from SuffixTree.suffixtree import SuffixTree
from SuffixTree.modules import CheckSubString

p = rdpcap("/home/aleksandr/new_storage/DDOS/datasets/LEGIT.pcap")
print(p)
print(len(p))
# strings = []
# for i in range(len(p)):
#     pkt = p[i]
#     a = hexstr(pkt)
#     strings.append(a)

# print(len(strings))

# legit_trees = []
#
# for i in range(len(strings)):
#     tree = SuffixTree(strings[i])
#     tree.build_suffix_tree()
#     legit_trees.append(tree)
#
# print(len(legit_trees))
print("\nSpecific packet:")
pkt = p[0]
print(pkt)
print(type(pkt))
hexdump(pkt)
tcpdump(pkt)
a = hexstr(pkt)
print(type(a))
print(a)
print(len(a))

print(a[401])
print(codecs.encode(b".", "hex"))
print(hex(ord(a[401])))

b = "FF FF FF FF FF FF 08 9E 01 4B 26 6F 08 00 45 00 00 65 9A 00 40 00 40 11 37 CE 93 E5 D4 D4 FF FF FF FF 86 94 00 A1 00 51 14 E9 30 47 02 01 01 04 06 70 75 62 6C 69 63 A0 3A 02 04 10 E1 C1 CD 02 01 00 02 01 00 30 2C 30 0C 06 08 2B 06 01 02 01 01 01 00 05 00 30 0C 06 08 2B 06 01 02 01 01 02 00 05 00 30 0E 06 0A 2B 06 01 02 01 02 02 01 06 01 05 00"
b = "FF"
b.replace(" ", "")
print(codecs.decode("FF", "hex").decode('utf-8'))
