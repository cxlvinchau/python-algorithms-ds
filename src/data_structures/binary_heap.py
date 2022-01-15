class BinaryHeap:
    """Min heap"""

    def __init__(self):
        self.h = []

    def insert(self, e):
        self.h.append(e)
        self._sift_up(len(self.h)-1)

    def _sift_up(self, i):
        while i > 0 and self.h[(i-1)//2] > self.h[i]:
            self.h[(i-1)//2], self.h[i] = self.h[i], self.h[(i-1)//2]
            i = (i-1)//2

    def __sift_down(self, i):
        while 2*i+1 < len(self.h):
            j = 2*i+1
            if 2*i+2 < len(self.h):
                j = 2*i+2
            if self.h[2*i+1] < self.h[j]:
                self.h[i], self.h[2*i+1] = self.h[2*i+1], self.h[i]
                i = 2*i+1
            else:
                self.h[i], self.h[j] = self.h[j], self.h[i]
                i = j

    def build(self, h):
        self.h = h
        for i in range(len(h)//2-1, -1, -1):
            self.__sift_down(i)

    def print_heap(self, i=0, depth=0):
        if i >= len(self.h):
            return
        prefix = "-"*depth
        print(prefix + str(self.h[i]))
        self.print_heap(i=2*i+1, depth=depth+1)
        self.print_heap(i=2*i+2, depth=depth+1)

    def delete_min(self):
        e = self.h[0]
        self.h[0] = self.h[-1]
        self.h = self.h[:-1]
        self.__sift_down(0)
        return e

