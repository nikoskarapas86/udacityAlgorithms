# BubbleSort
def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]
            if prev <= this:
                continue
            l[index] = prev
            l[index - 1] = this


# MergeSort
def mergesort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
    return merged

# quickSort


def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)


def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]
    while (pivot_index != left_index):
        item = items[left_index]
        if item <= pivot_value:
            left_index += 1
            continue
        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1
    return pivot_index


def quicksort(items):
    sort_all(items, 0, len(items) - 1)
