def palindrome_locator(s):

    s = s.lower()

    i = 0
    j = -1

    word_len = len(s)

    # checks even
    if word_len % 2 == 0:

        # check both start and end of the word
        while True:

            # if not equal, return None
            if s[i] != s[j]:

                return "none"
            
            # condition to break the loop
            if i + abs(j) + 1 == word_len:

                break

            i = i + 1
            j = j - 1

        return s[i] + s[j]

    # checks odd
    else:

        # check both start and end of the word
        while 1 + 1 == 2:

            # if not equal, return None
            if s[i] != s[j]:

                return "none"

            # condition to break the loop
            if i + abs(j) == word_len:

                break
            
            i = i + 1
            j = j - 1

        return s[i]


if __name__ == "__main__":

    print(palindrome_locator("saippuakivikauppias")) # expected return "v"
    print(palindrome_locator("Tattarrattat")) # expected return "rr"
    print(palindrome_locator("REDDERER")) # expected return None
    print(palindrome_locator("Mukai"))
    print(palindrome_locator("freecodecamp"))