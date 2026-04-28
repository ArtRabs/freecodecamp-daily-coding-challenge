# just for random sample
import random

def get_number_words(n):

    # set up dictionaries
    ones = {
        0: "zero",
        1: "one", 
        2: "two", 
        3: "three", 
        4: "four", 
        5: "five", 
        6: "six", 
        7: "seven", 
        8: "eight", 
        9: "nine", 
        }
    
    tens = {
        20: "twenty", 
        30: "thirty", 
        40: "forty", 
        50: "fifty", 
        60: "sixty", 
        70: "seventy", 
        80: "eighty", 
        90: "ninety"
        }
    
    teens = {
        10: "ten",
        11: "eleven", 
        12: "twelve", 
        13: "thirteen", 
        14: "fourteen", 
        15: "fifteen", 
        16: "sixteen", 
        17: "seventeen", 
        18: "eighteen", 
        19: "nineteen"
        }
    
    # if n is in ones, teens, or tens, return it
    if n in ones:

        return ones[n]
    
    elif n in teens:

        return teens[n]
    
    elif n in tens:

        return tens[n]
    
    # if n is > 20 and < 100, return the tens and ones words
    # modulus to separate the digit into tens and ones
    # * 10 so it will be equal to 20, 30, 40, etc. in tens dictionary
    return f"{tens[(n // 10 % 10) * 10]}-{ones[n % 10]}"

if __name__ == "__main__":

    print(get_number_words(23))
    print(get_number_words(random.randint(0, 99)))
    print(get_number_words(random.randint(0, 99)))
    print(get_number_words(random.randint(0, 99)))