def array_swap(arr):

    swap = []

    swap.append(arr[1])
    swap.append(arr[0])

    return swap

print(array_swap([1, 2]))
print(array_swap([True, False]))
print(array_swap(["one", "two"]))
print(array_swap([3, "yon"]))