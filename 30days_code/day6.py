'''
Given a string, S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as 2 space-separated
strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.
'''


def seperate_print(S):
    N = len(S)
    odd_char = ''
    even_char = ''
    for index in range(N):
        if index % 2 == 0:
            even_char += S[index]
        else:
            odd_char += S[index]
    print('{0} {1}'.format(even_char, odd_char))

# how many word
times = int(input())
for _ in range(times):
    S = input()
    seperate_print(S)
