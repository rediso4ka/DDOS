from suffix_tree import Tree

tree = Tree({1: 'aba', 2: 'bbba'})
print(tree.find('a'), tree.find('cc'))
tree.add(3, 'ccc')
print(tree.find('cc'))
for id_, path in tree.find_all('a'):
    print(id_, ':', str(path))
# print(tree.to_dot())
print(tree.find_id(3, 'c'))
