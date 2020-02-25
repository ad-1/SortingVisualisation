# Quick Sort Algorithm

"""
    Quicksort is an efficient sorting algorithm.
    When implemented well, it can be about two or three times faster
    than its main competitors, merge sort and heapsort.
"""


class QuickSort:

    def __init__(self, unsorted, start, end):
        self.counter = 0
        self.quick(unsorted, start, end)

    def quick(self, unsorted, start, end):
        """ quick sort recursive algorithm """
        if start >= end:
            return
        n = len(unsorted)
        self.counter += 1
        i_pivot = self.partition(unsorted, start, end - 1)
        self.quick(unsorted, start, i_pivot)
        self.quick(unsorted, i_pivot + 1, n)

    @staticmethod
    def partition(unsorted, start, end):
        """ arrange (left array < pivot) and (right array > pivot) """
        pivot = unsorted[end]
        i_pivot = start
        for i in range(start, end):
            if unsorted[i] <= pivot:
                v1 = unsorted[i]
                v2 = unsorted[i_pivot]
                unsorted[i_pivot] = v1
                unsorted[i] = v2
                i_pivot += 1
        v1 = unsorted[i_pivot]
        unsorted[i_pivot] = pivot
        unsorted[end] = v1
        return i_pivot


if __name__ == '__main__':
    _arr = [100, 2, 6, 1, 4, 10, 20, 3, 56, 18, 12]
    _start, _end = 0, len(_arr)
    quick = QuickSort(_arr, _start, _end)
    print(_arr)
    print(quick.counter)
