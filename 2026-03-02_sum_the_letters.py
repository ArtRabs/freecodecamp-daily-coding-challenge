def sum_letters(s):

    s = s.upper()

    total = 0

    for char in s:

        if char.isalpha():

            total += ord(char) - ord("A") + 1

    return total

# ord("A") = 65
# ord("B") = 66
# ord("C") = 67
# ...
# ord("Z") = 90

# ord("a") = 97
# ord("b") = 98
# ord("c") = 99
# ...
# ord("z") = 122

# ord("A") - ord("A") = 0
# ord("B") - ord("A") = 1
# ord("C") - ord("A") = 2

# ord("A") - ord("A") + 1 = 1
# ord("B") - ord("A") + 1 = 2
# ord("C") - ord("A") + 1 = 3