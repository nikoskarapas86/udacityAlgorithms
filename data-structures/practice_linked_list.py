# given an array of numbers , a number will be presented 2 times . find that number
def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    mapper = {}
    for item in arr:
        if item in mapper:
            mapper[item] += 1
        else:
            mapper[item] = 1

    if mapper[item] == 2:
        return item
    else:
        return -1


# arr = [0, 2, 3, 1, 4, 5, 3]
# solution = 3


# Example 1:

# arr= [1, 2, 3, -4, 6]
# The largest sum is 8, which is the sum of all elements of the array.
# Example 2:

# arr = [1, 2, -5, -4, 1, 6]
# The largest sum is 7, which is the sum of the last two elements of the array.
#
def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    currect_sum = arr[0]
    max_sum = arr[0]

    for num in arr[1:]:
        currect_sum = max(currect_sum+num, num)
        max_sum = max(currect_sum, max_sum)
    return max_sum

    '''
    def max_sum_subarray(arr):

    current_sum = arr[0] # `current_sum` denotes the sum of a subarray
    # `max_sum` denotes the maximum value of `current_sum` ever
    max_sum = arr[0]

    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:
        current_sum = max(current_sum + element, element)

        # Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
        max_sum = max(current_sum, max_sum)

    return max_sum

     '''

#   Problem Statement
# Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.
# For example, if n = 4, then output = [1, 4, 6, 4, 1].


def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    for num in range(n):
        print(' '*(n-(num)), end='')

        print(' '.join(map(str, str(11**(num)))))

    def test_function(test_case):
        n = test_case[0]
        solution = test_case[1]
        output = nth_row_pascal(n)
        if solution == output:
            print("Pass")
        else:
            print("Fail")

    n = 3
    solution = [1, 3, 3, 1]

    test_case = [n, solution]
    test_function(test_case)
