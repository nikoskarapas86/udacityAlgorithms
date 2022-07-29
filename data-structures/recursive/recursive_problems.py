

import copy


# calculate 2^n recursively
def power_of_two(n):
    if n == 0:
        return 1
    return 2*power_of_two(n-1)


# sum of integers from 1 to n


def sum_digits(n):
    if n == 1:
        return 1
    return n + sum_digits(n-1)

  # sum array ,sum all digits of an array


def sum_array_digits(array):
    if len(array) == 1:
        return array[0]
    return array[0] + sum_array_digits(array[1:])

# factorial time complexity is O(n) and space complexity is O(n)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)


def reverse_string(str):
    if len(str) == 0:
        return ''
    return reverse_string(str[1:]) + str[0]

# palindrom checker


def palindrome_checker(strl):
    if len(strl) == 1:
        return True
    return strl[0] == strl[len(strl)-1] and palindrome_checker(strl[1:-1])


print(palindrome_checker("madam"))
# add one at last list element


def add_one(arr):
    if arr == [9]:
        return [0, 1]
    if arr[-1] < 9:
        arr[-1] += 1
    else:
        arr = add_one(arr[:-1]) + [0]
        return arr


# premutations of a list


def permute(inputList):
    finalCompoundList = []
    if len(inputList) == 0:
        finalCompoundList.append([])
    else:
        first_element = inputList[0]
        rest_list = inputList[1:]
        sub_compoundList = permute(rest_list)

        for aList in sub_compoundList:
            for j in range(0, len(aList) + 1):
                bList = copy.deepcopy(aList)
                bList.insert(j, first_element)
                finalCompoundList.append(bList)

    return finalCompoundList


def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


print("Pass" if (check_output(permute([]), [[]])) else "Fail")
print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1, 2]), [[0, 1, 2], [
      0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")
