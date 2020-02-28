# Quick Sort Algorithm

"""
    Quicksort is an efficient sorting algorithm.
    When implemented well, it can be about two or three times faster
    than its main competitors, merge sort and heapsort.
"""

from random import sample


class QuickSort:

    def __init__(self, unsorted, start, end):
        self.counter = 0
        self.quick_sort(unsorted, start, end)

    def quick_sort(self, unsorted, start, end):
        """ quick sort recursive algorithm """
        if start >= end:
            return
        self.counter += 1
        i_pivot = self.partition(unsorted, start, end - 1)
        self.quick_sort(unsorted, start, i_pivot)
        self.quick_sort(unsorted, i_pivot + 1, end)

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
    a = sample(range(1000), 1000)
    s, e = 0, len(a)
    solver = QuickSort(a, s, e)
    print(a)
