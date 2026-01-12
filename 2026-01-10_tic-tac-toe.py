def tic_tac_toe(board):

    # row

    for rows in board:

        if rows == ["X", "X", "X"]:

            return "X wins"
        
        if rows == ["O", "O", "O"]:

            return "O wins"
        
    # column

    x = 0

    while x != len(board) - 1:

        column = []

        for rows in board:

            column.append(rows[x])

        if column == ["X", "X", "X"]:

            return "X wins"
        
        if column == ["O", "O", "O"]:

            return "O wins"

        x += 1

    # slanting
        
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):

        return "X wins"

    if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):

        return "O wins"

    return "Draw"
