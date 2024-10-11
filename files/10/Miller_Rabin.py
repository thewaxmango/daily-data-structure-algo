# primality test taken from cp-algorithms
# fast if combined with simply testing small primes (88% of all numbers have a prime factor smaller than 100)

from random import randint
def rand() -> int: return randint(0, 2**30)

def binpower(base: int, e: int, mod: int) -> int:
    res: int = 1
    base %= mod
    while e:
        if e&1:
            res = res * base % mod
        base = base * base % mod
        e >>= 1
    return res

def check_composite(n: int, a: int, d: int, s: int) -> bool:
    x: int = binpower(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(1, s):
        x = x * x % n
        if x == n - 1:
            return False
    return True

def Miller_Rabin(n: int, iter: int = 5):
    if n < 4:
        return n == 2 or n == 3
    
    s: int = 0
    d: int = n - 1
    while (d & 1) == 0:
        d >>= 1
        s += 1
    
    for _ in range(iter):
        a: int = 2 + rand() % (n - 3)
        if check_composite(n, a, d, s):
            return False
    return True

def Miller_Rabin_Deterministic(n: int):
    if n < 2:
        return False
    
    r: int = 0
    d: int = n - 1
    while (d & 1) == 0:
        d >>= 1
        r += 1
        
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n == a:
            return True
        if check_composite(n, a, d, r):
            return False
    return True
