def min_max_sum(arr):
    smallest_num = arr[0]
    largest_num = arr[0]

    for num in arr:
        if num < smallest_num:
            smallest_num = num
        if num > largest_num:
            largest_num = num

    # copy needs to be used here, or else changes on these arrays will change the original too
    smallest_arr = arr.copy()
    largest_arr = arr.copy()

    smallest_arr.remove(largest_num)
    largest_arr.remove(smallest_num)

    min_sum = 0
    max_sum = 0

    for num in smallest_arr:
        min_sum += num

    for num in largest_arr:
        max_sum += num

    print(f"{min_sum} {max_sum}")


min_max_sum([1, 2, 3, 4, 5])