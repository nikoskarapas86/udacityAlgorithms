import random


def get_min_max(ints):
    if len(ints) == 0:
        return (0, 0)
    minNumber = ints[0]
    maxNumber = ints[0]

    for number in ints:
        if number > maxNumber:
            maxNumber = number
        if number < minNumber:
            minNumber = number
    return (minNumber, maxNumber)


l = [i for i in range(0, 10)]
random.shuffle(l)

print("test case 1")
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("test case 2")
l = [i for i in range(-23, -2)]
random.shuffle(l)
print("Pass" if ((-23, -3) == get_min_max(l)) else "Fail")

print("test case 3")
print("Pass" if ((0, 0) == get_min_max([])) else "Fail")

print("test case 4")
print("Pass" if ((-1, 100) == get_min_max([-1, 1, 2, 3, 4, 100])) else "Fail")
