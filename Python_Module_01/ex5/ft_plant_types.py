class Plant:
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size


class Flower(Plant):
    def __init__(self, name, age, size, color):
        super().__init__(name, age, size)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, age, size, trunk_diameter, shade):
        super().__init__(name, age, size)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self):
        print(f"{self.name} provides {self.shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, age, size, harvest_season, nutritional_value):
        super().__init__(name, age, size)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutritional_value(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    Rose = Flower("Rose", 30, 25, "red")
    Margarite = Flower("Margarite", 20, 15, "White")

    Oak = Tree("Oak", 1825, 500, 50, 78)
    Pine = Tree("Pine", 80, 300, 40, 150)

    Carrot = Vegetable("Carrot", 60, 10, "summer", "vitamin A")
    Tomato = Vegetable("Tomato", 90, 80, "summer", "vitamin C")

    print("=== Garden Plant Types ===")
    print(f"{Rose.name} (Flower): {Rose.size}cm, {Rose.age} days, {Rose.color} color")
    Rose.bloom()

    print(f"{Oak.name} (Tree): {Oak.size}cm, {Oak.age} days, {Oak.trunk_diameter}cm diameter")
    Oak.produce_shade()

    print(f"{Tomato.name} (Vegetable): {Tomato.size}cm, {Tomato.age} days, {Tomato.harvest_season} harvest")
    Tomato.show_nutritional_value()

