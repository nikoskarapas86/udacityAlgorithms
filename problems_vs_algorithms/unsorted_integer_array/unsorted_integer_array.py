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
print("Pass" if ((0, 0) == get_min_max([])) else "Fail")
