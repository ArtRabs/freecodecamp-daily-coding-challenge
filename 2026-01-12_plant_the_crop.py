def get_number_of_plants(field_size, unit, crop):

    acre = 4046.86 * field_size

    hectare = 10000 * field_size


    if unit == "acres":

        unit = acre

    elif unit == "hectares":

        unit = hectare


    if crop == "corn":

        crops = unit * 1

    elif crop == "wheat":

        crops = unit * 9

    elif crop == "soybeans":

        crops = unit * 2

    elif crop == "tomatoes":

        crops = unit * 4

    elif crop == "lettuce":

        crops = unit * 5

    return int(crops)

if __name__ == "__main__":
    print(get_number_of_plants(1, "acres", "corn"))
    print(get_number_of_plants(2, "hectares", "lettuce"))