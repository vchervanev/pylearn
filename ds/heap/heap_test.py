import pytest 
from heap import Heap


@pytest.fixture
def heap():
    return Heap()

def test_minimum(heap):
    heap.add(300)
    heap.add(200)
    heap.add(250)
    heap.add(400)
    heap.add(100)
    assert heap.minimum() == 100

