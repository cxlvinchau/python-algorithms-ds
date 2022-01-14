import abc
from typing import List
import itertools
import random


class SortingAlgorithm:
    """Sort lists in ascending order"""

    @abc.abstractmethod
    def sort(self, l: List) -> List:
        pass


class BubbleSort(SortingAlgorithm):

    def sort(self, l: List) -> List:
        for _ in range(len(l)):
            f = False
            for i in range(len(l) - 1):
                if l[i] > l[i + 1]:
                    l[i], l[i + 1] = l[i + 1], l[i]
                    f = True
            if not f:
                break
        return l


class MergeSort(SortingAlgorithm):

    def sort(self, l: List) -> List:
        if len(l) == 2:
            a, b = l
            if a > b:
                return [b, a]
            return l
        if len(l) <= 1:
            return l
        m = len(l) // 2
        l1, l2 = self.sort(l[:m]), self.sort(l[m:])
        result = []
        i, j = 0, 0
        while i < len(l1) or j < len(l2):
            if i >= len(l1):
                result.append(l2[j])
                j += 1
            elif j >= len(l2):
                result.append(l1[i])
                i += 1
            elif l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        return result


class Quicksort(SortingAlgorithm):
    """Inplace sorting"""

    def sort(self, l: List) -> List:
        self._rec_sort(0, len(l), l)
        return l

    def _rec_sort(self, i, j, l):
        if j - i > 1:
            pivot = l[j-1]
            k1, k2 = 0, j - 1
            while k1 < k2:
                while l[k1] < pivot:
                    k1 += 1
                while l[k2] > pivot:
                    k2 -= 1
                if k1 < k2:
                    l[k1], l[k2] = l[k2], l[k1]
                    k1 += 1
            self._rec_sort(i, k1, l)
            self._rec_sort(k1, j, l)


class Quickselect:

    def select(self, l: List, k):
        return self.rec_select(0, len(l), k, l)

    def rec_select(self, i, j, k, l: List):
        print(l[i:j])
        if j-i == 1:
            return l[0]
        pivot = l[j-1]
        k1, k2 = i, j-1
        while k1 < k2:
            while l[k1] < pivot:
                k1 += 1
            while l[k2] > pivot:
                k2 -= 1
            if k1 < k2:
                l[k1], l[k2] = l[k2], l[k1]
                k1 += 1
        l[k1], l[j-1] = l[j-1], l[k1]
        if k1 == k-1:
            return l[k-1]
        elif k1 > k-1:
            return self.rec_select(i, k1, k, l)
        else:
            return self.rec_select(k1, j, k, l)
