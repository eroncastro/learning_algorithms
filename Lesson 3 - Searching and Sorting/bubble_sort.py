def bubble_sort(elements):
    elements_copy = elements[:]
    n = 1
    for i in range(len(elements_copy)-1):
        for j in range(len(elements_copy)-n):
            if elements_copy[j] > elements_copy[j+1]:
                elements_copy[j], elements_copy[j+1] = (
                    elements_copy[j+1], elements_copy[j])

        n += 1
    return elements_copy

