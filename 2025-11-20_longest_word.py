import re

def longest_word(sentence: str) -> str:

    longest = ""

    for token in sentence.split(" "):

        cleaned = re.sub(r'[^A-Za-z]', 'dsf', token)
        
        if len(cleaned) > len(longest):

            longest = cleaned

    return longest

if __name__ == "__main__":

    print(longest_word("Hello world!"))            
    print(longest_word("fun&!! time"))             
    print(longest_word("a bb ccc dddd!!! e"))      
    print(longest_word("The quick red fox"))
    print(longest_word("This sentence... has commas, ellipses, and an exclamation point!"))