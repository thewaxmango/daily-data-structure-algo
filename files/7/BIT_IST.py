from Implicit_Segtree import SSNode

class BIT_IST:
    def __init__(self, size = 2 << 17) -> None:
        self.size = size
        self.st: list[SSNode] = [SSNode()] * size

    def update(self, x: int, y: int, val: int) -> None:
        while x < self.size:
            self.st[x].update(y, val)
            x += x & -x
    
    def query_l(self, x: int, yl: int, yr: int) -> int:
        res: int = 0
        while x:
            res += self.st[x].query(yl, yr)
            x -= x & -x
        return res
    
    def query(self, xl: int, xr: int, yl: int, yr: int) -> int:
        return self.query_l(xr, yl, yr) - self.query_l(xl-1, yl, yr)
