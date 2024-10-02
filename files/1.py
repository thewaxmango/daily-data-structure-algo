# DFS tree!!

from typing import List, Set
Graph = List[Set[int]]
Up_Tree = List[int]

def dfs_tree(graph: Graph, root: int = 0) -> tuple[Up_Tree, Graph, Graph, Graph]:
    n = len(graph)
    span_edges_up: Up_Tree = [-1]*n
    span_edges_down: Graph = [set() for _ in range(n)]
    back_edges_up: Graph = [set() for _ in range(n)]
    back_edges_down: Graph = [set() for _ in range(n)]
    
    stack = [root]
    passed = [False] * n
    while stack:
        node = stack.pop()
        passed[node] = True
        for adj in graph[node]:
            if not passed[adj]:
                stack.append(adj)
                span_edges_down[adj].add(node)
                span_edges_up[node] = adj
            elif adj != span_edges_up[node]:
                
                back_edges_down[adj].add(node)
                back_edges_up[node].add(adj)
    
    return (span_edges_up, span_edges_down, back_edges_up, back_edges_down)

def bridge(dfs_tree: tuple[Up_Tree, Graph, Graph, Graph], root: int = 0):
    dfs = [0]*len(dfs_tree[0])
    stack = [root]
    while stack:
        node = stack.pop()
        if node < 0:
            node = ~node
            for child in dfs_tree[1][node]:
                dfs[node] += dfs[child]
        else:
            stack.append(~node)
            dfs[node] += len(dfs_tree[2][node]) - len(dfs_tree[3][node])
            for child in dfs_tree[1][node]:
                stack.append(child)
    return [n == 0 for n in dfs]
