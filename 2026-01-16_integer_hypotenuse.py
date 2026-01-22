def is_integer_hypotenuse(a, b):

    c = a**2 + b**2

    c_root = int(c ** 0.5)

    print(c_root * c_root)

    is_perfect_square = c == c_root * c_root

    return is_perfect_square

if __name__ == "__main__":
    print(is_integer_hypotenuse(3,4))
    print(is_integer_hypotenuse(2,3))
    print(is_integer_hypotenuse(250,333))

