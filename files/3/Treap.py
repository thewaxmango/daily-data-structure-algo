# translated from cp-algo
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from random import random

@dataclass
class Treap_Node:
    key: int = -1
    prio: float = random()
    l: Optional[Treap_Node] = None
    r: Optional[Treap_Node] = None

# returns l, r
def split(t: Optional[Treap_Node], key: int) -> tuple[Optional[Treap_Node], Optional[Treap_Node]]:
    if not t:
        return (None, None)
    elif t.key <= key:
        t.r, r = split(t.r, key)
        return (t, r)
    else:
        l, t.l = split(t.l, key)
        return (l, t)

# returns modified t
def insert(t: Optional[Treap_Node], it: Treap_Node) -> Treap_Node:
    if not t:
        return it
    elif it.prio > t.prio:
        it.l, it.r = split(t, it.key)
        return it
    elif t.key <= it.key:
        t.r = insert(t.r, it)
        return t
    else:
        t.l = insert(t.l, it)
        return t

# returns t
def merge(l: Optional[Treap_Node], r: Optional[Treap_Node]) -> Optional[Treap_Node]:
    if not (l and r):
        return l if l else r
    elif l.prio > r.prio:
        l.r = merge(l.r, r)
        return l
    else:
        r.l = merge(l, r.l)
        return r
    
# returns modified t
def erase(t: Optional[Treap_Node], key: int) -> Optional[Treap_Node]:
    if not t:
        return t
    elif t.key == key:
        return merge(t.l, t.r)
    elif key < t.key:
        t.l = erase(t.l, key)
        return t
    else:
        t.r = erase(t.r, key)
        return t

def unite(l: Optional[Treap_Node], r: Optional[Treap_Node]) -> Optional[Treap_Node]:
    if not (l and r):
        return l if l else r
    if l.prio < r.prio:
        l, r = r, l
    lt, rt = split(r, l.key)
    l.l = unite(l.l, lt)
    r.l = unite(l.r, rt)
    return l
