# time complexity O(nlog n) space complexity O(n)
def sqrt(number):
    if number < 0:
        return None
    if number in [0, 1]:
        return number

    start = 1
    end = number
    while (start <= end):
        mid = (start + end) // 2
        if (mid*mid == number):
            return mid
        if (mid * mid < number):
            start = mid + 1
            ans = mid

        else:
            end = mid-1

    return ans


print("Pass" if (1 == sqrt(1)) else "Fail")

print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
# edge cases
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (None == sqrt(-5)) else "Fail")
print("Pass" if (None == sqrt(-22)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
