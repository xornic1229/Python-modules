class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.kind = "regular"

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")
        return 1

    def describe(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False
        self.kind = "flowering"

    def bloom(self):
        self.is_blooming = True

    def grow(self):
        self.bloom()
        return super().grow()

    def describe(self):
        status = " (blooming)" if self.is_blooming else ""
        return f"{self.name}: {self.height}cm, {self.color} flowers{status}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points
        self.kind = "prize"

    def describe(self):
        base = super().describe()
        return f"{base}, Prize points: {self.prize_points}"


class GardenManager:
    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def plants_added(self):
            return self.garden.plant_count

        def total_growth(self):
            return self.garden.total_growth_cm

        def count_types(self):
            regular = 0
            flowering = 0
            prize = 0
            i = 0
            while i < self.garden.plant_count:
                k = self.garden.plants[i].kind
                if k == "prize":
                    prize += 1
                elif k == "flowering":
                    flowering += 1
                else:
                    regular += 1
                i += 1
            return regular, flowering, prize

        def validate_all_heights(self):
            i = 0
            while i < self.garden.plant_count:
                if not GardenManager.validate_height(self.garden.plants[i].height):
                    return False
                i += 1
            return True

        def score(self):
            total = 0
            blooming = 0
            prize_bonus = 0
            i = 0
            while i < self.garden.plant_count:
                p = self.garden.plants[i]
                total += p.height
                if p.kind == "flowering" or p.kind == "prize":
                    if p.is_blooming:
                        blooming += 1
                if p.kind == "prize":
                    prize_bonus += 2 * p.prize_points
                i += 1
            return total + 10 * blooming + prize_bonus

    class Garden:
        def __init__(self, owner):
            self.owner = owner
            self.plants = []
            self.plant_count = 0
            self.total_growth_cm = 0
            self.stats = GardenManager.GardenStats(self)

        def add_plant(self, plant):
            self.plants.append(plant)
            self.plant_count += 1
            print(f"Added {plant.name} to {self.owner}'s garden")

        def help_all_grow(self):
            print(f"{self.owner} is helping all plants grow...")
            i = 0
            while i < self.plant_count:
                self.total_growth_cm += self.plants[i].grow()
                i += 1

        def report(self):
            print(f"=== {self.owner}'s Garden Report ===")
            line = "Plants in garden:"
            i = 0
            while i < self.plant_count:
                line += f"- {self.plants[i].describe()}"
                i += 1
            print(line)

            regular, flowering, prize = self.stats.count_types()
            print(f"Plants added: {self.stats.plants_added()}, Total growth: {self.stats.total_growth()}cm")
            print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")
            print(f"Height validation test: {self.stats.validate_all_heights()}")

    def __init__(self):
        self.gardens = []
        self.garden_count = 0

    def add_garden(self, owner):
        g = GardenManager.Garden(owner)
        self.gardens.append(g)
        self.garden_count += 1
        return g

    @classmethod
    def create_garden_network(cls):
        return cls.__name__

    @staticmethod
    def validate_height(height):
        return height >= 0 and height <= 10000

    def print_scores(self):
        print("Garden scores")
        i = 0
        while i < self.garden_count:
            g = self.gardens[i]
            print(f"- {g.owner}: {g.stats.score()}")
            i += 1
        print(f"Total gardens managed: {self.garden_count}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager = GardenManager()
    manager.create_garden_network()

    alice_garden = manager.add_garden("Alice")
    bob_garden = manager.add_garden("Bob")

    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    alice_garden.help_all_grow()
    alice_garden.report()

    bob_garden.add_plant(Plant("Basil", 92))

    manager.print_scores()


