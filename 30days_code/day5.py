'''
Given an integer, N, print its first 10 multiples. Each multiple N * i
(where 1 <= i <= 10)should be printed on a new line in the form: N x i = result
'''
N = int(input().strip())

result = None
for i in range(1, 10 + 1):
    result = N * i
    print('{0} x {1} = {2}'.format(N, i, result))
