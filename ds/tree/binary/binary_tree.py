class BinaryTree:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def __repr__(self):
            return f'<{self.value}: {self.left}, {self.right}>'

    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return f'<BinaryTree {self.root}>'

    @staticmethod
    def from_list(values):
        parent = 0
        child = 0
        nodes = list(map(lambda value: BinaryTree.Node(value), values))
        while child < len(values):
            child += 1
            if child < len(values):
                nodes[parent].left = nodes[child]
            child += 1
            if child < len(values):
                nodes[parent].right = nodes[child]
            parent += 1
        return BinaryTree(nodes[0]) if len(nodes) > 0 else BinaryTree()
