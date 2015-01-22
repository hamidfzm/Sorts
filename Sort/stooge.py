__author__ = 'Hamid FzM'


def sort(arr, i=0, j=None):
    """ Stooge sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if j is None:
        j = len(arr) - 1
    if arr[j] < arr[i]:
        arr[i], arr[j] = arr[j], arr[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        sort(arr, i, j - t)
        sort(arr, i + t, j)
        sort(arr, i, j - t)
    return arr