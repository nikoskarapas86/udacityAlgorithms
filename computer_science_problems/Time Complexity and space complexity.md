# Time Complexity and space complexity

## Task0:

The function getFirtAndLastRecord of the first task will take constant time complexity `O(1)` as the access time for list items also variable assignation will take constant time.
as for the space complexity will take space complexity is also `O(1)`

## Task1:

The function findDifferentPhones will take linear time complexity `O(n)`
all iterations take `O(n)` time complexity
access item in list takes `O(n)` time complexity
replace('(','') takes `O(n)` time complexity
time complexity is O(n+ 1 + 1+1 +1+1 +1 +1 +1+n+ 1 + 1+1 +1+1 +1 +1 +1) ~~~~> O(2n) => O(n), Also space complexity is O(n) because for each item in list we create variables and new variables needs more space in memory .

## Task2:

The function findLongestCall will take linear time complexity `O(n +n +1+1)`=> `O(n)`
all iterations take `O(n)` time complexity
while space complexity is O(1)

## Task3:

PartA:
time complexity `O(n+n +1+1+nlogn)`--> `O(n+n +nlogn)`--> `O(2n +nlogn)` --> `O(nlogn) ` while space complexity is Also O(n)
`O(n)` for lists
`O(1)` for variable assignations , if statements append methods find methods and replace methods and for set

PartB:
time complexity `O(n+1)`--> `O(n)` while space complexity is Also `O(n)`

`O(n)`: for iteration in list
`O(1)`: for math calculation

## Task4:

time complexity `OO(n+n+n+n+n+1+1+nlogn)`--> `O(5n+nlogn)`--> `O(n + nlogn)` --> `O(nlogn) ` while space complexity is Also O(n)
`O(n)`: the four list iteration `O(4n)` --> `O(n)`
`O(nlogn)`: sorted(telemarketers) takes `O(nlogn)`
`O(n)`: for loop for print
