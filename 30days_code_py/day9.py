'''
Write a factorial function that takes a positive integer, as a parameter
and prints the result of ( factorial).

Note: If you fail to use recursion or fail to name your recursive function
factorial or Factorial, you will get a score of .
'''


def factorial(n):
    if n >= 2:
        return n * factorial(n - 1)
    return 1
N = int(input())
print(factorial(N))
