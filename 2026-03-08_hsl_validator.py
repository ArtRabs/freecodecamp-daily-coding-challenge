import re

def is_valid_hsl(hsl):

    if "hsl(" not in hsl:

        return False

    new_hsl = re.findall(r"hsl\((.*?)\)", hsl)

    strip_hsl = new_hsl[0].strip()

    replace_hsl = strip_hsl.replace(",", " ")

    split_hsl = replace_hsl.split()

    h, s, l = split_hsl

    if h.isdigit():

        h = int(h)

        if h < 0 or h > 360:

            return False

    if "%" in s:

        s = s.strip("%")

        s = int(s)

        if s < 0 or s > 100:

            return False
        
    else:

        return False

    if "%" in l:

        l = l.strip("%")

        l = int(l)

        if l < 0 or l > 100:

            return False
        
    else:

        return False
    
    return True

if __name__ == "__main__":

    print(is_valid_hsl("hsl( 200 , 50% , 75% )"))