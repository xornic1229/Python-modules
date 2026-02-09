class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        
    def grow(self):
        self.height = self.height + 1

    def age_one_day(self):
        self.age = self.age + 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    rose = plant("Rose", 25, 30)
    initial_height = rose.height
    print("=== Day 1 ===")
    rose.get_info()
    day = 2
    while day <= 7:
        rose.grow()
        rose.age_one_day()
        day += 1

    print("=== Day 7 ===")
    rose.get_info()

    growth = rose.height - initial_height
    print(f"Growth this week: +{growth}cm")