def get_landing_stance(start_stance, rotation):

    rotation = abs(rotation) % 360

    if rotation in range(0, 180):

        if start_stance == "Regular":

            return "Regular"
        
        elif start_stance == "Goofy":

            return "Goofy"
    
    if rotation in range(180, 360):

        if start_stance == "Regular":

            return "Goofy"
        
        elif start_stance == "Goofy":

            return "Regular"

if __name__ == "__main__":

    print(get_landing_stance("Regular", 90))
    print(get_landing_stance("Regular", 180))
    print(get_landing_stance("Regular", 2340))
    print(get_landing_stance("Goofy", -270))