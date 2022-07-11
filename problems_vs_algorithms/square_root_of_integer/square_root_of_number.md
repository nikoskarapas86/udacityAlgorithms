## Better Approach: The idea is to find the largest integer i whose square is less than or equal to the given number. The idea is to use Binary Search to solve the problem. The values of i \* i is monotonically increasing, so the problem can be solved using binary search.

## Algorithm:

## Take care of some base cases, i.e when the given number is 0 or 1.

## Create some variables, lowerbound l = 0, upperbound r = n, where n is the given number, mid and ans to store the answer.

## Run a loop until l <= r , the search space vanishes

## Check if the square of mid (mid = (l + r)/2 ) is less than or equal to n, If yes then search for a larger value in second half of search space, i.e l = mid + 1, update ans = mid

## Else if the square of mid is more than n then search for a smaller value in first half of search space, i.e r = mid – 1

## Print the value of answer ( ans)

## Complexity Analysis:

## Time complexity: O(log n).

## The time complexity of the binary search is O(log n).

## Space Complexity: O(1).

## Constant extra space is needed.
