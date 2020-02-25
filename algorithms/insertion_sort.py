# Insertion Sort Algorithm

"""
    Insertion sort is a simple sorting algorithm that builds
    the final sorted array (or list) one item at a time.

    It is much less efficient on large lists than more advanced
    algorithms such as quicksort, heapsort, or merge sort.
"""


class InsertionSort:

    def __init__(self, unsorted):
        self.insertion(unsorted)

    @staticmethod
    def insertion(arr):
        """ insertion sort algorithm 1 """
        n = len(arr)
        for i in range(1, n):
            val = arr[i]
            for j in range(0, i):
                if arr[j] > val:
                    arr[j + 1:i + 1] = arr[j:i]
                    arr[j] = val
                    break

    @staticmethod
    def _insertion(arr):
        """ insertion sort algorithm 2 """
        n = len(arr)
        for i in range(0, n):
            val = arr[i]
            hole = i
            while hole > 0 and arr[hole - 1] > val:
                arr[hole] = arr[hole - 1]
                hole -= 1
            arr[hole] = val
