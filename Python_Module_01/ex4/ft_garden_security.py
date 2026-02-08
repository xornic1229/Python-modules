#!/usr/bin/env python3

class SecurePlant:
    
    def __init__(self, name, height, age):

        self.name = name
        self._height = None
        self._age = None
        
        self.set_height(height)
        self.set_age(age)
    
    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return False
        
        self._height = height
        print(f"Height updated: {height}cm [OK]")
        return True
    
    def set_age(self, age):

        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return False
        
        self._age = age
        print(f"Age updated: {age} days [OK]")
        return True

    def get_height(self):
        return self._height
    
    def get_age(self):
        return self._age
    
    def __str__(self):
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    
    plant = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {plant.name}")
    
    plant.set_height(-5)
    
    print(f"Current plant: {plant.name} ({plant.height}cm, {plant.age} days)")

