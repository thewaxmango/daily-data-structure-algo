# translated from benq's SparseSeg
from __future__ import annotations
from typing import Optional, TypeVar, Generic, Callable

#^ queries inclusively
#^ operation should be commutative and associative
T = TypeVar('T')
class SSNodeT(Generic[T]):
    SZ: int = 2**17
    
    def __init__(self, operation: Callable[[T, T], T], default: T) -> None:
        self.dft = default
        self.val: T = default
        self.op: Callable[[T, T], T] = operation
        self.n0: Optional[SSNodeT[T]] = None
        self.n1: Optional[SSNodeT[T]] = None
    
    def new(self) -> SSNodeT[T]:
        return SSNodeT[T](self.op, self.dft)
    
    def update(self, index: int, value: T, L: int = 0, R: int = SZ-1) -> None:
        if L == index and R == index:
            self.val = self.op(self.val, value)
            return
        M: int = (L + R) // 2
        if index <= M:
            if not self.n0:
                self.n0 = self.new()
            self.n0.update(index, value, L, M)
        else:
            if not self.n1:
                self.n1 = self.new()
            self.n1.update(index, value, M+1, R)
        self.val = self.dft
        if self.n0:
            self.val = self.op(self.val, self.n0.val)
        if self.n1:
            self.val = self.op(self.val, self.n1.val)
    
    def query(self, lo: int, hi: int, L: int = 0, R: int = SZ-1) -> T:
        if (hi < L or R < lo):
            return self.dft
        if (lo <= L and R <= hi):
            return self.val
        M: int = (L + R) // 2
        res: T = self.dft
        if self.n0: 
            res = self.op(res, self.n0.query(lo, hi, L, M))
        if self.n1:
            res = self.op(res, self.n1.query(lo, hi, M+1, R))
        return res

    def __upd(self, index: int, node0: Optional[SSNodeT[T]], node1: Optional[SSNodeT[T]], L: int = 0, R: int = SZ-1) -> None:
        if L != R:
            M: int = (L + R) // 2
            if index <= M:
                if not self.n0:
                    self.n0 = self.new()
                self.n0.__upd(index, node0.n0 if node0 else None, node1.n0 if node1 else None, L, M)  
            else:
                if not self.n1:
                    self.n1 = self.new()
                self.n1.__upd(index, node0.n1 if node0 else None, node1.n1 if node1 else None, M+1, R)
        self.val = self.op(node0.val if node0 else self.dft, node1.val if node1 else self.dft)
        
def main():
    pass

if __name__ == "__main__":
    main()
