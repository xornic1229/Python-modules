class Plant:
    
    def __init__(self, name, height, age):
        self.name = name
        self.height = height  # in cm
        self.age = age  # in days


if __name__ == "__main__":

    total_plants = 0
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)
    plants = [plant1, plant2, plant3, plant4, plant5]
    
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        total_plants += 1

    print(f"\nTotal plants created: {total_plants}")


