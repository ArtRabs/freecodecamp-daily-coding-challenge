def smallest_gap(s):

    # initiate minimum variables to check later
    min_gap = None
    min_i = None
    min_j = None

    i = 0
    j = 1

    # brute force
    # checks every possible pairs in the string
    while i < len(s) - 1:

        # if index for j is equals to len(s), then it is out of bounds
        # add 1 to i and reset the j next to i
        if j == len(s):

            i += 1
            j = i + 1

        # if characters not in pair, advance the index for j
        elif s[i] != s[j]:

            j += 1

        # if characters are pair, it checks the smallest gap
        elif s[i] == s[j]:

            # initiate new value
            if min_gap is None:

                min_gap = j - i + 1
                min_i = i
                min_j = j

            # if the new smallest gap is smaller the previous smallest gap
            if j - i + 1 < min_gap:

                min_gap = j - i + 1
                min_i = i
                min_j = j

            j += 1

    # return the smallest gap between the pair
    return s[min_i + 1:min_j]

if __name__ == "__main__":

    print(smallest_gap("ABCDAC"))