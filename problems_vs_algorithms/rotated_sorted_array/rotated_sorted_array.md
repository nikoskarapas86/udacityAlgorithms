## You are given a sorted array which is rotated at some random pivot point.

## Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

## You are given a target value to search. If found in the array return its index, otherwise return -1.

## You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

## Example:

## Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

## well the requirement algorithm's runtime complexity must be in the order of O(log n).

## we slould use binary search

## to solve that problem we find the the lowerest value in the rotated array thats the pivot

## then we create two subArrays

## then we use binarySearch to find the target number in each subArray . time complexity for the solution is `O(log n)`

## As for space complexity rotated_array_search requires `(1)` space compexity

## find_pivot requires `(1)` space compexity

## binary_search requires `(n)` space compexity

## linear_search requires `(n)` space compexity
