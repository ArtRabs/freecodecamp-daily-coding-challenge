def to_snake(camel):

    snake = ""

    for letter in camel:

        if letter.isupper():

            snake += "_" + letter.lower()

        else:

            snake += letter

    return snake

if __name__ == "__main__":

    print(to_snake("helloWorld"))
    print(to_snake("myVariableName"))