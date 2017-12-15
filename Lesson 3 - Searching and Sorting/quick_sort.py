def partition(alist, first, last):
    pivot_pos = last
    cur_pos = first

    while pivot_pos != cur_pos:
        cur, pivot = alist[cur_pos], alist[pivot_pos]
        if cur > pivot:
            alist[cur_pos] = alist[pivot_pos-1]
            alist[pivot_pos-1], alist[pivot_pos] = pivot, cur
            pivot_pos -= 1
        else:
            cur_pos += 1
    return cur_pos


def quick_sort(alist, first, last):
    if first >= last:
        return

    position = partition(alist, first, last)

    quick_sort(alist, 0, position-1)
    quick_sort(alist, position+1, last)
