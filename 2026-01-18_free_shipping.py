def gets_free_shipping(cart, minimum):

    prices = {

        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95

    }

    total = 0

    for item in cart:

        if item in prices.keys():

            total += prices[item]

    if total < minimum:

        return False

    return True

if __name__ == "__main__":
    print(gets_free_shipping(["hat", "socks"], 50))
    print(gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100))
    print(gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200))