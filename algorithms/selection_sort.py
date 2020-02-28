# Selection Sort Algorithm

"""
    Selection sort algorithm is an in-place comparison-based
    algorithm in which the list is divided into two parts,
    the sorted part at the left end and the unsorted part
    at the right end.

    Initially, the sorted part is empty and the unsorted
    part is the entire list.
"""

from random import sample


class SelectionSort:

    def __init__(self, unsorted, n):
        self._selection_sort(unsorted, n)

    @staticmethod
    def selection_sort(unsorted):
        """ selection sort algorithm (unused) """
        n = len(unsorted)
        _sorted = []
        for _ in range(0, n):
            val = min(unsorted)
            _sorted.append(val)
            unsorted.remove(val)
        del unsorted

    @staticmethod
    def _selection_sort(unsorted, n):
        """ selection sort algorithm inplsace """
        for i in range(0, n):
            min_ = min(unsorted[i:])
            min_index = unsorted.index(min_)
            swap = unsorted[i]
            unsorted[i] = min_
            unsorted[min_index] = swap


if __name__ == '__main__':
    a = sample(range(1000), 1000)
    solver = SelectionSort(a, len(a))
    print(a)
