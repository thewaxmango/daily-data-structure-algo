# yosupo judge "Eertree"

from sys import stdin, stdout

def I(): return stdin.readline().strip(" \r\n")
def II(): return int(I())
def IL(): return I().split()
def ICL(): return list(I())
def IIL(): return list(map(int, IL()))
def IM(): return map(str, IL())
def IIM(): return map(int, IL())
def ICLM(): return map(int, ICL())
def P(*args,sep=' ',end=''): stdout.write(sep.join([str(s) for s in args]) + end)
def PL(*args,sep=' '): P(*args, sep=sep, end='\n')
def PLi(arg,end='\n'): P(*arg, sep='\n', end=end)
def F(): stdout.flush()
def Y(): PL("YES")
def N(): PL("NO")

from typing import Callable

class Palindromic_Tree:
    def __init__(self, length: int):
        length += 2
        self.s: list[int] = [-1] * length
        self.len: list[int] = [0] * length
        self.par: list[int] = [0] * length
        self.link: list[int] = [0] * length
        self.to: list[int] = [[] for _ in range(length)]
        self.link[0] = 1
        self.len[1] = -1
        self.n: int = 1
        self.sz: int = 2
        self.last: int = 0

    def get_link(self, v: int):
        while self.s[self.n - 1] != self.s[self.n - self.len[v] - 2]:
            v = self.link[v]
        return v

    def get(self, v: int, c: int):
        for cu in self.to[v]:
            if cu & 255 == c:
                return cu >> 8
        return 0

    def add_letter(self, c: int):
        c = ord(c) - 97
        self.s[self.n] = c
        self.n += 1
        self.last = self.get_link(self.last)
        if not self.get(self.last, c):
            u: int = self.get(self.get_link(self.link[self.last]), c)
            self.link[self.sz] = u
            self.par[self.sz] = self.last
            self.len[self.sz] = self.len[self.last] + 2
            self.to[self.last].append((self.sz << 8) | c)
            self.sz += 1
        self.last = self.get(self.last, c)

    def sufpal(self, adjust: Callable[[int], int] = lambda x: x):
        return adjust(self.last)

    def print(self, adjust: Callable[[int], int] = lambda x: x):
        print(self.sz - 2)
        for i in range(2, self.sz):
            print(adjust(self.par[i]), adjust(self.link[i]))

def main():
    #for _ in range(II()):
        solve()

def solve():
    def yosupo(v):
        if (v == 1):
            return -1
        elif (v > 1):
            return v - 1
        else:
            return 0

    s = I()
    pt = Palindromic_Tree(len(s))
    lasts = []
    for c in s:
        pt.add_letter(c)
        lasts.append(pt.sufpal(yosupo))
    pt.print(yosupo)
    PL(*lasts)
    
if __name__ == "__main__":
	main()

