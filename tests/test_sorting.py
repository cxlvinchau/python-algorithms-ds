import unittest
import random
from src.algorithms.sorting import BubbleSort, MergeSort, Quicksort, Quickselect


class TestSorting(unittest.TestCase):

    def setUp(self) -> None:
        self.l = list(range(40)) + list(range(10))
        random.seed(0)
        random.shuffle(self.l)

    def test_bubble_sort(self):
        self.assertEqual(BubbleSort().sort(self.l), sorted(self.l))

    def test_merge_sort(self):
        self.assertEqual(MergeSort().sort(self.l), sorted(self.l))

    def test_quick_sort(self):
        self.assertEqual(Quicksort().sort(self.l), sorted(self.l))

    def test_quick_select(self):
        expected = sorted(self.l)
        for i in range(10, len(self.l)):
            actual = Quickselect().select(self.l, i+1)
            self.assertEqual(expected[i], actual)


if __name__ == '__main__':
    unittest.main()
