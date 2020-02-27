# Bubble Sort or Sinking Sort Algorithm

"""
    Repeatedly steps through the list, compares adjacent
    elements and swaps them if they are in the wrong order.

    The pass through the list is repeated until the list is sorted.

    The algorithm, which is a comparison sort, is named for
    the way smaller or larger elements "bubble" to the top of the list.
"""


class BubbleSort:

    def __init__(self, unsorted, n):
        self.bubble(unsorted, n)

    @staticmethod
    def bubble(unsorted, n):
        """ bubble sort algorithm """
        for i in range(0, n - 1):
            swapped = False
            for j in range(0, n - 1 - i):
                if unsorted[j] > unsorted[j + 1]:
                    val = unsorted[j]
                    swap = unsorted[j + 1]
                    unsorted[j] = swap
                    unsorted[j + 1] = val
                    swapped = True
            if not swapped:
                break


if __name__ == '__main__':
    a = [76766, 43, 56, 23, 6, 39, 34435, 8, 2]
    n = len(a)
    solver = BubbleSort(a, n)
    print(a)
