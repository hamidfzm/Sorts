__author__ = 'Hamid FzM'


def sort(arr):
    """ Quick sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []

    less = list()
    more = list()
    equal = list()

    # first element is considers ad pivot
    for x in arr:
        if x < arr[0]:
            less.append(x)
        elif x > arr[0]:
            more.append(x)
        elif x == arr[0]:
            equal.append(x)

    return sort(less) + equal + sort(more)