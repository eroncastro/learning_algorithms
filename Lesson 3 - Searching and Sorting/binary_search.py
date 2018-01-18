def binary_search(input_list, value):
    min_index = 0
    max_index = len(input_list)-1
    if not max_index:
        return -1

    while True:
        index = (min_index + max_index) // 2

        if input_list[index] == value:
            return index
        elif min_index == max_index:
            return -1

        if input_list[index] < value:
            min_index = index + 1
        else:
            max_index = index


def recursive_binary_search(alist, value, low_index=None, high_index=None):
    if low_index is None:
        low_index = 0

    if high_index is None:
        high_index = len(alist)-1

    m = (low_index + high_index) // 2

    if alist[m] == value:
        return m
    elif low_index == high_index:
        return -1

    if alist[m] < value:
        low_index = m + 1
    else:
        high_index = m

    return recursive_binary_search(alist, value, low_index, high_index)
