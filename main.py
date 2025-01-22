import suffix_trees
from suffix_trees import STree
import graphviz
from collections import Counter


class TreeNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def __str__(self):
        return self.label


def generate_strees1(s, m):
    if m <= 0:
        return []

    def helper(start, end, m):
        if m == 1:
            return [s[start:end]]
        trees = []

        for i in range(start + 1, end):
            left_subtrees = helper(start, i, m - 1)

            right_subtrees = helper(i, end, 1)

            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    node = TreeNode(s[i])
                    node.left = left_subtree
                    node.right = right_subtree
                    trees.append(node)

        return trees

    return helper(0, len(s), m)


def print_tree(node, level=0, prefix="Root: "):
    if node:

        print("  " * level + prefix, node)

        if str(type(node)).split("'")[1] != 'str':
            print_tree(node.left, level + 1, "Left: ")
            print_tree(node.right, level + 1, "Right: ")


class TreeNodeHP:
    def __init__(self, character=None, frequency=None):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None


def build_hp_tree(string):
    from collections import Counter
    char_freq = Counter(string)
    nodes = [TreeNodeHP(c, f) for c, f in char_freq.items()]

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.frequency)

        left_node = nodes.pop(0)
        right_node = nodes.pop(0)

        combined_frequency = left_node.frequency + right_node.frequency
        intermediate_node = TreeNodeHP(frequency=combined_frequency)
        intermediate_node.left = left_node
        intermediate_node.right = right_node

        nodes.append(intermediate_node)

    return nodes[0]


def display_hp_tree1(node, level=0):
    if node is not None:
        display_hp_tree1(node.right, level + 1)

        print('    ' * level + str(node.frequency) + (" (" + node.character + ")" if node.character else ""))

        display_hp_tree1(node.left, level + 1)


def compute_modified_lists(input_string, m):
    n = len(input_string)
    F0 = [0, 0, 1, 0, 0, 1]
    F1 = [0] * (n - m + 1)

    for i in range(n - m + 1):
        for j in range(i + 1, n - m + 1):

            distance = hamming_distance(input_string[i:i + m], input_string[j:j + m])
            if distance <= 1:
                F1[i] += 1

        F1[i] -= F0[i]

    return F0, F1


def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def construct_s_tree(input_string, m):
    n = len(input_string)
    s_tree = []
    modified_lists = []

    for i in range(n - m + 1):
        suffix = input_string[i:i + m]
        modified_lists.append([suffix, i])

    modified_lists.sort()

    suffix_counter = 1

    for i in range(len(modified_lists)):
        suffix, index = modified_lists[i]
        leaf = {'suffix': suffix, 'index': index, 'modified': True, 'modified_list': [index], 'id': suffix_counter}
        s_tree.append(leaf)
        suffix_counter += 1

        if i > 0 and suffix == modified_lists[i - 1][0]:
            s_tree[-2]['modified'] = False

    return s_tree


def generate_F1_s_tree(s_tree, F0):
    n = len(s_tree)
    F1 = [0] * n

    for i in range(n - 1, -1, -1):
        if s_tree[i]['modified']:
            modified_list = s_tree[i]['modified_list']
            F1[i] += len(modified_list) - F0[i]
        if i < n - 1:
            F1[i] += F1[i + 1]

    F1[len(F1) - 1] = 2
    return F1


def construct_hp_tree(input_string, m):
    n = len(input_string)
    hp_tree = []
    modified_lists = []
    unmodified_lists = []

    for i in range(n - m + 1):
        suffix = input_string[i:i + m]
        modified_lists.append([suffix, i])

    modified_lists.sort()

    for i in range(len(modified_lists)):
        suffix, index = modified_lists[i]
        leaf = {'suffix': suffix, 'index': index, 'modified': True, 'modified_list': [index]}
        hp_tree.append(leaf)

        if i > 0 and suffix == modified_lists[i - 1][0]:
            hp_tree[-2]['modified'] = False

    for i in range(n - m + 1):
        suffix = input_string[i:i + m]
        unmodified_lists.append({'suffix': suffix, 'index': i, 'modified': False})

    hp_tree.extend(unmodified_lists)
    hp_tree.sort(key=lambda x: x['suffix'])

    return hp_tree


def generate_F1_hp_tree(hp_tree, F0):
    n = len(hp_tree)
    F1 = [0] * n

    for i in range(n - 1, -1, -1):
        if hp_tree[i]['modified']:
            modified_list = hp_tree[i]['modified_list']
            F1[i] += len(hp_tree[i]['unmodified_list']) - F0[i]
            F1[i] += len(modified_list) * len(hp_tree[i]['unmodified_list'])
        if i < n - 1:
            F1[i] += F1[i + 1]

    return F1


input_string = input("Enter the input string: ")
m = int(input("Enter the value of m: "))

if m <= 0:
    print("m should be a positive integer.")
else:
    s_trees = generate_strees1(input_string, m)
    print(f"All s-trees for the input string with m={m}:")
    for i, tree1 in enumerate(s_trees):
        print(f"Tree {i + 1}:")
        print_tree(tree1)
        print("-" * 30)

print("Printing HP-Tree")
hp_tree_root = build_hp_tree(input_string)
display_hp_tree1(hp_tree_root)

F0, F1 = compute_modified_lists(input_string, m)
s_tree = construct_s_tree(input_string, m)
hp_tree = construct_hp_tree(input_string, m)

F1_s_tree = generate_F1_s_tree(s_tree, F0)
arr = [""] * len(s_tree)
for tree in s_tree:
    arr[tree['index']] = tree['suffix']
print("printing table: ")
print()
print("----------------------------------------------------")
print("Index", end="\t")
for i in range(len(F1_s_tree)):
    print(i + 1, end="\t")
print()
print("----------------------------------------------------")
print("string", end="\t")
for i in range(len(arr)):
    print(arr[i], end="\t")
print()
print("----------------------------------------------------")
print("F0", end="\t")
for f0 in F0:
    print(f0, end="\t")
print()
print("----------------------------------------------------")
print("F1", end="\t")
for f1 in F1_s_tree:
    print(f1, end="\t")
print()
print("----------------------------------------------------")