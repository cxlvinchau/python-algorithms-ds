import heapq
import itertools

from collections import deque

from graphs.graph import Graph, WeightedGraph


def dijkstra(g: WeightedGraph, start=0, goal=None):
    dist = dict()
    dist[start] = 0
    h = [(dist.setdefault(v, float("inf")), v) for v in g.vertices]
    pre = dict()
    heapq.heapify(h)
    while h:
        d, v = heapq.heappop(h)
        if goal is not None and v == goal:
            break
        if dist[v] < d:
            continue
        for t in g.get_succs(v):
            if dist[t] is None or dist[v] + g.weights[(v,t)] < dist[t]:
                dist[t] = dist[v] + g.weights[(v,t)]
                pre[t] = v
                heapq.heappush(h, (dist[t], t))
    print(dist)
    if goal is not None and goal in pre:
        path = deque([goal])
        current = goal
        while current in pre:
            path.appendleft(pre[current])
            current = pre[current]
        print(" -> ".join(map(str, path)))


def bellman_ford(g: WeightedGraph, start=0):
    q1, q2 = [start], []
    dist = {start: 0}
    for i in range(len(g.vertices)):
        while q1:
            v = q1.pop()
            for t in g.get_succs(v):
                dist.setdefault(t, float("inf"))
                if dist[t] > dist[v] + g.weights[(v, t)]:
                    dist[t] = dist[v] + g.weights[(v, t)]
                    q2.append(t)
        if not q2:
            break
        elif i == len(g.vertices)-1 and q2:
            print("Cycle of negative length")
        else:
            q1, q2 = q2, q1
    print(dist)


def floyd_warshall(g: WeightedGraph):
    dist = [[float("inf")]*len(g.vertices) for _ in range(len(g.vertices))]
    for s,t in g.edges:
        dist[s][t] = min(dist[s][t], g.weights[(s,t)])
    for k,s,t in itertools.product(g.vertices, g.vertices, g.vertices):
        dist[s][t] = min(dist[s][t], dist[s][k] + dist[k][t])
    print(dist)