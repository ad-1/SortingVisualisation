# Insertion Sort Algorithm

"""
    Insertion sort is a simple sorting algorithm that builds
    the final sorted array (or list) one item at a time.

    It is much less efficient on large lists than more advanced
    algorithms such as quicksort, heapsort, or merge sort.
"""


class InsertionSort:

    def __init__(self, unsorted, n):
        self._insertion_sort(unsorted, n)

    @staticmethod
    def insertion_sort(arr, n):
        """ insertion sort algorithm 1 """
        for i in range(1, n):
            val = arr[i]
            for j in range(0, i):
                if arr[j] > val:
                    arr[j + 1:i + 1] = arr[j:i]
                    arr[j] = val
                    break

    @staticmethod
    def _insertion_sort(arr, n):
        """ insertion sort algorithm """
        for i in range(1, n):
            val = arr[i]
            hole = i
            while hole > 0 and arr[hole - 1] > val:
                arr[hole] = arr[hole - 1]
                hole -= 1
            arr[hole] = val


if __name__ == '__main__':
    a = [76766, 43, 56, 23, 6, 39, 34435, 8, 2]
    n = len(a)
    solver = InsertionSort(a, n)
    print(a)
