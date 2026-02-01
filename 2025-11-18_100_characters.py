def one_hundred(chars):

    one00 = ""
    i = 0

    while len(one00) != 100:

        one00 += chars[i % len(chars)]
        i += 1

    return one00

if __name__ == "__main__":

    print(one_hundred("One hundred "))
    print(one_hundred("daily challenges "))