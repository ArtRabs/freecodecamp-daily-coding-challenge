def truncate_text(text):

    if len(text) > 20:

        truncate_text = text[0:17]
        truncate_text += "..."

        return truncate_text

    return text

if __name__ == "__main__":

    print(truncate_text("Hello, world!"))
    print(truncate_text("This string should not get truncated."))