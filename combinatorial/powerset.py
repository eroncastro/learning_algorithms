def powerset(alist):
    if not any(alist):
        return [[]]

    new_set = []
    for elem in powerset(alist[1:]):
        new_set.append(elem)
        new_set.append([alist[0]] + elem)
    return new_set