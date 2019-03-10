from graph import Graph, DFS

def test_e2e():
    g = Graph(5)
    g.connect(0,1)
    g.connect(0,2)
    g.connect(1,3)
    g.connect(1,4)
    g.connect(4,0)
    log = []
    def pre_visit(v):
        log.append(f"pre{v}")

    def post_visit(v):
        log.append(f"post{v}")        

    def cycle(path):
        log.append("cycle" + str.join('', [str(x) for x in path]))
    DFS.explore(g, 0, pre_visit=pre_visit, post_visit=post_visit, cycle=cycle)

    assert log[0] == 'pre0'
    assert log[1] == 'pre1'
    assert log[2] == 'pre3'
    assert log[3] == 'post3'
    assert log[4] == 'pre4'
    assert log[5] == 'cycle014'
    assert log[6] == 'post4'
    assert log[7] == 'post1'
    assert log[8] == 'pre2'
    assert log[9] == 'post2'
    assert log[10] == 'post0'