__author__ = 'Hamid FzM'


def sort(arr):
    """ Insertion sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for keyPos in xrange(1, len(arr)):

        # Get the value of the element to insert
        keyValue = arr[keyPos]

        # Scan from right to the left (start of list)
        scanPos = keyPos - 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scanPos >= 0) and (arr[scanPos] > keyValue):
            arr[scanPos + 1] = arr[scanPos]
            scanPos -= 1

        # Everything has been moved out of the way, insert
        # the key into the correct location
        arr[scanPos + 1] = keyValue
