def is_flat(arr):

    for num in arr:

        if isinstance(num, list):

            return False

    return True