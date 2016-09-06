'''
Given an integer, , perform the following conditional actions:

    If is odd, print Weird
    If is even and in the inclusive range of 2 to 5, print Not Weird
    If is even and in the inclusive range of 6 to 20, print Weird
    If is even and greater than 20, print Not Weird

Complete the stub code provided in your editor to print whether or not is weird.
'''
# input N
N = int(input().strip())

# if odd
if N % 2 != 0:
    print('Weird')
elif 2 <= N <= 5:
    print('Not Weird')
elif 6 <= N <= 20:
    print('Weird')
else:
    print('Not Weird')
