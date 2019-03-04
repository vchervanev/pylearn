from binary_tree import BinaryTree

def wrap(node):
    return [node.value, wrap(node.left), wrap(node.right)] if node is not None else None

def test_creation_empty():
    tree = BinaryTree.from_list([])
    assert tree.root is None

def test_creation_single_element():
    tree = BinaryTree.from_list([42])
    assert wrap(tree.root) == [42, None, None]

def test_creation_3_nodes():
    tree = BinaryTree.from_list([1,2,3])
    assert wrap(tree.root) == [
        1, 
            [2, None, None],
            [3, None, None],
        ]

def test_creation_9_nodes():
    tree = BinaryTree.from_list(list(range(1, 10)))
    assert wrap(tree.root) == [
        1, 
            [2, 
                [4, 
                    [8, None, None],
                    [9, None, None]],
                [5, None, None]],
            [3, 
                [6, None, None],
                [7, None, None]],
        ]

def test_bfs():
    numbers = list(range(1, 10))
    tree = BinaryTree.from_list(numbers)
    result = list(tree.bfs())

    assert result == numbers

def test_bfs_empty_tree():
    tree = BinaryTree()
    result = list(tree.bfs())

    assert len(result) == 0