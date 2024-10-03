# translated from benq's SparseSeg
from __future__ import annotations
from typing import Optional

#^ ints only, queries inclusively
class SSNode:
    SZ: int = 2**17
    
    def __init__(self):
        self.val: int = 0
        self.n0 : Optional[SSNode] = None
        self.n1 : Optional[SSNode] = None
    
    def update(self, index: int, value: int, L: int = 0, R: int = SZ-1) -> None:
        if L == index and R == index:
            self.val += value
            return
        M: int = (L + R) // 2
        if index <= M:
            if not self.n0:
                self.n0 = SSNode()
            self.n0.update(index, value, L, M)
        else:
            if not self.n1:
                self.n1 = SSNode()
            self.n1.update(index, value, M+1, R)
        self.val = 0
        if self.n0:
            self.val += self.n0.val
        if self.n1:
            self.val += self.n1.val
    
    def query(self, lo: int, hi: int, L: int = 0, R: int = SZ-1) -> int:
        if (hi < L or R < lo):
            return 0
        if (lo <= L and R <= hi):
            return self.val
        M: int = (L + R) // 2
        res: int = 0
        if self.n0: 
            res += self.n0.query(lo, hi, L, M)
        if self.n1:
            res += self.n1.query(lo, hi, M+1, R)
        return res

    def __upd(self, index: int, node0: Optional[SSNode], node1: Optional[SSNode], L: int = 0, R: int = SZ-1) -> None:
        if L != R:
            M: int = (L + R) // 2
            if index <= M:
                if not self.n0:
                    self.n0 = SSNode()
                self.n0.__upd(index, node0.n0 if node0 else None, node1.n0 if node1 else None, L, M)  
            else:
                if not self.n1:
                    self.n1 = SSNode()
                self.n1.__upd(index, node0.n1 if node0 else None, node1.n1 if node1 else None, M+1, R)
        self.val = (node0.val if node0 else 0) + (node1.val if node1 else 0)
        
def main():
    pass

if __name__ == "__main__":
    main()
