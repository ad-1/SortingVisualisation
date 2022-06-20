# Sorting Algorithms

Visualising various sorting algorithms using <b>Python</b> and <b>Tkinter</b>.
<br><br>
Algorithms include:
<ul>
<li>Selection Sort</li>
<li>Bubble Sort</li>
<li>Insertion Sort</li>
<li>Merge Sort</li>
<li>Quick Sort</li>
</ul>

This repository is linked to an article on Medium describing project.
Check it out <a href="">here</a>.

## Selection Sort

<b>Selection</b> sort manipulates elements in the array <i>"in-place"</i>. Due to the time complexity, efficiencies arise when working on large lists.
<br><br>
It has <i>similarities</i> to the insertion sort algorithm presented below.
Therefore, if comparing both, selection sort generally performs suboptimally versus insertion sort.

    Worst complexity: n^2
    Average complexity: n^2
    Best complexity: n^2
    Space complexity: 1
    Method: Selection
    Stable: No
    Class: Comparison sort

<img src="images/selection.gif" alt="selection sort" width="500"/>

## Bubble Sort

Bubble sort compares adjacent elements and swaps them if they are in the wrong order. The pass of the list repeats to obtain the final ordered values.<br><br>
Items are seen to <i>bubble</i> to the top of the array, thus giving the algorithm its name. Alternatively, they may <i>sink</i>, which is the other name for this algorithm, <i>sinking</i> sort.

    Worst complexity: n^2
    Average complexity: n^2
    Best complexity: n
    Space complexity: 1
    Method: Exchanging
    Stable: Yes
    Class: Comparison sort

<img src="images/bubble.gif" alt="bubble sort" width="500"/>

## Insertion Sort

<b>Insertion</b> sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. Wikipedia

    Worst complexity: n^2
    Average complexity: n^2
    Best complexity: n
    Space complexity: 1
    Method: Insertion
    Stable: Yes
    Class: Comparison sort

<img src="images/insertion.gif" alt="insertion sort" width="500"/> 

## Merge Sort

<b>Merge</b> sort is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, meaning that the order of equal elements is the same in the input and output.
Merge sort is a divide and conquer algorithm.

    Worst complexity: n*log(n)
    Average complexity: n*log(n)
    Best complexity: n*log(n)
    Space complexity: n
    Method: Merging
    Stable: Yes

<img src="images/merge-sort.gif" alt="merge sort" width="500"/>

## Quick Sort

<b>Quicksort</b> was developed by British computer scientist Tony Hoare in 1959.
It is still a commonly used algorithm for sorting. It has potential to be multiple times faster than its main competitors, merge sort and heapsort.

    Worst complexity: n^2
    Average complexity: n*log(n)
    Best complexity: n*log(n)
    Method: Partitioning
    Stable: No
    Class: Comparison sort
    
<img src="images/quick-sort.gif" alt="quick sort" width="500"/>

