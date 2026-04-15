def get_last_letter(s):

    # used as a reference later to ignore case sensitivity
    lower_s = s.lower()

    # original string
    letters = []
    # lower string
    lower_letters = []

    i = 0

    # append both original string and lower string
    while len(s) > i + 1:

        if s[i].isalpha():

            letters.append(s[i])

        if lower_s[i].isalpha():

            lower_letters.append(lower_s[i])

        i += 1

    # check the highest letter (A or a being lowest and Z or z being highest) in the lower string 
    max_letter = max(lower_letters)
    index_max_letter = lower_letters.index(max_letter)

    # return the original letter of string by using the index
    return letters[index_max_letter]

if __name__ == "__main__":

    print(get_last_letter("Hello there"))
    print(get_last_letter("WATERwater"))
    print(get_last_letter("waterWATER"))
    print(get_last_letter("216378216!@#$%^&*()w%^&*(-94059mmm)?>?>}HJKUUUZasdsadgrrgrgrgrg222z22x222"))