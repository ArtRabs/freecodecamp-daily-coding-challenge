def is_in_crossword(char):

    if char == "0":

        return True

    convert = format(ord(char), "08b")
    binary = list(map(int, convert))

    print(binary)

    matrix = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0]
    ]

    # check all rows
    for row in matrix:
        

        
        if row == binary:            

            return True

    # check all columns
    num_cols = len(matrix[0])

    for j in range(num_cols):

        col = [matrix[i][j] for i in range(len(matrix))]

        if col == binary:

            return True

    return False

if __name__ == "__main__":

    print(is_in_crossword("A"))
    print(is_in_crossword("B"))
    print(is_in_crossword("C"))