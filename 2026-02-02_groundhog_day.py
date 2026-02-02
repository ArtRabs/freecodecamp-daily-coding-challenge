def groundhog_day_prediction(appearance):

    if appearance == True:

        return "Looks like we'll have six more weeks of winter."
    
    elif appearance == False:

        return "It's going to be an early spring."
    
    elif not isinstance(appearance, bool):

        return "No prediction this year."

if __name__ == "__main__":

    print(groundhog_day_prediction(True))
    print(groundhog_day_prediction(False))
    print(groundhog_day_prediction(None))
    print(groundhog_day_prediction(None))
    print(groundhog_day_prediction("True"))