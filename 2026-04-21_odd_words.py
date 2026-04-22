def get_odd_words(s):

    split_s = s.split(' ')
    
    odd_words = []
                 
    for word in split_s:

        if len(word) % 2 != 0:

            odd_words.append(word)

    s = ' '.join(odd_words)

    return s