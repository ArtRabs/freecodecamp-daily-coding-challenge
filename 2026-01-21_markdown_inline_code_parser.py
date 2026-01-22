def parse_inline_code(markdown):

    index1 = markdown.index("`")
    index2 = markdown.index("`", markdown.index("`") + 1)

    word = markdown[index1 : index2]
    word1 = markdown[index1 : index2 + 1]

    parse1 = word.replace("`","<code>")
    parse1 += "</code>"

    parsed = markdown.replace(word1, parse1)
    
    count = markdown.count("`")

    while count > 2:

        index1 = parsed.index("`")
        index2 = parsed.index("`", parsed.index("`") + 1)

        word = parsed[index1 : index2]
        word1 = parsed[index1 : index2 + 1]

        parse1 = word.replace("`","<code>")
        parse1 += "</code>"

        parsed = parsed.replace(word1, parse1)

        count = count - 2

    return parsed

if __name__ == "__main__":
    
    print(parse_inline_code("Use `let` to declare the variable."))
    print(parse_inline_code("Use `let` or `const` to declare a variable."))