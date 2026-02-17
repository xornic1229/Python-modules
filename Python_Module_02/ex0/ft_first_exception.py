def check_temperature(temp_str):
    try:
        temp = int(temp_str)

        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        return temp
    except:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    print("Testing temperature: 25")
    temp = check_temperature("25")
    if temp is not None:
        print(f"Temperature {temp}°C is perfect for plants!")

    print("Testing temperature: abc")
    check_temperature("abc")

    print("Testing temperature: 100")
    check_temperature("100")

    print("Testing temperature:-50")
    check_temperature("-50")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()