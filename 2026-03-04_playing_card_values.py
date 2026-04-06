def card_values(cards):

    # save the value of each card
    card_value = []

    # loop through each card
    for card in cards:

        # check if card is Ace, Jack, Queen, or King
        if card[0].isalpha():

            # if it is Jack, Queen, or King, add 10
            if card[0] in "JQK":

                card_value.append(10)

            # if it is Ace, add 1
            elif card[0] == "A":

                card_value.append(1)

        # check if card is 10 then add 10
        elif card[0:2] == "10":

            card_value.append(10)

        # check if card is from 2 to 9 then add the number itself by using int()
        elif card[0].isdigit():

            card_value.append(int(card[0]))

    return card_value

if __name__ == "__main__":

    print(card_values(["2C", "3D", "AD", "QH"]))
    print(card_values(["AS", "10S", "10H", "6D", "7D"]))
    print(card_values(["10H", "JH", "QH", "KH", "AH"]))