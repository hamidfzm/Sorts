__author__ = 'Hamid FzM'


def sort(arr):
    """ Comb sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    gap = len(arr)
    while 1:
        gap = int(gap / 1.25)
        swaps = False
        for i in xrange(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swaps = True
        if not swaps and gap <= 1:
            break
    return arr