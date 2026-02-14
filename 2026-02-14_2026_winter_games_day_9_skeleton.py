def get_difficulty(track):

    points = 0
    is_l = False
    is_r = False
    is_s = False

    for move in track:

        if move == "L":

            if is_r:

                points += 15

                is_l = True
                is_r = False
                is_s = False

            else:

                points += 5

                is_l = True
                is_r = False
                is_s = False

        elif move == "R":

            if is_l:

                points += 15

                is_l = False
                is_r = True
                is_s = False

            else:

                points += 5

                is_l = False
                is_r = True
                is_s = False

        elif move == "S":

            points += 0

            is_l = False
            is_r = False
            is_s = True

    if points >= 0 and points <= 100:

        return "Easy"
    
    elif points >= 101 and points <= 200:

        return "Medium"
    
    elif points > 200:

        return "Hard"

if __name__ == "__main__":

    print(get_difficulty("SLSLLSRRLSRLRL"))