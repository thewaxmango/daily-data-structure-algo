# Finds maximum on a unimodal function
# Unimodal: strictly increasing to max then strictly decreasing

from typing import Optional, Callable

def Ternary_Search(arr: list, L: int = 0, R: Optional[int] = None) -> int:
    if R == None:
        R = len(arr)
    while L < R - 2:
        C1: int = L + (R - L) // 3
        C2: int = R + (L - R) // 3
        if arr[C1] < arr[C2]:
            L = C1
        else:
            R = C2
    return max(list(range(L, R)), key = lambda x: arr[x])

def Ternary_Func_Search(f: Callable, L: float = 0, R: float = 10**9, precision: float = 10**(-9)) -> float:
    while R - L > precision:
        C1: float = (2*L + R) / 3
        C2: float = (L + 2*R) / 3
        if f(C1) < f(C2):
            L = C1
        else:
            R = C2
    return L

def main():
    q = Ternary_Search([0, 1, 2, 3, 4, 5, 6, 5, 4, 2, 0])
    print(q)
    r = Ternary_Func_Search(lambda x: -abs(x - 1), 0, 10)
    print(r)

if __name__ == "__main__":
    main()
