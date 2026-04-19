def get_captured_value(pieces):

    total = 39

    chess_values = {
        "P": 1,   # Pawn
        "R": 5,   # Rook
        "N": 3,   # Knight
        "B": 3,   # Bishop
        "Q": 9,   # Queen
        "K": 0    # King
    }

    if "P" and "R" and "N" and "B" and "Q" in pieces and "K" not in pieces:

        return "Checkmate"

    for chess in pieces:

        total -= chess_values[chess]

    return total