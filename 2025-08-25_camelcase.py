def to_camel_case(s):

    case = ""
    camel = False
    first_character = True

    for letter in s:

        if first_character:

            case += letter.lower()

            first_character = False

        elif letter == " " or letter == "-" or letter == "_":

            case += ""

            camel = True

        elif camel:

            case += letter.upper()

            camel = False

        elif letter == letter.upper():

            case += letter.lower()

            camel = False

        else:

            case += letter

            camel = False        

    return case

if __name__ == "__main__":

    print(to_camel_case("hello -there"))