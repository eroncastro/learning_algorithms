def quick_sort(elements_list):
    sorting_list = elements_list[:]
    pivot = len(elements_list) - 1
    wall, current = 0, 0

    while wall < pivot:
        if sorting_list[current] <= sorting_list[pivot]:
            sorting_list[wall], sorting_list[current] = (
                sorting_list[current], sorting_list[wall])
            wall += 1
        current = current + 1 if current < pivot else 0
    return sorting_list

