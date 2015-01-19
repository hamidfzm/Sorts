__author__ = 'Hamid FzM'


def sort(arr, loops_n=2):
    """ Odd Even sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    finished = False
    while not finished:
        finished = True
        for n in xrange(loops_n):
            for i in xrange(n, len(arr) - 1, loops_n):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    finished = False

    return arr