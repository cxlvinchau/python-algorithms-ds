from graphs.flow import edmonds_karp
from graphs.graph import Graph, WeightedGraph
from graphs.paths import dijkstra, bellman_ford, floyd_warshall
from graphs.traversal import tarjan, tarjan_rec

def tarjan_exmp():
    g = Graph()
    g.add_edge((0, 1))
    g.add_edge((1, 2))
    # g.add_edge((2,0))
    g.add_edge((1, 3))
    g.add_edge((3, 4))
    g.add_edge((4, 1))
    print(g.to_dot())

    tarjan(g)
    print("---------")
    tarjan_rec(g)

def dijkstra_exmp():
    g = WeightedGraph()
    g.add_edge((0,1), 1)
    g.add_edge((0,2), 4)
    g.add_edge((1,2), 2)
    g.add_edge((1,3), 2)
    g.add_edge((1,4), 1)
    g.add_edge((2,3), 2)
    g.add_edge((3,5), 3)
    g.add_edge((4,3), 2)
    g.add_edge((4,5), 5)
    print(g.to_dot())
    dijkstra(g, goal=5)

def bellman_ford_exmp():
    g = WeightedGraph()
    g.add_edge((0, 1), 1)
    g.add_edge((0, 2), 4)
    g.add_edge((1, 2), 2)
    g.add_edge((1, 3), 2)
    g.add_edge((1, 4), 1)
    g.add_edge((2, 3), 2)
    g.add_edge((3, 5), 3)
    g.add_edge((4, 3), 2)
    g.add_edge((4, 5), 5)
    print(g.to_dot())
    bellman_ford(g)

def bellman_ford_exmp_neg_cycle():
    g = WeightedGraph()
    g.add_edge((0,1), 2)
    g.add_edge((1,2), -3)
    g.add_edge((1,3), 1)
    g.add_edge((2,0), 1)
    g.add_edge((3,4), 4)
    g.add_edge((4,1), 6)
    print(g.to_dot())
    bellman_ford(g)

def floyd_warshall_exmp():
    g = WeightedGraph()
    g.add_edge((0, 1), 1)
    g.add_edge((0, 2), 4)
    g.add_edge((1, 2), 2)
    g.add_edge((1, 3), 2)
    g.add_edge((1, 4), 1)
    g.add_edge((2, 3), 2)
    g.add_edge((3, 5), 3)
    g.add_edge((4, 3), 2)
    g.add_edge((4, 5), 5)
    print(g.to_dot())
    floyd_warshall(g)

def flow_exmp():
    network = WeightedGraph()
    network.add_edge((0,1), 16)
    network.add_edge((0,2), 13)
    network.add_edge((1,3), 4)
    network.add_edge((2,1), 4)
    network.add_edge((2,4), 14)
    network.add_edge((3,2), 9)
    network.add_edge((3,5), 20)
    network.add_edge((4,3), 4)
    network.add_edge((4,5), 4)
    print(network.to_dot())
    print(edmonds_karp(network, 0, 5))

if __name__ == "__main__":
    flow_exmp()