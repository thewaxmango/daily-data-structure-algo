class DSU_Rollback:
    def __init__(self, size: int) -> None:
        self.e: list[int] = [-1]*size
        self.mod: list[tuple[int, int, int, int]] = []
    def find(self, x: int) -> int:
        return x if self.e[x] < 0 else self.find(self.e[x])
    def conn(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    def size(self, x: int) -> int:
        return -self.e[self.find(x)]
    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if (x == y):
            self.mod.append((-1, -1, -1, -1))
            return False
        if self.e[x] > self.e[y]:
            x, y = y, x
        self.mod.append((x, y, self.e[x], self.e[y]))
        self.e[x] += self.e[y]
        self.e[y] = x
        return True
    def rollback(self) -> None:
        if not self.mod:
            return
        a, b, c, d = self.mod.pop()
        if a != -1:
            self.e[a] = c
            self.e[b] = d
