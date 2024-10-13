# Max-flow algorithm 
# Runs in O(VE^2) time
from typing import Union
from collections import deque
Numeric = Union[int, float]

class Edmonds_Karp:
    def __init__(self, capacity: list[list[Numeric]], adj: list[list[int]], size: int = -1) -> None:
        self.n = size if size != -1 else len(capacity)
        self.capacity = capacity
        self.adj = adj
    
    def bfs(self, s: int, t: int, parent: list[int]) -> Numeric:
        for i in range(len(parent)):
            parent[i] = -1
        parent[s] = -2
        q: deque[tuple[int, Numeric]] = deque([(s, float("inf"))])
        
        while q:
            cur: int = q[0][0]
            flow: Numeric = q[0][1]
            q.popleft()
            
            for next in self.adj[cur]:
                if parent[next] == -1 and self.capacity[cur][next]:
                    parent[next] = cur
                    new_flow: Numeric = min(flow, self.capacity[cur][next])
                    if next == t:
                        return new_flow
                    q.append((next, new_flow))
        
        return 0

    # s is source, t is sink
    def maxflow(self, s: int, t: int) -> Numeric:
        flow: Numeric = 0
        parent: list[int] = [0]*self.n
        new_flow: Numeric = self.bfs(s, t, parent)
        
        while new_flow:
            flow += new_flow
            cur: int = t
            while cur != s:
                prev: int = parent[cur]
                self.capacity[prev][cur] -= new_flow
                self.capacity[cur][prev] += new_flow
                cur = prev
        
        return flow
        
                    
            
            
