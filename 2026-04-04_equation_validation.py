def is_valid_equation(equation):

    i = -1

    while True:
        
        if equation[i] == "=":

            left_side = equation[:i]
            right_side = equation[i + 1:]

            if eval(left_side) == int(right_side):

                return True

            break

        i -= 1

    return False

if __name__ == "__main__":

    print(is_valid_equation("2 + 9 / 3 = 5"))


# def is_valid_equation(equation):

#     i = -1

#     while True:
        
#         if equation[i] == "=":

#             left_side = equation[:i]
#             right_side = equation[i + 1:]

#             print(left_side.strip())
#             print(right_side.strip())

#             left_side = left_side.strip()
#             right_side = right_side.strip()

#             print(left_side)
#             print(right_side)

#             solve = 2 + 9 / 3
#             print(solve)            
#             print(solve == int(right_side))
#             print(int(left_side) == int(right_side))

#             break

#         i -= 1

#     return False
