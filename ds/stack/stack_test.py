
from stack import Stack
from pytest import fixture, raises

@fixture
def stack():
    return Stack()

def test_emptyness(stack):
    assert stack.isEmpty() == True

def test_push(stack):
    value = 123
    stack.push(value)
    result = stack.pop()

    assert result == value

def test_empty_pop(stack):
    with raises(Stack.InvalidOperaion):
        stack.pop()

def test_sequence(stack):
    sequence = list(range(5))
    [stack.push(value) for value in sequence]
    result = []
    while not stack.isEmpty():
        result.append(stack.pop())

    sequence.reverse()
    assert result == sequence
