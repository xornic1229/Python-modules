def garden_operations():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing ZeroDivisionError...")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught {e}: No such file 'missing.txt'")

    print("Testing KeyError...")
    try:
        garden = {"rose": 5}
        value = garden["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")


def test_error_types():
    print("=== Garden Error Types Demo ===")

    garden_operations()

    print("Testing multiple errors together...")
    try:
        int("abc")
        result = 10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
