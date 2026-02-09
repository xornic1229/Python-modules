def ft_first_exception():
    """Exercise 0: First Exception Handling"""
    try:
        # Intentionally raise an exception to demonstrate handling
        raise ValueError("This is a sample exception for demonstration.")
    except ValueError as e:
        print(f"Caught an exception: {e}")
if __name__ == "__main__":
    ft_first_exception()
Compare this snippet from Python_Module_00/test_all_exercises.py:
def test_ex0():
    """Test Exercise 0: ft_hello_garden"""
    print_separator("Exercise 0: ft_hello_garden")
    ft_hello_garden()
        