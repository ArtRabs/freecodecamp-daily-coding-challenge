def mirror(s):

    mirror = ""

    mirror += s

    reverse_s = s[::-1]

    mirror += reverse_s

    return mirror

if __name__ == "__main__":

    print(mirror("hello"))