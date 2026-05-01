def sort_and_swap(arr):

    sorted_arr = sorted(arr)

    continue_once = True

    # just use "while loop" if only going to use the "i" as index in this case
    for i, item in enumerate(sorted_arr):

        # skip to ignore the first equal to 0 index in modulus
        if continue_once:

            continue_once = False  
        
            continue

        # check if the index is divisible by 3
        if i % 3 == 0:

            sorted_arr[i], sorted_arr[i - 1] = sorted_arr[i - 1], sorted_arr[i]

    return sorted_arr

if __name__ == "__main__":

    print(sort_and_swap([3, 1, 2, 4, 6, 5]))