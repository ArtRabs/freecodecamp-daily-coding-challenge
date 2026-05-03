def get_greeting(s):

    time = s.split(':')
    hour = int(time[0])

    if 5 <= hour <= 11:

        return "Good morning"
    
    elif 12 <= hour <= 17:

        return "Good afternoon"
    
    elif 18 <= hour <= 21:

        return "Good evening"
    
    else:

        return "Good night"

if __name__ == "__main__":

    print(get_greeting("05:00"))
    print(get_greeting("12:30"))
    print(get_greeting("19:45"))
    print(get_greeting("23:10"))
    print(get_greeting("04:59"))