def separate_letters_and_numbers(s):

    separated = ""
    numbers = "0123456789"
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for character in s:

        if character in alphabet:

            try:

                if separated[-1] in numbers:

                    separated += "-"

            except:

                separated += character
                is_except = True

            finally:

                if is_except == False:
                    separated += character

                is_except = False

        elif character in numbers:

            if separated[-1] in alphabet:

                separated += "-"

            separated += character

        else:

            separated += character

    return separated

if __name__ == "__main__":

    print(separate_letters_and_numbers("ABC123"))
    print(separate_letters_and_numbers("Route66"))
    print(separate_letters_and_numbers("H3LL0W0RLD"))
    print(separate_letters_and_numbers("a1b2c3d4"))