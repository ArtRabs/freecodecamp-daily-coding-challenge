def get_element_size(window_size, element_vw, element_vh):

    # remove "x" then get window size
    window_size = window_size.split("x")
    window_width = int(window_size[0])
    window_height = int(window_size[1])

    # remove "vw" and "vh"
    element_vw = element_vw.replace("vw", "")
    element_vh = element_vh.replace("vh", "")

    # calculate element size
    element_width = int(element_vw) * window_width / 100
    element_height = int(element_vh) * window_height / 100

    return f"{int(element_width)} x {int(element_height)}"


if __name__ == "__main__":

    print(get_element_size("1200 x 800", "50vw", "50vh"))