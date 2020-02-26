# Sorting Algorithms Solver Class


class Solver:

    def __init__(self, unsorted, n, solve_mode, subscriber):
        self.subscriber = subscriber
        if solve_mode == 0:
            self.selection_sort(unsorted, n)
        elif solve_mode == 1:
            self.insertion_sort(unsorted, n)
        elif solve_mode == 2:
            self.bubble_sort(unsorted, n)

    @staticmethod
    def selection_sort(unsorted, n):
        """ selection sort algorithm inplace """
        for i in range(0, n):
            a = min(unsorted[i:], key=lambda x: x.value)
            a_index = unsorted.index(a)
            b = unsorted[i]
            unsorted[i] = a
            unsorted[a_index] = b
            a.index = i  # visualise
            b.index = a_index  # visualise

    @staticmethod
    def insertion_sort(unsorted, n):
        """ insertion sort algorithm """
        for i in range(1, n):
            val = unsorted[i].value
            hole = i
            while hole > 0 and unsorted[hole - 1].value > val:
                unsorted[hole].value = unsorted[hole - 1].value
                unsorted[hole].index = hole  # visualise
                hole -= 1
            unsorted[hole].value = val
            unsorted[hole].index = hole  # visualise

    @staticmethod
    def bubble_sort(unsorted, n):
        """ bubble sort algorithm """
        for i in range(0, n - 1):
            swapped = False
            for j in range(0, n - 1 - i):
                if unsorted[j].value > unsorted[j + 1].value:
                    a = unsorted[j]
                    b = unsorted[j + 1]
                    unsorted[j] = b
                    unsorted[j + 1] = a
                    a.index = j + 1  # visualise
                    b.index = j  # visualise
                    swapped = True
            if not swapped:
                break

