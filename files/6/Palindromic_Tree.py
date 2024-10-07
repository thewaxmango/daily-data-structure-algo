from collections import deque
from typing import Callable

class Palindromic_Tree:
    def __init__(self, str_len: int) -> None:
        str_len += 2
        
        self.n: int = 1
        self.sz: int = 2
        self.last: int = 0
        
        self.s: list[int] = [-1] * str_len
        self.to: list[deque[int]] = [deque() for _ in range(str_len)]
        self.len: list[int] = [0] * str_len
        self.link: list[int] = [0] * str_len
        self.par: list[int] = [0] * str_len
        
        self.link[0] = 1
        self.len[1] = -1
    
    def get_link(self, v: int) -> int:
        while self.s[self.n - 1] != self.s[self.n - self.len[v] - 2]:
            v = self.link[v]
        return v

    def get(self, v: int, c: int) -> int:
        for cu in self.to[v]:
            if (cu & 0xFF) == c:
                return cu >> 8
        return 0
    
    def add_letter(self, ch: str) -> None:
        c: int = ord(ch) - 97       # ord('a') = 97
        self.s[self.n] = c
        self.n += 1
        
        self.last: int = self.get_link(self.last)
        if not self.get(self.last, c):
            u: int = self.get(self.get_link(self.link[self.last]), c)
            self.link[self.sz] = u
            self.par[self.sz] = self.last
            self.len[self.sz] = self.len[self.last] + 2
            self.to[self.last].appendleft((self.sz << 8) | c)
            self.sz += 1
        self.last = self.get(self.last, c)
    
    def sufpal(self, adjust: Callable[[int], int] = lambda x: x) -> int:
        return adjust(self.last)
    
    def print(self, adjust: Callable[[int], int] = lambda x: x) -> None:
        print(self.sz - 2)
        for i in range(2, self.sz):
            print(f"{adjust(self.par[i])} {adjust(self.link[i])}")
