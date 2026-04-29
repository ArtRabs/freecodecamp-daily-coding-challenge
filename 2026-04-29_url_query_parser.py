def parse_url_query(url):

    url1 = url.split("?")

    url_dict = {}

    url2 = url1[1].split("&")

    for i in range(len(url2)):

        url3 = url2[i].split("=")

        url_dict[url3[0]] = url3[1]

    return url_dict

if __name__ == "__main__":

    print(parse_url_query("https://example.com/search?name=Alice&age=30"))