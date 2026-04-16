from collections import Counter
import re

def has_no_repeats(s):

    split_s = s.split(' ')
    for word in split_s:

        # only A–Z or a–z
        letters = re.findall(r"[A-Za-z]", word)    
        # normalize case
        counts = Counter(ch.lower() for ch in letters)
        # if count is greater than 1, it repeats a letter
        repeated = {ch: cnt for ch, cnt in counts.items() if cnt > 1}

        if repeated:

            return False

    return True

if __name__ == "__main__":

    s = "The quick brown fox jumped over the lazy dog"
    print(has_no_repeats(s))