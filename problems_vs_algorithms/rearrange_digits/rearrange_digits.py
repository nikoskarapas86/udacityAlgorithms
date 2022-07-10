

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    firstNumber = 0
    secondNumber = 0

    # mergeSort will give us an array of inputs  sorted but we know that a max num has max digits first then second max digits etcheteral
    # so we need the list reversed
    sortedList = mergeSort(input_list)[::-1]
    # get numbers in even indeces
    for k in range(len(sortedList)):
        if k % 2 != 0:

            secondNumber = secondNumber * 10 + sortedList[k]
        else:

            firstNumber = firstNumber * 10 + sortedList[k]

    return [firstNumber, secondNumber]

# `O(nlog(n))` time complexity and `O(n)` space complexity


def mergeSort(list):
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    mergedList = []
    lIndex = 0
    rIndex = 0

    while lIndex < len(left) and rIndex < len(right):
        if left[lIndex] > right[rIndex]:
            mergedList.append(right[rIndex])
            rIndex += 1
        else:
            mergedList.append(left[lIndex])
            lIndex += 1
    mergedList += left[lIndex:]
    mergedList += right[rIndex:]

    return mergedList


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0]])
test_function([[1, 1, 1, 1], [11, 11]])
