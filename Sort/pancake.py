__author__ = 'Hamid FzM'


def sort(arr):
    """ Pancake sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """

    if len(arr) <= 1:
        return arr
    for size in range(len(arr), 1, -1):
        maxindex = max(range(size), key=arr.__getitem__)
        if maxindex+1 != size:
            # This indexed max needs moving
            if maxindex != 0:
                # Flip the max item to the left

                arr[:maxindex+1] = reversed(arr[:maxindex+1])
            # Flip it into its final position
            arr[:size] = reversed(arr[:size])
    return arr