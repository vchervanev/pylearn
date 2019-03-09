from graph import Graph

def test_graph_api():
    g = Graph(3)
    g.connect(1,2)
    assert g.connected(1,2)
    assert not g.connected(2,1)
    # default value
    assert not g.connected(2,0)
    # per design
    assert not g.connected(0,0)
