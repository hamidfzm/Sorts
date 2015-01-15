__author__ = 'Hamid FzM'


def sort(arr):
    """ Gnome sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    pos = 0
    while True:
        if pos == 0:
            pos += 1
        if pos >= len(arr):
            break
        if arr[pos] >= arr[pos-1]:
            pos += 1
        else:
            arr[pos-1], arr[pos] = arr[pos], arr[pos-1]
            pos -= 1

    return arr