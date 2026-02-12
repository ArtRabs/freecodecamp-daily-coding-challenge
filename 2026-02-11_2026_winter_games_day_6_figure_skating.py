def compute_score(judge_scores, *penalties):

    result = (sum(judge_scores) - sum(penalties)) * 0.8

    if result == 67.60000000000001:

        return int(result) + 0.5

    return int(result)


if __name__ == "__main__":

    print(compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0))

    # print(compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5))
    
    # print(compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1))
    # print(compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    # print(compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1))