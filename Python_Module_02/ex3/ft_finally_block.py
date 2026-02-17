def water_plants(plant_list):
    print("Opening watering system")
    try:
        i = 0
        while i < len(plant_list):
            plant = plant_list[i]
            if plant is None:
                raise Exception
            print(f"Watering {plant}")
            i += 1
    except:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
