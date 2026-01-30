def is_sorted(arr):

    if arr == sorted(arr):

        return "Ascending"

    if arr == sorted(arr, reverse=True):

        return "Descending"
    
    else:

        return "Not sorted"
    
if __name__ == "__main__":

    print(is_sorted([1, 2, 3, 4, 5]))
    print(is_sorted([1, 3, 2, 4, 5]))
    print(is_sorted([10, 8, 6, 4, 2]))