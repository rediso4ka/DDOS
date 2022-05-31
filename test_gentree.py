from suffix_tree import Tree

tree = Tree({'a': 'aaa', 'b': 'bbb'})
print(tree.find('a'), tree.find('cc'))
tree.add('c', 'ccc')
print(tree.find('cc'))
