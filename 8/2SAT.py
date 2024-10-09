# translated from https://sotanishy.github.io/cp-library-cpp/sat/twosat.hpp

from collections import namedtuple
Clause = tuple[int, bool, int, bool]

def Two_SAT(n: int, clauses: list[Clause]) -> list[bool]:
    G: list[list[int]] = [[] for _ in range(2*n)]
    val: list[bool] = [False]*n
    
    for i, f, j, g in clauses:
        G[n * f + i].append(n * (not g) + j)
        G[n * g + j].append(n * (not f) + i)
        
    comps = kosaraju(G)
    for i in range(n):
        if comps[i] == comps[n+i]:
            return []
        val[i] = comps[i] > comps[n + i]
    return val
    
def kosaraju(G):
    """ For a graph G given as a list of lists of node numbers
        find the strongly connected components.
        Use Kosaraju's algorithm:
        for each unvisited node, traverse and mark visited its out-neighbours,
          then add it to a sequence L
        for each unassigned node taken from L in reverse order,
          assign it to the same new SCC as all nodes reached via in-neighbours
    """
    # postorder DFT on G to transpose the graph and push root vertices to L
    N = len(G)
    T, L, visited = [[] for _ in  range(N)], [], [False] * N
    for u in range(N):
        if visited[u]:
            continue
        visited[u], stack = True, [u]
        while stack:
            u = stack[-1]
            for v in G[u]:
                T[v].append(u)
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
                    break
            else:
                stack.pop()
                L.append(u)
    # print("L:", L)
    # try and follow en.wikipedia's hint and have
    #  visited indication share storage with the final assignment
    assigned = visited
                         
    # postorder DFT on T to pop root vertices from L and mark SCCs
    assigned = visited   # C = [None] * N
    while L:
        root = L.pop()
        if not visited[root] is True:
            continue
        assigned[root] = root
        stack = [root]
        while stack:
            # print("T[" + stack[-1] + "]: " + T[stack[-1]])
            for v in T[stack[-1]]:
                if visited[v] is True:
                    stack.append(v)
                    assigned[v] = root
                    break
            else:
                stack.pop()
    
    return assigned
