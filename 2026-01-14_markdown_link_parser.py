def parse_link(markdown):

    # replaces all spaces and replace the outer square bracket as space to split it properly
    markdown_replace = markdown.replace(" ", "_").replace("[", "").replace("]", " ")
    markdown_split = markdown_replace.split()
    
    link_text, link_url = markdown_split

    # bring back the original spaces
    link_text = link_text.replace("_", " ")
    # removes the "(" and ")" only at the first and end part
    link_url = link_url[1:-1]

    parse = f'<a href="{link_url}">{link_text}</a>'

    return parse

if __name__ == "__main__":

    print(parse_link("[freeCodeCamp](https://freecodecamp.org/)"))
    print(parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)"))
    print(parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)"))
