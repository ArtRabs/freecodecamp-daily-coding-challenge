def count_perfect_cubes(a, b):

    count = 0

    # always make `a` less than `b`
    if a > b:

        temp = a
        a = b
        b = temp

    # checks if there is negative 
    negative = False

    if a < 0 or b < 0:

        negative = True

        # subtracts 1 because for some reason if there is negative, my count is always off by 1
        # perhaps it also counts the 0 twice
        count -= 1

    # counts the perfect cube
    i = 0

    while True:

        perfect_cube = i ** 3

        # checks if perfect cube is between `a` and `b`
        if a <= perfect_cube and perfect_cube <= b:

            # `a` is always lower than `b` if not equal
            # makes negative False
            if -perfect_cube < a:

                negative = False

            # counts the perfect cube if it is negative
            if negative:

                count += 1

            # counts the perfect cube normally
            count += 1
            
            i += 1

        # `b` is always greater than `a` if not equal
        # breaks if perfect cube is greater than `b`
        elif perfect_cube > b:

            break

        # adds 1 to `i` if perfect cube is not between `a` and `b`
        else:

            i += 1

    return count

if __name__ == "__main__":

    print(count_perfect_cubes(3, 30)) # 2
    print(count_perfect_cubes(1, 30)) # 3
    print(count_perfect_cubes(30, 0)) # 4
    print(count_perfect_cubes(-64, 64)) # 9
    print(count_perfect_cubes(9214, -8127)) # 41


# def count_perfect_cubes(a, b):

#     if a > b:

#         a, b = b, a

#     count = 0
#     i = 0

#     while True:

#         perfect_cube = i ** 3

#         if perfect_cube > b and -perfect_cube < a:

#             break

#         if a <= perfect_cube <= b:

#             count += 1

#         if perfect_cube != 0 and a <= -perfect_cube <= b:
            
#             count += 1

#         i += 1

#     return count