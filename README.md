Sorts
=====
Visualization and comparison of sort algorithms for data structures project



Table of contents:

[TOC]

#Sorting algorithm
From Wikipedia, the free encyclopedia

A sorting algorithm is an algorithm that puts elements of a list in a certain order. The most-used orders are numerical order and lexicographical order. Efficient sorting is important for optimizing the use of other algorithms (such as search and merge algorithms) which require input data to be in sorted lists; it is also often useful for canonicalizing data and for producing human-readable output. More formally, the output must satisfy two conditions:

The output is in nondecreasing order (each element is no smaller than the previous element according to the desired total order);
The output is a permutation (reordering) of the input.
Further, the data is often taken to be in an array, which allows random access, rather than a list, which only allows sequential access, though often algorithms can be applied with suitable modification to either type of data.

Since the dawn of computing, the sorting problem has attracted a great deal of research, perhaps due to the complexity of solving it efficiently despite its simple, familiar statement. For example, bubble sort was analyzed as early as 1956. A fundamental limit of comparison sorting algorithms is that they require linearithmic time – O(n log n) – in the worst case, though better performance is possible on real-world data (such as almost-sorted data), and algorithms not based on comparison, such as counting sort, can have better performance. Although many consider sorting a solved problem – asymptotically optimal algorithms have been known since the mid-20th century – useful new algorithms are still being invented, with the now widely used Timsort dating to 2002, and the library sort being first published in 2006.

Sorting algorithms are prevalent in introductory computer science classes, where the abundance of algorithms for the problem provides a gentle introduction to a variety of core algorithm concepts, such as big O notation, divide and conquer algorithms, data structures such as heaps and binary trees, randomized algorithms, best, worst and average case analysis, time-space trade offs, and upper and lower bounds.

#Comparison of algorithms

--------------------------------------------------------------------------------------
| Name | Best | Average | Worst | Memory | Stable | Method | Other notes |
|--------|-------|-----------|--------|------------|---------|----------|----------------|
|Insertion Sort|$$n$$|$$n^2$$|$$n^2$$|$$1$$|Yes|Insertion|O(n + d), in the worst case over sequences that have d inversions.
|Shell Sort
|Quicksort|$$n log n$$|$$n log n$$|$$n^2$$| $$logn$$on average, worst case is $$n$$: Sedgewick variation is $$logn$$ worst case| typical in-place sort is not stable; stable versions exist |Partitioning|Quicksort is usually done in place with $$O(log n)$$ stack space.Most implementations are unstable, as stable in-place partitioning is more complex. Naïve variants use an $$O(n)$$ space array to store the partition. Quicksort variant using three-way (fat) partitioning takes $$O(n)$$ comparisons when sorting an array of equal keys.|