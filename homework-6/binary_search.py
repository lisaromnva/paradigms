def find_number(arr, num):
    first_i = 0
    last_i = len(arr) - 1

    while first_i <= last_i:
        middle_i = (first_i + last_i) // 2

        if num == arr[middle_i]:
            return middle_i

        if num < arr[middle_i]:
            last_i = middle_i - 1
        else:
            first_i = middle_i + 1

    return -1


print(find_number([0, 1, 1, 2, 3, 4, 5, 8], 2))