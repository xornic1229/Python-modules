def ft_plant_age():
    number_of_days = int(input("Enter plant age in days: "))
    if number_of_days <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")