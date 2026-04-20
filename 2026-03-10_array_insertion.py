def insert_into_array(arr, value, index):

    arr.insert(index, value)

    return arr

if __name__ == "__main__":

    print(insert_into_array([1, 2, 3, 4], 5, 2))
    print(insert_into_array(["a", "b", "c"], "d", 0))