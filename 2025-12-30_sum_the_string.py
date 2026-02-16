def string_sum(s):

    current_string = ""
    all_num = []

    for char in s:

        if char.isalpha():

            current_string += " "

        if char.isdigit():

            current_string += char

    current_num = current_string.split(" ")

    for num in current_num:

        if num != "":

            all_num.append(int(num))

    return sum(all_num)

if __name__ == "__main__":

    print(string_sum("a1b20c300"))
    print(string_sum("10cats5dogs2birds"))
    print(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"))





# def string_sum(s):

    # is_letter = False
    # is_number = False
    # always_number = True

    # total_num = 0
    # current_num = ""

    # alphabet = "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # for character in s:

    #     if character not in alphabet:

    #         is_number = True

    #     if is_number and not is_letter:

    #         current_num += str(character)

    #     if is_number and is_letter:

    #         if current_num == "":

    #             total_num += int(character)

    #         else:
            
    #             total_num += int(current_num) + int(character)
    #             current_num = ""

    #         is_letter = False
    #         always_number = False

    #     if character in alphabet:

    #         is_letter = True
    #         always_number = False

    #     is_number = False

    # if current_num.isdigit() and always_number:

    #     total_num = int(current_num)

    # return total_num