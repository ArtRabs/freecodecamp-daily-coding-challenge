def get_hill_rating(drop, distance, hill_type):

    if hill_type == "Downhill":

        hill_type = 1.2

    elif hill_type == "Slalom":

        hill_type = 0.9

    elif hill_type == "Giant Slalom":

        hill_type = 1.0


    steep = drop / distance * hill_type
    

    if steep <= 0.1:

        return "Green"

    elif steep > 0.1 and steep <= 0.25:

        return "Blue"
    
    elif steep > 0.25:

        return "Black"
    
if __name__ == "__main__":

    print(get_hill_rating(95, 900, "Slalom"))
    print(get_hill_rating(620, 2800, "Downhill"))
    print(get_hill_rating(420, 1680, "Giant Slalom"))