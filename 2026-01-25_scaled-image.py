def scale_image(size, scale):

    resolution = size.split("x")

    new_resolution = []

    for pixel in resolution:

        new_resolution.append(int(int(pixel) * scale))

    return f"{new_resolution[0]}x{new_resolution[1]}"

if __name__ == "__main__":

    print(scale_image("800x600", 2))
    print(scale_image("1024x768", 0.5))
