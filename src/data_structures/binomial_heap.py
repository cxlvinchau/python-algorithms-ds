import copy
from typing import Deque
from collections import deque


class BinomialTree:

    def __init__(self, val):
        self.val = val
        self.order = 0
        self.children: Deque[BinomialTree] = deque()

    def __add__(self, other):
        if isinstance(other, BinomialTree):
            if other.order != self.order:
                raise ValueError("BinomialTrees have to have the same order")
            t1, t2 = copy.deepcopy(other), copy.deepcopy(self)
            if t1.val < t2.val:
                t1.children.appendleft(t2)
                t1.order += 1
                return t1
            t2.children.appendleft(t1)
            t2.order += 1
            return t2
        raise TypeError()

    def to_str(self, depth=0):
        if self.order == 0:
            return str(self.val)
        s = str(self.val) + "\n" + "  "*(depth+1)
        s += ("\n" + "  "*(depth+1)).join(map(lambda x: x.to_str(depth=depth+1), self.children))
        return s


class BinomialForest:

    def __init__(self, trees=None, min_pointer=None):
        self.trees = dict() if trees is None else trees
        self.min_pointer = min_pointer

    def __add__(self, other):
        if isinstance(other, BinomialForest):
            max_order = 0
            if len(other.trees) > 0:
                max_order = max(max_order, max(other.trees))
            if len(self.trees) > 0:
                max_order = max(max_order, max(self.trees))
            carry = None
            result = dict()
            min_val, min_pointer = float("inf"), None
            for i in range(0, max_order+2):
                if carry is not None:
                    if i in other.trees and i not in self.trees:
                        carry = carry + other.trees[i]
                    elif i not in other.trees and i in self.trees:
                        carry = carry + self.trees[i]
                    else:
                        result[i] = carry
                        carry = None
                else:
                    if i in other.trees and i in self.trees:
                        carry = other.trees[i] + self.trees[i]
                    elif i in other.trees or i in self.trees:
                        result[i] = other.trees[i] if i in other.trees else self.trees[i]
                if i in result and result[i].val < min_val:
                    min_val, min_pointer = result[i].val, i
            return BinomialForest(trees=result, min_pointer=min_pointer)
        raise TypeError()


class BinomialHeap:

    def __init__(self):
        self.forest = BinomialForest()

    def insert(self, val):
        self.forest += BinomialForest({0: BinomialTree(val)}, min_pointer=0)

    def get_min(self):
        return self.forest.trees[self.forest.min_pointer].val

    def delete_min(self):
        val = self.get_min()
        tree = self.forest.trees.pop(self.forest.min_pointer)
        forest = BinomialForest({t.order: t for t in tree.children}, min_pointer=None)
        self.forest += forest
        return val

    def print_heap(self):
        for order, tree in self.forest.trees.items():
            print(f"Order {order}")
            print(tree.to_str())
            print("")


if __name__ == "__main__":
    import random
    heap = BinomialHeap()
    l = list(range(6))
    random.seed(0)
    random.shuffle(l)
    for i in l:
        heap.insert(i)
    heap.print_heap()
    heap.delete_min()
    heap.print_heap()
    heap.delete_min()
    print("---")
    heap.print_heap()