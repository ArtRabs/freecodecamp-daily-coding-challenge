def get_bingo_letter(n):

    if n >= 1 and n <= 15:

        return "B"

    elif n >= 16 and n <= 30:

        return "I"

    elif n >= 31 and n <= 45:

        return "N"

    elif n >= 46 and n <= 60:

        return "G"

    elif n >= 61 and n <= 75:

        return "O"
    
if __name__ == "__main__":

    print(get_bingo_letter(15))
    print(get_bingo_letter(30))
    print(get_bingo_letter(57))
    print(get_bingo_letter(45))
    print(get_bingo_letter(62))