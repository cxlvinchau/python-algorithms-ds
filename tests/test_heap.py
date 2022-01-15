import unittest

from data_structures.binary_heap import BinaryHeap


class TestHeap(unittest.TestCase):


    def test_binary_heap(self):
        h = BinaryHeap()
        for e in [23,3,5,6,8,9,10,10,10,23324,3]:
            h.insert(e)
        l = []
        for _ in range(7):
            l.append(h.delete_min())
        print(l)
        h.print_heap()


if __name__ == '__main__':
    unittest.main()
