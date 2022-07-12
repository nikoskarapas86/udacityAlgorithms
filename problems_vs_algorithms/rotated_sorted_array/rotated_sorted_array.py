def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    if len(input_list) == 1:
        if input_list[0] == number:
            return 0
        else:
            return -1

    start = 0
    end = len(input_list) - 1
    finding = 0
    if input_list[start] < input_list[end]:
        finding = binary_search(start, end, input_list, number)
    else:
        pivot = find_pivot(start, end, input_list)
        if number >= input_list[pivot] and number <= input_list[end]:
            finding = binary_search(pivot, end, input_list, number)
        else:
            finding = binary_search(start, pivot-1, input_list, number)
    return finding

# time complexity O(n) space complexity O(1)


def find_pivot(start, end, inputList):
    mid = start + (end - start) // 2
    pivot = 0
    if inputList[mid] > inputList[mid + 1]:
        return mid + 1
    else:
        if inputList[start] > inputList[mid]:
            pivot = find_pivot(start, mid-1, inputList)
        else:
            pivot = find_pivot(mid+1, end, inputList)
    return pivot

# time complexity O(nlogn) space complexity O(1)


def binary_search(start, end, inputList, target):

    while start <= end:
        middle = (start+end)//2
        if inputList[middle] == target:
            return middle
        else:
            if inputList[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
    return -1

# time complexity O(n) space complexity O(1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# edge cases
test_function([[2], 2])
test_function([[], -1])
test_function([[1, 2, 3, 4, 5], -1])
