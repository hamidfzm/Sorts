__author__ = 'Hamid FzM'


def sort(arr):
    """ Bubble sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    for i in xrange(len(arr)-1, 0, -1):
        for j in xrange(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
