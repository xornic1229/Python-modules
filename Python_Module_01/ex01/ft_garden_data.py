#!/usr/bin/env python3

class Plant:
    """A class to represent a plant in the garden."""
    
    def __init__(self, name, height, age):
        """
        Initialize a plant with its attributes.
        
        Args:
            name (str): The name of the plant
            height (str): The height of the plant (e.g., "25cm")
            age (str): The age of the plant (e.g., "30 days")
        """
        self.name = name
        self.height = height
        self.age = age
    
    def __str__(self):
        """Return a formatted string representation of the plant."""
        return f"{self.name}: {self.height}, {self.age} old"


if __name__ == "__main__":
    # Create multiple plants
    plant1 = Plant("Rose", "25cm", "30 days")
    plant2 = Plant("Sunflower", "80cm", "45 days")
    plant3 = Plant("Cactus", "15cm", "120 days")
    
    # Display the garden registry
    print("=== Garden Plant Registry ===")
    print(plant1)
    print(plant2)
    print(plant3)
