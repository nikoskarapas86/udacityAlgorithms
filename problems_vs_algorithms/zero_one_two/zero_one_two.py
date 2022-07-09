def change_position(arr, firstIndex, secondIndex):
    temp = arr[firstIndex]
    arr[firstIndex] = arr[secondIndex]
    arr[secondIndex] = temp


def sort_012(list012):
    if len(list012) == 0:
        return []
    zeroIndex = 0
    twoIndex = len(list012) - 1
    i = 0
    while i <= twoIndex:
        if list012[i] == 0:
            change_position(list012, i, zeroIndex)
            zeroIndex += 1
            i += 1
        elif list012[i] == 2:
            change_position(list012, i, twoIndex)
            twoIndex -= 1
        else:
            i += 1

    return list012


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
              2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
