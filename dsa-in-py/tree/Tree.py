class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)


# Create a tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


# Print the tree

def pre_order_print(node):
    if node:
        print(node.data, " -> ", end="")
        pre_order_print(node.left)
        pre_order_print(node.right)


def in_oder_print(node):
    if node:
        in_oder_print(node.left)
        print(node.data, " -> ", end="")
        in_oder_print(node.right)


def post_order_print(node):
    if node:
        post_order_print(node.left)
        post_order_print(node.right)
        print(node.data, " -> ", end="")


def bfs_print(node):
    queue = [node]
    while len(queue) > 0:
        pop = queue.pop(0)
        print(pop.data, "->", end="")
        if pop.left is not None:
            queue.append(pop.left)
        if pop.right is not None:
            queue.append(pop.right)


print("Pre Order")
pre_order_print(tree.root)

print("\nIn Order")
in_oder_print(tree.root)

print("\nPost Order")
post_order_print(tree.root)

print("\nBFS")
bfs_print(tree.root)
