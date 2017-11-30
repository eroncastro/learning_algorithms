def binary_search(input_list, value):
    min_index = 0
    max_index = len(input_list)
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
