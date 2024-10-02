# Codeforces 118E: Bertown Roads
# AC

from sys import stdin, stdout

def I(): return stdin.readline().strip(" \r\n")
def II(): return int(I())
def IL(): return I().split()
def ICL(): return list(I())
def IIL(): return list(map(int, IL()))
def IFL(): return list(map(float, IL()))
def IM(): return map(str, IL())
def IIM(): return map(int, IL())
def IFM(): return map(float, IL())
def ICLM(): return map(int, ICL())
def P(*args,sep=' ',end=''): stdout.write(sep.join([str(s) for s in args]) + end)
def PL(*args,sep=' '): P(*args, sep=sep, end='\n')
def PA(arg,end='\n'): P(*arg, sep='\n', end=end)
def F(): stdout.flush()
def Y(): PL("YES")
def N(): PL("NO")

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
        #PL(dfs)
        self.bridges = [n == 0 and i != self.root for i, n in enumerate(dfs)]
    
    def is_connected(self) -> bool:
        return self.span_edges_up.count(-1) == 1

def main():
    #for _ in range(II()):
	    solve()

def solve():
    n, m = IIM()
    graph = [set() for _ in range(n)]
    for _ in range(m):
        a, b = IIM()
        a -= 1
        b -= 1
        graph[a].add(b)
        graph[b].add(a)
    dfst = DFS_Tree(graph)    
    dfst.gen_bridges()

    if not dfst.is_connected() or any(dfst.bridges):
        PL(0)
        return
    
    for i in range(n):
        for v in dfst.span_edges_down[i]:
            PL(i + 1, v + 1)
        for v in dfst.back_edges_up[i]:
            PL(i + 1, v + 1)

if __name__ == "__main__":
    main()
