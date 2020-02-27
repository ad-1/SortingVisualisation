# Selection Sort Algorithm

"""
    Selection sort algorithm is an in-place comparison-based
    algorithm in which the list is divided into two parts,
    the sorted part at the left end and the unsorted part
    at the right end.

    Initially, the sorted part is empty and the unsorted
    part is the entire list.
"""


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
    a = [76766, 43, 56, 23, 6, 39, 34435, 8, 2]
    n = len(a)
    solver = SelectionSort(a, n)
    print(a)
