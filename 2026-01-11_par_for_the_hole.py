def golf_score(par, strokes):

    if strokes == 1:

        return "Hole in one!"

    if strokes == par - 2:

        return "Eagle"

    if strokes == par - 1:

        return "Birdie"

    if strokes == par:

        return "Par"

    if strokes == par + 1:

        return "Bogey"

    if strokes == par + 2:

        return "Double bogey"   

    return par

if __name__ == "__main__":
    pass