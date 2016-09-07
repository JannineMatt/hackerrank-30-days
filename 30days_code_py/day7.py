'''
Task
Given an array, A, of N integers, print A's elements in reverse order as a
single line of space-separated numbers.
'''

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in arr[::-1]:
    print(i, " ", sep='', end='')
