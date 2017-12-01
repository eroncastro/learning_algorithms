def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def sort(elements_list):
    if len(elements_list) == 1:
        return elements_list[:]

    left = sort(elements_list[:len(elements_list) // 2])
    right = sort(elements_list[len(elements_list) // 2:])
    return merge(left, right)
