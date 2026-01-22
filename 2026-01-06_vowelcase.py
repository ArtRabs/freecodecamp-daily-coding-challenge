def vowel_case(s):

    vowel = "aeiouAEIOU"
    word = ""

    for letter in s:

        if letter in vowel:

            word += letter.upper()

        elif letter not in vowel:

            word += letter.lower()

        else:

            word += letter

    return word

if __name__ == "__main__":
    print(vowel_case("HELLO, world!"))