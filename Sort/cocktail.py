__author__ = 'Hamid FzM'


def sort(arr):
    """ Cocktail sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    begin, end = 0, len(arr) - 1
    finished = False
    while not finished:
        finished = True
        for i in xrange(begin, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                finished = False
        if finished:
            break
        finished = True
        end -= 1
        for i in reversed(xrange(begin, end)):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                finished = False
        begin += 1

    return arr