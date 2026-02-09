class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
if __name__ == "__main__":
    my_plant_1 = plant("Rose", "25", "30")
    my_plant_2 = plant("Sunflower", "80", "45")
    my_plant_3 = plant("Cactus", "15", "120")
    print("=== Garden Plant Registry ===")
    for my_plant in [my_plant_1, my_plant_2, my_plant_3]:
        print(f"{my_plant.name}: {my_plant.height}cm, {my_plant.age} days old")
