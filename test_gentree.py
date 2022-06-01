from suffix_tree import Tree

tree = Tree({1: 'aba', 2: 'bbba', 'a' : u'a\x81'})
print(tree.find('a'), tree.find('cc'))
tree.add(3, 'ccc')
print(tree.find('cc'))
for id_, path in tree.find_all('a'):
    print(id_, ':', str(path))
# print(tree.to_dot())
print(tree.find(u'\x81'))

hexstring = '48'
a_string = bytes.fromhex(hexstring)
a_string = a_string.decode("ascii")

print(hex(ord("É")))
tree.add(4, a_string)
# print(a_string)
print(u'Entre\x81\xc9')
