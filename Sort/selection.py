__author__ = 'Hamid FzM'


def sort(arr):
    """ Selection sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    for keyPos in xrange(len(arr)-1, 0, -1):
        max_pos = 0

        for location in xrange(1, keyPos+1):
            if arr[location] > arr[max_pos]:
                max_pos = location

        arr[keyPos], arr[max_pos] = arr[max_pos], arr[keyPos]

    return arr