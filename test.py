from SuffixTree.payload_suffix_tree import SuffixTree
from SuffixTree.payload_modules import CheckSubString

legit = ["ABCD$", "AATT$", "ME$", "MAAM$", "BANANA$", "DANANA$", "ATAT$"]
income = ["ATTACK", "CRIME", "BANAN", "ABCD", "BANANA",
          "DANANA", "ATTACK", "ATTAC", "MAMA", "PAPA",
          "AATAT", "ABCT", "ME", "BCD", "DAATT", "HEL"]
attacks = []
not_attacks = []

legit_trees = []

for i in range(len(legit)):
    tree = SuffixTree(legit[i])
    tree.build_suffix_tree()
    legit_trees.append(tree)

# for i in range(len(legit)):
#     a = CheckSubString(legit_trees[i], 'BANA', findall=True)
#     print(a.check())

for i in range(len(income)):  # each income
    prob = 0
    start_prob = 1 / len(legit)
    good = False
    # print(len(income))
    for k in range(len(income[i]), 0, -1):  # each word length
        # print(k)
        for l in range(len(income[i]) - k + 1):  # each amount of that length
            substr = income[i][l:l + k]
            # print(substr, l)
            for j in range(len(legit)):  # check in each legit
                a = CheckSubString(legit_trees[j], substr, findall=True)
                a = a.check()
                if type(a) == list and a[0] >= 0:
                    # print(a)
                    if len(substr) == len(income[i]):
                        prob = 1
                    else:
                        prob += start_prob
                    if prob >= 0.4:
                        good = True
                        break
            if good:
                break
        if good:
            break
        start_prob /= 2
    if good:
        not_attacks.append(income[i])
    else:
        attacks.append(income[i])


print("NOT ATTACKS: ", not_attacks)
print("ATTACKS: ", attacks)