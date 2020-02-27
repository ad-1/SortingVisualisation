# Sorting Algorithms Solver Class


class Solver:

    def __init__(self, unsorted, n, solve_mode, subscriber):
        self.subscriber = subscriber
        self.counter = 0
        if solve_mode == 0:
            self.selection_sort(unsorted, n)
        elif solve_mode == 1:
            self.insertion_sort(unsorted, n)
        elif solve_mode == 2:
            self.bubble_sort(unsorted, n)
        elif solve_mode == 3:
            self.divide(unsorted, 0, n - 1)  # merge sort
        elif solve_mode == 4:
            start, end = 0, len(unsorted)
            self.quick_sort(unsorted, start, end)

    ########################################################################

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

    ########################################################################

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

    ########################################################################

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

    ########################################################################

    def divide(self, unsorted, lower, upper):
        """ recrusive function to divide array into 2 sub arrays for sorting """
        self.counter += 1
        if upper <= lower:
            return
        mid = (lower + upper) // 2
        self.divide(unsorted, lower, mid)
        self.divide(unsorted, mid + 1, upper)
        self.merge(unsorted, lower, mid, mid + 1, upper)

    @staticmethod
    def merge(unsorted, l_lower, l_upper, r_lower, r_upper):
        """ merging two sorted arrays to one sorted array """
        i, j = l_lower, r_lower
        temp = []
        while i <= l_upper and j <= r_upper:
            if unsorted[i].value <= unsorted[j].value:
                temp.append(unsorted[i])
                i += 1
            else:
                temp.append(unsorted[j])
                j += 1
        while i <= l_upper:
            temp.append(unsorted[i])
            i += 1
        while j <= r_upper:
            temp.append(unsorted[j])
            j += 1
        y = 0
        for k in range(l_lower, r_upper + 1):
            unsorted[k] = temp[y]
            unsorted[k].index = k
            y += 1

    ########################################################################

    def quick_sort(self, unsorted, start, end):
        """ quick sort recursive algorithm """
        if start >= end:
            return
        n = len(unsorted)
        self.counter += 1
        i_pivot = self.partition(unsorted, start, end - 1)
        self.quick_sort(unsorted, start, i_pivot)
        self.quick_sort(unsorted, i_pivot + 1, n)

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

