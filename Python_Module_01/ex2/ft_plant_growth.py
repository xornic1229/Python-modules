#!/usr/bin/env python3

class Plant:
    """A class to represent a plant in the garden with growth simulation."""
    
    def __init__(self, name, height, age):
        """
        Initialize a plant with its attributes.
        
        Args:
            name (str): The name of the plant
            height (int): The height of the plant in centimeters
            age (int): The age of the plant in days
        """
        self.name = name
        self.height = height  # in cm
        self.age = age  # in days
        self.initial_height = height  # Store initial height for growth tracking
    
    def grow(self):
        """Simulate the plant growing by increasing its height."""
        self.height += 1
    
    def age_plant(self):
        """Age the plant by one day."""
        self.age += 1
    
    def get_info(self):
        """Return the current state information of the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"
    
    def get_growth_this_week(self):
        """Calculate and return the growth in the last week (7 days)."""
        # Growth is calculated based on the change from initial height
        # In this simulation, we grow 1cm per day, so 7 days = 7cm growth
        return self.height - self.initial_height


if __name__ == "__main__":
    # Create a plant
    rose = Plant("Rose", 25, 30)
    
    # Day 1 - Show initial state
    print("=== Day 1 ===")
    print(rose.get_info())
    
    # Simulate 6 more days (Day 1 to Day 7)
    for day in range(6):
        rose.grow()
        rose.age_plant()
    
    # Day 7 - Show final state
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.get_growth_this_week()}cm")
