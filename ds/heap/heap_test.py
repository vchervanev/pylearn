import pytest
from heap import Heap


@pytest.fixture
def heap():
    return Heap()


def test_add_and_pop_sequence(heap):
    heap.add(200)
    assert len(heap.items) == 1
    heap.add(100)
    assert len(heap.items) == 2
    heap.add(300)
    assert len(heap.items) == 3
    heap.add(50)
    assert len(heap.items) == 4
    heap.add(400)
    assert len(heap.items) == 5
    v = heap.pop()
    assert len(heap.items) == 4
    assert v == 50
    v = heap.pop()
    assert len(heap.items) == 3
    assert v == 100
    v = heap.pop()
    assert len(heap.items) == 2
    assert v == 200
    v = heap.pop()
    assert len(heap.items) == 1
    assert v == 300
    v = heap.pop()
    assert len(heap.items) == 0
    assert v == 400
    v = heap.pop()
    assert len(heap.items) == 0
    assert v == None
