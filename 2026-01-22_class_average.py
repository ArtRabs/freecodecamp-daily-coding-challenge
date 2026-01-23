def get_average_grade(scores):

    average_score = sum(scores) / len(scores)
    average_score = int(average_score)

    if average_score <= 100 and average_score >= 97:

        return "A+"

    elif average_score <= 96 and average_score >= 93:

        return "A"
    
    elif average_score <= 92 and average_score >= 90:

        return "A-"
    
    elif average_score <= 89 and average_score >= 87:

        return "B+"
    
    elif average_score <= 86 and average_score >= 83:

        return "B"
    
    elif average_score <= 82 and average_score >= 80:

        return "B-"
    
    elif average_score <= 79 and average_score >= 77:

        return "C+"
    
    elif average_score <= 76 and average_score >= 73:

        return "C"
    
    elif average_score <= 70 and average_score >= 72:

        return "C-"
    
    elif average_score <= 69 and average_score >= 67:

        return "D+"
    
    elif average_score <= 66 and average_score >= 63:

        return "D"
    
    elif average_score <= 62 and average_score >= 60:

        return "D-"
    
    elif average_score < 59:

        return "F"

    return average_score

if __name__ == "__main__":

    print(get_average_grade([63, 69, 65, 66, 71, 64, 65]))