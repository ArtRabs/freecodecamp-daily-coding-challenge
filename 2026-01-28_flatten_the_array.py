def flatten(arr):
    flat_arr = []
    
    for item in arr:
        if isinstance(item, list):
            flat_arr.extend(flatten(item))  # Recursively flatten nested lists
        else:
            flat_arr.append(item)  # Append non-list items directly
    
    return flat_arr

if __name__ == "__main__":

    print(flatten([1, 2, 3]))
    print(flatten([1, [2, 3], 4]))
    print(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]))
    print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))