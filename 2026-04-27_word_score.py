def get_word_score(word):

    word = word.lower()

    score = 0

    for letter in word:

        score += ord(letter) - 96

    return score

if __name__ == '__main__':

    print(get_word_score("abc"))
    print(get_word_score("hello"))