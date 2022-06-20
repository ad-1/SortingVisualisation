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
        elif solve_mode == 3:
            self.divide(unsorted, 0, n - 1)  # merge sort
        elif solve_mode == 4:
            self.quick_sort(unsorted, 0, n)

    ########################################################################

    def selection_sort(self, unsorted, n):
        """ selection sort algorithm inplace """
        for i in range(0, n):
            # current_min = min(unsorted[i:], key=lambda x: x.value)
            # a_index = unsorted.index(a)
            current_min = unsorted[i]
            min_index = i
            for j in range(i, n):
                if unsorted[j] < current_min:
                    current_min = unsorted[j]
                    min_index = j
            self.swap(unsorted, i, min_index)

    ########################################################################

    @staticmethod
    def insertion_sort(unsorted, n):
        """ insertion sort algorithm """
        for i in range(1, n):
            val = unsorted[i].value
            hole = i
            while hole > 0 and unsorted[hole - 1].value > val:
                unsorted[hole].value = unsorted[hole - 1].value
                unsorted[hole].index = hole  # set index to trigger dispatch
                hole -= 1
            unsorted[hole].value = val
            unsorted[hole].index = hole  # set index to trigger dispatch

    ########################################################################

    def bubble_sort(self, unsorted, n):
        """ bubble sort algorithm """
        for i in range(0, n - 1):
            swapped = False
            for j in range(0, n - 1 - i):
                if unsorted[j].value > unsorted[j + 1].value:
                    self.swap(unsorted, j, j + 1)
                    swapped = True
            if not swapped:
                break

    # ==============================================================
    # Merge Sort Algorithm

    def divide(self, unsorted, lower, upper):
        """ recrusive function to divide array into 2 sub arrays for sorting """
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

        for y, k in enumerate(range(l_lower, r_upper + 1)):
            unsorted[k] = temp[y]
            unsorted[k].index = k  # set index to trigger dispatch

    # ==============================================================
    # Quick Sort Algorithm

    def quick_sort(self, unsorted, start, end):
        """ quick sort recursive algorithm """
        if start >= end:
            return
        i_pivot = self.partition(unsorted, start, end - 1)
        self.quick_sort(unsorted, start, i_pivot)
        self.quick_sort(unsorted, i_pivot + 1, end)

    def partition(self, unsorted, start, end):
        """ arrange (left array < pivot) and (right array > pivot) """
        pivot = unsorted[end]
        i_pivot = start
        for i in range(start, end):
            if unsorted[i].value <= pivot.value:
                self.swap(unsorted, i, i_pivot)
                i_pivot += 1
        self.swap(unsorted, i_pivot, end)
        return i_pivot

    ########################################################################

    @staticmethod
    def swap(arr, a, b):
        """ helper function to swap elements a and b in an array """
        arr[a].index = b  # set index to trigger dispatch
        arr[b].index = a  # set index to trigger dispatch
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
