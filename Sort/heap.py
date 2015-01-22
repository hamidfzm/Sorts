__author__ = 'Hamid FzM'


def sort(arr):
    """ Heap sort a list
    this function sorts in-place (it mutates the list)

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    # in pseudo-code, heapify only called once, so inline it here
    for start in range((len(arr)-2)/2, -1, -1):
        siftdown(arr, start, len(arr)-1)

    for end in range(len(arr)-1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        siftdown(arr, 0, end - 1)
    return arr


def siftdown(lst, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break