# Max-flow algorithm 
# Runs in O(V^2E) time

from dataclasses import dataclass
from typing import Union
from collections import deque
Numeric = Union[int, float]

@dataclass 
class DinicEdge:
    v: int = -1
    u: int = -1 
    cap: Numeric = -1
    flow: Numeric = 0

class Dinic:
    def __init__(self, n: int, s: int, t: int) -> None:
        self.edges: list[DinicEdge] = []
        self.adj: list[list[int]] = [[] for _ in range(n)]
        self.n: int = n
        self.m: int = 0
        self.s: int = s
        self.t: int = t
        self.level: list[int] = [0]*n
        self.ptr: list[int] = [0]*n
        self.q: deque[int] = deque()
        
    def add_edge(self, v: int, u: int, cap: int) -> None:
        self.edges.append(DinicEdge(v, u, cap))
        self.edges.append(DinicEdge(u, v, 0))
        self.adj[u].append(self.m)
        self.adj[v].append(self.m + 1)
        self.m += 2
    
    def bfs(self) -> bool:
        while self.q:
            v: int = self.q.popleft()
            for id in self.adj[v]:
                if self.edges[id].cap - self.edges[id].flow < 1:
                    continue
                if self.level[self.edges[id].u] != -1:
                    continue
                self.level[self.edges[id].u] = self.level[v] + 1
                self.q.append(self.edges[id].u)
        return self.level[self.t] != -1

    def dfs(self, v: int, pushed: Numeric) -> Numeric:
        if pushed == 0:
            return 0
        if v == self.t:
            return pushed
        while self.ptr[v] < len(self.adj[v]):
            id: int = self.adj[v][self.ptr[v]]
            u: int = self.edges[id].u 
            if self.level[v] + 1 != self.level[u] or self.edges[id].cap - self.edges[id].flow < 1:
                continue
            tr: Numeric = self.dfs(u, min(pushed, self.edges[id].cap - self.edges[id].flow))
            if tr == 0:
                continue
            self.edges[id].flow += tr
            self.edges[id ^ 1].flow -= tr
            return tr
        return 0

    def flow(self) -> Numeric:
        f: Numeric = 0
        while True:
            self.level = [-1]*self.n 
            self.level[self.s] = 0
            self.q.append(self.s)
            if not self.bfs():
                break
            self.ptr = [0]*self.n
            pushed: Numeric = self.dfs(self.s, float("inf"))
            while pushed:
                f += pushed
                pushed = self.dfs(self.s, float("inf"))
        return f
