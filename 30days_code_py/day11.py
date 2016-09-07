def sum_square(square, col, row):
    ''' sum square number except someone, S mean skip
    111
    S1S
    111
    '''
    _total = 0
    for c in range(col - 1, col + 2):
        for r in range(row - 1, row + 2):
            if (r == (row - 1) or r == (row + 1)) and c == col:
                continue
            _total += square[c][r]
    return _total

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
# arr = [[1, 1, 1, 0, 0, 0],
#        [0, 1, 0, 0, 0, 0],
#        [1, 1, 1, 0, 0, 0],
#        [0, 0, 2, 4, 4, 0],
#        [0, 0, 0, 2, 0, 0],
#        [0, 0, 1, 2, 4, 0], ]
max_sum = sum_square(arr, 1, 1)
total = 0

for col in range(1, 5):
    for row in range(1, 5):
        # sum square
        total = sum_square(arr, col, row)
        if total > max_sum:
            max_sum = total
print(max_sum)
