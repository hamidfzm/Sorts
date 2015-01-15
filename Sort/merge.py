__author__ = 'Hamid FzM'


def sort(arr):
    """ Merge sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    if len(arr) > 1:

        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        sort(lefthalf)
        sort(righthalf)

        i = 0  # left counter
        j = 0  # right counter
        k = 0  # master counter
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    return arr