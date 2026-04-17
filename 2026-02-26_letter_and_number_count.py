def count_letters_and_numbers(s):

    letters = 0
    numbers = 0

    # count the number of letters and numbers
    for char in s:

        if char.isalpha():

            letters += 1

        if char.isdigit():

            numbers += 1

    # checks if letter is singular or plural
    if letters == 1:

        print_letters = "letter"

    else:

        print_letters = "letters"

    # checks if letter is singular or plural
    if numbers == 1:

        print_number = "number"

    else:

        print_number = "numbers"

    return f"The string has {letters} {print_letters} and {numbers} {print_number}."