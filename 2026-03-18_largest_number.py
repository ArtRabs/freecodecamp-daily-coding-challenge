def largest_number(s):

    i = 0
    j = 0

    array_num = []

    while i < len(s) - 1:

        # seperators
        if s[i] in ",!?:;":

            array_num.append(float(s[j:i]))

            j = i + 1

        i += 1

    # add the last number
    array_num.append(float(s[j:]))

    return max(array_num)

if __name__ == "__main__":

    print(largest_number("1,2"))
    print(largest_number("12;-50,99.9,49.1!-10.1?88?16"))