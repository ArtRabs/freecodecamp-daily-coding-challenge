def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):

    jumper_total_scores = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]

    total_score = distance_points + style_points + wind_comp + k_point_bonus

    jumper_total_scores.append(total_score)

    jumper_total_scores.sort(reverse=True)

    place = jumper_total_scores.index(total_score)

    if place == 0:

        return "Gold"

    elif place == 1:

        return "Silver"

    elif place == 2:

        return "Bronze"
    
    else:

        return "No Medal"
    
if __name__ == "__main__":

    print(ski_jump_medal(125.0, 58.0, 0.0, 6.0))