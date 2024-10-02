from typing import List, Set
Graph = List[Set[int]]
Up_Tree = List[int]

class DFS_Tree:
    def __init__(self, graph: Graph, root: int = 0) -> None:
        self.n = len(graph)
        self.root = root
        
        self.span_edges_up: Up_Tree = [-1]*self.n
        self.span_edges_down: Graph = [set() for _ in range(self.n)]
        self.back_edges_up: Graph = [set() for _ in range(self.n)]
        self.back_edges_down: Graph = [set() for _ in range(self.n)]
        
        self.bridges: list[bool] = []
        
        # (parent, cur)
        stack = [(-1, root)]
        passed = [False] * self.n
        while stack:
            par, node = stack.pop()
            
            if self.span_edges_up[node] == -1:
                if par != -1:
                    self.span_edges_down[par].add(node)
                self.span_edges_up[node] = par
            elif par not in self.back_edges_down[node]:
                self.back_edges_down[par].add(node)
                self.back_edges_up[node].add(par)
            
            for adj in graph[node]:
                if not passed[adj]:
                    stack.append((node, adj))
            passed[node] = True

    def gen_bridges(self) -> None:
        dfs = [0]*self.n
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node < 0:
                node = ~node
                for child in self.span_edges_down[node]:
                    dfs[node] += dfs[child]
            else:
                stack.append(~node)
                dfs[node] += len(self.back_edges_up[node]) - len(self.back_edges_down[node])
                for child in self.span_edges_down[node]:
                    stack.append(child)
        self.bridges = [n == 0 and i != self.root for i, n in enumerate(dfs)]
    
    def is_connected(self) -> bool:
        return self.span_edges_up.count(-1) == 1
