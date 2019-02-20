class Heap:
    def __init__(self):
        self.items = []

    def add(self, value):
        node = Heap.Node(self.items, value)
        while node.lessThanParent():
            node = node.swapWithParentAndReturn()

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