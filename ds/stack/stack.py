class Stack:
    def __init__(self):
        self.top = None

    class Item:
        def __init__(self, prev, value):
            self.prev = prev
            self.value = value

    class InvalidOperaion(Exception):
        pass

    def push(self, value):
        self.top = Stack.Item(self.top, value)

    def pop(self):
        if self.isEmpty(): raise Stack.InvalidOperaion
        item = self.top
        self.top = item.prev
        return item.value
    
    def isEmpty(self):
        return self.top == None