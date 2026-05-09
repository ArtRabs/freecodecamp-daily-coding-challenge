def transpose(matrix):

    transposed_matrix = []

    for col in zip(*matrix):

        transposed_matrix.append(list(col))

    return transposed_matrix

if __name__ == "__main__":

    print(transpose(
        [
            [1, 2, 3],
            [4, 5, 6]
        ]
        ))
    
    print(transpose(
        [
            [1, 2], 
            [3, 4], 
            [5, 6]
        ]
        ))