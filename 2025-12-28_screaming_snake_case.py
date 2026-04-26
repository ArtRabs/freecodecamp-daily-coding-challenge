def to_screaming_snake_case(variable_name):

    screaming_snake_case = variable_name

    index = 0

    for letter in screaming_snake_case:

        if letter.isupper():

            if index != 0:

                screaming_snake_case = screaming_snake_case.replace(letter, "_" + letter.lower())

            else:

                screaming_snake_case = screaming_snake_case.replace(letter, letter.lower())

        index += 1

    return screaming_snake_case.replace("-", "_").upper()
