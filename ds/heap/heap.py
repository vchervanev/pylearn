class Heap:
    def __init__(self):
        self.items = []

    def add(self, value):
        node = Heap.Node(self.items, value)
        while node.lessThanParent():
            node = node.swapWithParentAndReturn()

    def pop(self):
        value = self.minimum()
        if any(self.items): self.remove(0)
        return value

    def remove(self, index):
        node = self.items[index]
        lastNode = self.items.pop()
        node.value = lastNode.value
        if node is None:
            return None
        while node and node.biggerThanChildNode():
            node = node.swapWithSmallestChildNodeAndReturn()

    def minimum(self):
        return self.items[0].value if any(self.items) else None

    class Node:
        def __init__(self, items, value):
            self.items = items
            self.index = len(items)
            self.value = value
            items.append(self)

        def lessThanParent(self):
            parent = self.parent()
            return parent is not None and self.value < parent.value

        def swapWithParentAndReturn(self):
            parent = self.parent()
            [parent.value, self.value] = [self.value, parent.value]
            return parent

        def swapWithSmallestChildNodeAndReturn(self):
            childNode = self.smallestChildNode()
            [childNode.value, self.value] = [self.value, childNode.value]
            return childNode

        def biggerThanChildNode(self):
            node = self.smallestChildNode()
            return node and node.value < self.value

        def smallestChildNode(self):
            left = self.leftChild()
            right = self.rightChild()
            if left is None or right is None:
                return left or right
            elif left.value <= right.value:
                return left
            else:
                return right

        def leftChild(self):
            return self.safeGet(self.index*2+1)

        def rightChild(self):
            return self.safeGet(self.index*2+2)

        def safeGet(self, index):
            return self.items[index] if index < len(self.items) else None
            
        def parent(self):
            if self.index == 0:
                return None
            else:
                pindex = (self.index - 1) // 2
                return self.items[pindex]

        def __str__(self):
            return f'<{self.index}: {self.value}>'

        def __repr__(self):
            return str(self)
