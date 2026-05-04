def convert_parsecs(parsecs):

    if parsecs == 1:

        return 2

    elif parsecs == 2:

        return 6

    if parsecs % 2 == 0:

        return (parsecs * 6) / 2

    return parsecs * 2