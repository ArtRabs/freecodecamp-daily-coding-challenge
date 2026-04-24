def get_unique_climbs(steps):

    a = 0
    b = 1

    for _ in range(steps):

        a, b = b , a + b

    return b

if __name__ == "__main__":

    print(get_unique_climbs(4))
    print(get_unique_climbs(10))
    print(get_unique_climbs(18))
    print(get_unique_climbs(50))

# def get_unique_climbs(steps):

#     if steps == 0 or steps == 1:

#         return 1

#     return get_unique_climbs(steps - 1) + get_unique_climbs(steps - 2)