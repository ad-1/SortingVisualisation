# Merge Sorting Algorithm

"""
    Merge sort is an efficient, general-purpose, comparison-based sorting algorithm.
    Most implementations produce a stable sort, which means that the order of equal
    elements is the same in the input and output.

    Merge sort is a divide and conquer algorithm.
"""


class MergeSort:

    def __init__(self, unsorted):
        self.counter = 0
        self.divide(unsorted)

    def divide(self, unsorted):
        """ recrusive function to divide array into 2 sub arrays for sorting """
        self.counter += 1
        n = len(unsorted)
        if n < 2:
            return
        mid = n // 2
        left = unsorted[0:mid]
        right = unsorted[mid: n]
        self.divide(left)
        self.divide(right)
        self.merge(left, right, unsorted)

    @staticmethod
    def merge(left, right, unsorted):
        """ merging two sorted arrays to one sorted array """
        n_left, n_right = len(left), len(right)
        i, j, k = 0, 0, 0
        while i < n_left and j < n_right:
            if left[i] <= right[j]:
                unsorted[k] = left[i]
                i += 1
            else:
                unsorted[k] = right[j]
                j += 1
            k += 1
        while i < n_left:
            unsorted[k] = left[i]
            k += 1
            i += 1
        while j < n_right:
            unsorted[k] = right[j]
            k += 1
            j += 1
