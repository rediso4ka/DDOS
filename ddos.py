from scapy.all import *
from suffix_tree import Tree


'''
Reading legitimate packages
'''
legit = rdpcap("/home/aleksandr/new_storage/DDOS/datasets/LEGIT.pcap")
legit_tree = Tree()
for i in range(100):
    pkt = legit[i]
    try:
        payload = pkt[Raw]
        legit_tree.add(str(i), bytes(payload))
    except LookupError:
        continue


'''
Reading DNS packages
'''
dns = rdpcap("/home/aleksandr/new_storage/DDOS/datasets/DNS.pcap")
dns_tree = Tree()
for i in range(100):
    pkt = dns[i]
    try:
        payload = pkt[Raw]
        dns_tree.add(str(i), bytes(payload))
    except LookupError:
        continue


'''
Testing
'''
# mytest = rdpcap("/home/aleksandr/new_storage/DDOS/datasets/MYTEST.pcap")
# mytest_tree = Tree()
# for i in range(len(mytest)):
#     pkt = mytest[i]
#     try:
#         payload = pkt[Raw]
#         print(i, ": ", bytes(payload), type(payload))
#         mytest_tree.add(str(i), bytes(payload))
#     except:
#         continue
#
# print("\n")
# print(mytest_tree.find(b'\x00'))
# for id_, path in mytest_tree.find_all(b'\xcd'):
#     print(id_, ':', str(path))
