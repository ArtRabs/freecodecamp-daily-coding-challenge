def get_fastest_speed(times):

    segments = [320, 280, 350, 300, 250]
    i = 0
    place = []
    fastest_speed = 0
    top_place = 0
    
    for seconds in times:

        place.append(segments[i] / seconds)

        if (segments[i] / seconds) > fastest_speed:

            fastest_speed = segments[i] / seconds

            top_place = i

        i += 1

    return f"The luger's fastest speed was {fastest_speed:.2f} m/s on segment {top_place + 1}."

if __name__ == '__main__':

    print(get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]))