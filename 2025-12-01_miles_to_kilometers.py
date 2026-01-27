def convert_to_km(miles):

    miles *= 1.60934

    return round(miles, 2)

if __name__ == "__main__":

    print(convert_to_km(10))