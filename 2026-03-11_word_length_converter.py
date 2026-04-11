def convert_words(s):

    # split the words into array
    split_string = s.split(" ")

    # get all len() of each word
    len_strings = list(map(len, split_string))

    # convert the len_strings into a single string
    converted_words = " ".join(map(str, len_strings))

    return converted_words

print(convert_words("Hello World"))
print(convert_words("The quick brown fox jumps over the lazy dog"))


# def convert_words(s):

#     split_string = s.split(" ")
#     len_of_string = []

#     for word in split_string:

#         len_of_string.append(len(word))

#     converted_words = " ".join(map(str, len_of_string))

#     return converted_words