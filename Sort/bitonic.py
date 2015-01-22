__author__ = 'Hamid FzM'

import math
ASCENDING = True
DESCENDING = False

__all__ = ['sort']


def sort(arr):
    """ bitonic sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    # Length of list must be 2**x, where x is an integer.

    try:
        assert math.modf(math.log(len(arr), 2))[0] == 0
        return bitonicsort(arr, 0, len(arr), ASCENDING)
    except AssertionError:
        # Sorry I did something terrible here, I force list to be in 2**x mode and destroyed performance
        # I assumed the least min number is -99999
        fixer = [-99999] * (int(math.modf(math.log(len(arr), 2))[1]) + 1)
        return bitonicsort(arr + fixer, 0, len(arr), ASCENDING)[0:len(arr)]


def compare(arr, i, j, order):
    if order == (arr[i] > arr[j]):
        arr[i], arr[j] = arr[j], arr[i]


def merge(arr, lo, n, order):
    if n > 1:
        k = n/2
        for i in range(lo, lo+k):
            compare(arr, i, i+k, order)
        merge(arr, lo, k, order)
        merge(arr, lo+k, k, order)


def bitonicsort(arr, lo, n, order):
    if n > 1:
        k = n/2
        bitonicsort(arr, lo, k, ASCENDING)
        bitonicsort(arr, lo+k, k, DESCENDING)
        merge(arr, lo, n, order)
    return arr