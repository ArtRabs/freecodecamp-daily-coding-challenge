def compare_energy(calories_burned, watt_hours_used):

    calorie = 4184

    watt_hour = 3600

    calories_burned *= calorie

    watt_hours_used *= watt_hour

    if calories_burned > watt_hours_used:

        return "Workout"
    
    elif calories_burned < watt_hours_used:

        return "Devices"
    
    elif calories_burned == watt_hours_used:

        return "Equal"

print(compare_energy(250, 50))
print(compare_energy(100, 200))
print(compare_energy(450, 523))