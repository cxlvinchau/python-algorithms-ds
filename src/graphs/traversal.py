from graphs.graph import Graph
from collections import deque


def dfs(g: Graph, start=0):
    """Depth first search"""
    visited = set()
    stack = [start]
    while stack:
        current = stack.pop()
        visited.add(current)
        for t in g.get_succs(current):
            if t not in visited:
                stack.append(t)


def bfs(g: Graph, start=0):
    """Breadth first search"""
    visited = set()
    queue = deque([start])
    while queue:
        current = queue.popleft()
        visited.add(current)
        for t in g.get_succs(current):
            if t not in visited:
                queue.append(t)


def tarjan(g: Graph, start=0):
    """Returns strongly connected components in linear time"""
    n, num, active = 0, dict(), set()
    stack = [start]
    w = []
    while stack:
        current = stack[-1]
        if current in num:
            stack.pop()
            if w[-1][0] == current:
                scc = w.pop()
                for t in scc[1]:
                    active.remove(t)
                print(scc)
        else:
            num[current] = n
            n += 1
            active.add(current)
            w.append((current, {current}))
            for t in g.get_succs(current):
                if t in active:
                    d = set()
                    while num[w[-1][0]] > num[t]:
                        d = d.union(w.pop()[1])
                    u = w[-1][0]
                    d = d.union(w.pop()[1])
                    w.append((u, d))
                elif t not in num:
                    stack.append(t)


def tarjan_rec(g: Graph, start=0):
    n, num, active = 0, dict(), set()
    w = []
    def rec_dfs(v):
        nonlocal n
        num[v] = n
        n += 1
        active.add(v)
        w.append((v, {v}))
        for t in g.get_succs(v):
            if t not in num:
                rec_dfs(t)
            elif t in active:
                d = set()
                while num[w[-1][0]] > num[t]:
                    d = d.union(w.pop()[1])
                u = w[-1][0]
                d = d.union(w.pop()[1])
                w.append((u, d))
        if w[-1][0] == v:
            scc = w.pop()
            print(scc[1])
            for t in scc[1]:
                active.remove(t)

    rec_dfs(start)


