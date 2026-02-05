def count_change(change):

    total = list(map(lambda x: x/100, change))

    return f"${sum(total)}"

if __name__ == "__main__":

    print(count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]))