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

    def __init__(self, unsorted):
        self.selection_sort(unsorted)

    @staticmethod
    def selection_sort(unsorted):
        """ selection sort algorithm 1 """
        n = len(unsorted)
        _sorted = []
        for _ in range(0, n):
            val = min(unsorted)
            _sorted.append(val)
            unsorted.remove(val)
        del unsorted

    @staticmethod
    def _selection_sort(arr):
        """ selection sort algorithm 2 """
        n = len(arr)
        for i in range(0, n):
            min_ = min(arr[i:])
            min_index = arr.index(min_)
            swap = arr[i]
            arr[i] = min_
            arr[min_index] = swap

