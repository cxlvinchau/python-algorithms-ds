from graphs.graph import Graph
from graphs.traversal import tarjan, tarjan_rec

if __name__ == "__main__":
    g = Graph()
    g.add_edge((0,1))
    g.add_edge((1,2))
    #g.add_edge((2,0))
    g.add_edge((1,3))
    g.add_edge((3,4))
    g.add_edge((4,1))
    print(g.to_dot())

    tarjan(g)
    print("---------")
    tarjan_rec(g)