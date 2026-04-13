def get_initials(name):

    name_array = name.split(" ")
    initials = ""

    for char in name_array:

        initials += char[0] + "."

    return initials

if __name__ == "__main__":

    print(get_initials("John Doe"))