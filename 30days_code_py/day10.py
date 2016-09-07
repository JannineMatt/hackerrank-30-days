'''
Given a base-10 integer, note, convert it to binary (base-2). Then find and print
the base-10 integer denoting the maximum number of consecutive 1's in n's binary
representation.
'''


def decimaltobinary(n):
    ''' convert decimal number to binary , return str  1010101'''
    if n > 1:
        return decimaltobinary(n // 2) + str(n % 2)
    return str(n % 2)

N = int(input())
bin_number = decimaltobinary(N)
# check convet is fine
# print(bin(N))
# print(bin_number)

# count max 1 continue time, 11 = 2, 101 = 1
count = 0
max_count = 0
for c in bin_number:
    if c == '1':
        count += 1

    else:
        if count > max_count:
            max_count = count
        count = 0
# final loop doesn't check max_count, check
if count > max_count:
    max_count = count
print(max_count)
