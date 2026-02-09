def calculate_penalty_distance(rounds):

    total_meters = 0

    for target in rounds:

        target = 5 - target
        penalty = target * 150
        total_meters += penalty

    return total_meters

if __name__ == "__main__":

    print(calculate_penalty_distance([5, 5]))
    print(calculate_penalty_distance([5, 4, 5, 5]))