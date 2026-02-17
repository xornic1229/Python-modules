class GardenError(Exception):
    def __init__(self, message):
        self.message = message


class PlantError(GardenError):
    def __init__(self, message):
        self.message = message


class WaterError(GardenError):
    def __init__(self, message):
        self.message = message


def trigger_plant_error():
    raise PlantError("The tomato plant is wilting!")


def trigger_water_error():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        trigger_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e.message}")

    print("Testing WaterError...")
    try:
        trigger_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e.message}")

    print("Testing catching all garden errors...")
    try:
        trigger_plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e.message}")

    try:
        trigger_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e.message}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
