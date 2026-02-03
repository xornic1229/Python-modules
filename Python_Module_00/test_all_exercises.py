#!/usr/bin/env python3
"""
Test script for all Python_Module_00 exercises
"""

import sys
from io import StringIO
from unittest.mock import patch

# Import all functions
sys.path.insert(0, 'ex0')
sys.path.insert(0, 'ex1')
sys.path.insert(0, 'ex2')
sys.path.insert(0, 'ex3')
sys.path.insert(0, 'ex4')
sys.path.insert(0, 'ex5')
sys.path.insert(0, 'ex6')
sys.path.insert(0, 'ex7')

from ft_hello_garden import ft_hello_garden
from ft_plot_area import ft_plot_area
from ft_harvest_total import ft_harvest_total
from ft_plant_age import ft_plant_age
from ft_water_reminder import ft_water_reminder
from ft_count_harvest_iterative import ft_count_harvest_iterative
from ft_count_harvest_recursive import ft_count_harvest_recursive
from ft_garden_summary import ft_garden_summary
from ft_seed_inventory import ft_seed_inventory


def print_separator(title):
    """Print a section separator"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def test_ex0():
    """Test Exercise 0: ft_hello_garden"""
    print_separator("Exercise 0: ft_hello_garden")
    ft_hello_garden()


def test_ex1():
    """Test Exercise 1: ft_plot_area"""
    print_separator("Exercise 1: ft_plot_area")
    with patch('builtins.input', side_effect=['5', '4']):
        ft_plot_area()


def test_ex2():
    """Test Exercise 2: ft_harvest_total"""
    print_separator("Exercise 2: ft_harvest_total")
    with patch('builtins.input', side_effect=['10', '15', '8']):
        ft_harvest_total()


def test_ex3():
    """Test Exercise 3: ft_plant_age"""
    print_separator("Exercise 3: ft_plant_age")
    print("\nTest case 1 (45 days):")
    with patch('builtins.input', return_value='45'):
        ft_plant_age()
    
    print("\nTest case 2 (70 days):")
    with patch('builtins.input', return_value='70'):
        ft_plant_age()


def test_ex4():
    """Test Exercise 4: ft_water_reminder"""
    print_separator("Exercise 4: ft_water_reminder")
    print("\nTest case 1 (1 day):")
    with patch('builtins.input', return_value='1'):
        ft_water_reminder()
    
    print("\nTest case 2 (4 days):")
    with patch('builtins.input', return_value='4'):
        ft_water_reminder()


def test_ex5():
    """Test Exercise 5: ft_count_harvest (iterative and recursive)"""
    print_separator("Exercise 5: ft_count_harvest_iterative")
    with patch('builtins.input', return_value='5'):
        ft_count_harvest_iterative()
    
    print_separator("Exercise 5: ft_count_harvest_recursive")
    with patch('builtins.input', return_value='5'):
        ft_count_harvest_recursive()


def test_ex6():
    """Test Exercise 6: ft_garden_summary"""
    print_separator("Exercise 6: ft_garden_summary")
    with patch('builtins.input', side_effect=['Community Garden', '25']):
        ft_garden_summary()


def test_ex7():
    """Test Exercise 7: ft_seed_inventory"""
    print_separator("Exercise 7: ft_seed_inventory")
    print("\nTest case 1 (tomato, 15 packets):")
    ft_seed_inventory("tomato", 15, "packets")
    
    print("\nTest case 2 (carrot, 8 grams):")
    ft_seed_inventory("carrot", 8, "grams")
    
    print("\nTest case 3 (lettuce, 12 area):")
    ft_seed_inventory("lettuce", 12, "area")
    
    print("\nTest case 4 (basil, 10 unknown unit):")
    ft_seed_inventory("basil", 10, "kilos")


def main():
    """Run all tests"""
    print("\n" + "#" * 60)
    print("#  TESTING ALL PYTHON_MODULE_00 EXERCISES")
    print("#" * 60)
    
    try:
        test_ex0()
        test_ex1()
        test_ex2()
        test_ex3()
        test_ex4()
        test_ex5()
        test_ex6()
        test_ex7()
        
        print("\n" + "#" * 60)
        print("#  ALL TESTS COMPLETED SUCCESSFULLY!")
        print("#" * 60 + "\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
