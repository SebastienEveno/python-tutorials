"""A class that can be used to represent a restaurant."""

class Restaurant:
    
    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine_type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Describes the restaurant."""
        print(f"This restaurant called '{self.name.title()}' is {self.cuisine_type.title()}-type.")

    def open_restaurant(self):
        """Indicates if the restaurant is open."""
        print(f"{self.name.title()} is open!")

    def get_number_served(self):
        """Return the number of clients served."""
        print(f"This restaurant has served {self.number_served} clients.")
    
    def set_number_served(self, number):
        """Update the number of customers served."""
        self.number_served = number