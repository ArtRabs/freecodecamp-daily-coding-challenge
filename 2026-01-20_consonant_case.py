def to_consonant_case(s):

    word = ""

    for case in s:

        if case in "-":

            word += "_"

        elif case not in "aeiouAEIOU":

            word += case.upper()

        elif case in "aeiouAEIOU":

            word += case.lower()

    return word

if __name__ == "__main__":
    print(to_consonant_case("helloworld"))
    print(to_consonant_case("HELLOWORLD"))
    print(to_consonant_case("_hElLO-WOrlD-"))
    print(to_consonant_case("_~-generic_~-variable_~-name_~-here-~_"))