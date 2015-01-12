__author__ = 'Hamid FzM'


def sort(arr):
    """ Shell sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    gap = len(arr) / 2
    while gap:
        for keyPos in xrange(gap, len(arr)):
            keyValue = arr[keyPos]

            scanPos = keyPos - gap

            while (scanPos >= 0) and (arr[scanPos] > keyValue):
                arr[scanPos + gap] = arr[scanPos]
                scanPos -= gap
            arr[scanPos + gap] = keyValue
        gap = gap/2 if gap/2 else (0 if gap == 1 else 1)

    return arr

print sort([151, 901, 58, 389, 733, 553, 366, 757, 511, 176, 564, 996, 189, 312, 326, 267, 494, 45, 530, 889])