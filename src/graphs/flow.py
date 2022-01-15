from graphs.graph import WeightedGraph
from collections import deque

def edmonds_karp(network: WeightedGraph, s, t):
    flow_network = WeightedGraph()
    for v in network.vertices:
        flow_network.add_vertex(v)
    for e in network.edges:
        flow_network.add_edge(e, network.weights[e])

    flow = dict()
    while True:
        # Find augmenting flow
        queue = deque([s])
        pre = dict()
        visited = set()
        while queue:
            v = queue.popleft()
            visited.add(v)
            if v == t:
                break
            for u in flow_network.get_succs(v):
                if u not in visited and flow_network.weights[(v,u)] > 0:
                    queue.append(u)
                    pre[u] = v
        # No augmenting path anymore
        if t not in pre:
            return flow
        # Compute augmenting flow from pre
        v, min_flow = t, float("inf")
        path = deque([t])
        while path[0] in pre:
            p = pre[path[0]]
            min_flow = min(min_flow, flow_network.weights[(p, path[0])])
            path.appendleft(p)

        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            if (u,v) in network.edges:
                flow.setdefault((u,v), 0)
                flow[u,v] += min_flow
                flow_network.weights[u,v] -= min_flow
                if (v, u) in flow_network.edges:
                    flow_network.weights[(v,u)] += min_flow
                else:
                    flow_network.add_edge((v,u), min_flow)
            else:
                flow[v,u] -= min_flow
                flow_network.weights[(v,u)] += min_flow
                flow_network.weights[(u, v)] -= min_flow
    return flow

