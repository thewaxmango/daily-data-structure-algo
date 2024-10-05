from typing import Union, Sequence
from dataclasses import dataclass
Number = Union[int, float]

@dataclass
class IH_Node:
    l: Number = float("inf")
    r: Number = float("-inf")

class Interval_Heap:
    L = 0
    R = 1
    
    def __init__(self, initial: Sequence[Number] = []) -> None:
        self.n = 0
        self.heap: list[IH_Node] = []
        for v in initial:
            self.insert(v)
    
    def __bubble_up(self, index: int, parity: int) -> int:
        ptr: int = index
        if parity == self.L:        # min heap
            while ptr > 0:
                par = (ptr - 1) // 2
                if self.heap[par].l <= self.heap[ptr].l:
                    return ptr
                self.heap[par].l, self.heap[ptr].l = self.heap[ptr].l, self.heap[par].l
                ptr = par
        else:                       # max heap
            while ptr > 0:
                par = (ptr - 1) // 2
                if self.heap[par].r >= self.heap[ptr].r:
                    return ptr
                self.heap[par].r, self.heap[ptr].r = self.heap[ptr].r, self.heap[par].r
                ptr = par
        return ptr
    
    def __bubble_down(self, index: int, parity: int) -> int:
        ptr: int = index
        if parity == self.L:        # min heap
            while self.n > ptr * 4 + 2:
                ch_l = ptr * 2 + 1
                ch_r = ptr * 2 + 2
                if ch_r >= len(self.heap) or self.heap[ch_l].l <= self.heap[ch_r].l:          # right child DNE or greater equal to left
                    if self.heap[ch_l].l >= self.heap[ptr].l:
                        return ptr
                    self.heap[ch_l].l, self.heap[ptr].l = self.heap[ptr].l, self.heap[ch_l].l
                    ptr = ch_l
                else:
                    if self.heap[ch_r].l >= self.heap[ptr].l:
                        return ptr
                    self.heap[ch_r].l, self.heap[ptr].l = self.heap[ptr].l, self.heap[ch_r].l
                    ptr = ch_r
                self.reorder(ptr)
        else:                       # max heap
            while self.n > ptr * 4 + 3:
                ch_l = ptr * 2 + 1
                ch_r = ptr * 2 + 2
                if ch_r >= len(self.heap) or self.heap[ch_l].r >= self.heap[ch_r].r:          # right child DNE or less equal to left
                    if self.heap[ch_l].r <= self.heap[ptr].r:
                        return ptr
                    self.heap[ch_l].r, self.heap[ptr].r = self.heap[ptr].r, self.heap[ch_l].r
                    ptr = ch_l
                else:
                    if self.heap[ch_r].r <= self.heap[ptr].r:
                        return ptr
                    self.heap[ch_r].r, self.heap[ptr].r = self.heap[ptr].r, self.heap[ch_r].r
                    ptr = ch_r
                self.reorder(ptr)
        return ptr
    
    def reorder(self, index: int) -> None:
        if self.n == index * 2 + 1:
            return
        if self.heap[index].l > self.heap[index].r:
            self.heap[index].l, self.heap[index].r = self.heap[index].r, self.heap[index].l
            
    def insert(self, value: Number) -> None:
        self.n += 1
        if self.n == 1:                                         # if empty
            self.heap.append(IH_Node(value))
        elif self.n & 1:                                        # if heap was even, add a new node and swap with parent as necessary
            par: int = (len(self.heap) - 1) // 2
            if value < self.heap[par].l:                        # less than left parent
                self.heap.append(IH_Node(self.heap[par].l))
                self.heap[par].l = value
                self.__bubble_up(par, self.L)
            elif value > self.heap[par].r:                      # greater than right parent
                self.heap.append(IH_Node(self.heap[par].r))
                self.heap[par].r = value
                self.__bubble_up(par, self.R)
            else:                                               # in the middle
                self.heap.append(IH_Node(value))
        else:                                                   # if heap was odd, place and sort inside last node and bubble as necessary
            cur: int = len(self.heap) - 1
            if value < self.heap[cur].l:                         # if is smaller than and should switch with sibling
                self.heap[cur].r = self.heap[cur].l
                self.heap[cur].l = value
                self.__bubble_up(cur, self.L)
            else:                                             # if greater than or equal to sibling
                self.heap[cur].r = value
                self.__bubble_up(cur, self.R)
         
    def pop_min(self) -> Number:
        self.n -= 1
        ret: Number = self.heap[0].l
        if self.n == 0:                                         # if last element, empty heap
            self.heap.pop()
        elif self.n & 1 == 0:                                   # if was odd, replace with last element and pop empty node
            self.heap[0].l = self.heap[-1].l 
            self.heap.pop()
            self.reorder(self.__bubble_down(0, self.L))
        else:                                                   # otherwise need to pop appropriate left one and shift right one over
            self.heap[0].l = self.heap[-1].l
            self.heap[-1].l, self.heap[-1].r = self.heap[-1].r, float("-inf")
            self.reorder(self.__bubble_down(0, self.L))
        return ret
    
    def pop_max(self) -> Number:
        self.n -= 1
        if self.n == 0:                                         # if last element, empty heap
            ret: Number = self.heap[0].l
            self.heap.pop()
            return ret
        
        ret: Number = self.heap[0].r
        if self.n == 1:                                         # if second to last element, simply remove from root node
            self.heap[0].r = float("-inf")
        elif self.n & 1 == 0:                                   # if was odd, replace with last element and pop empty node
            self.heap[0].r = self.heap[-1].l
            self.heap.pop()
            self.reorder(self.__bubble_down(0, self.R))
        else:
            self.heap[0].r = self.heap[-1].r
            self.heap[-1].r = float("-inf")
            self.reorder(self.__bubble_down(0, self.R))    
        return ret
