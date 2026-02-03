def ft_count_harvest_iterative():
    total_harvest = 0
    days = int(input("Days until harvest: "))
    for day in range(1, days + 1):
        print(f"Day {day}")
        total_harvest+=1
    print("Total harvest:", total_harvest)
