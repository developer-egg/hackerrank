array = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonal_difference(arr):
    arr_len = len(arr)

    lr_sum = 0
    rl_sum = 0

    for i in range(arr_len):
        lr_sum += arr[i][i]
        rl_sum += arr[i][(arr_len - 1) - i]

    return(abs(lr_sum - rl_sum))

print(diagonal_difference(array))
