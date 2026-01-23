def parse_inline_code(markdown):

    count = markdown.count("`")
    
    while count > 0:

        index1 = markdown.index("`")
        index2 = markdown.index("`", markdown.index("`") + 1)

        word1 = markdown[index1 : index2]
        word2 = markdown[index1 : index2 + 1]

        parse = word1.replace("`","<code>")
        parse += "</code>"

        markdown = markdown.replace(word2, parse)

        count = count - 2

    return markdown

if __name__ == "__main__":
    
    print(parse_inline_code("Use `let` to declare the variable."))
    print(parse_inline_code("Use `let` or `const` to declare a variable."))