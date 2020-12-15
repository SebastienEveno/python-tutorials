class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

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

class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream stands."""
    def __init__(self, name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Initialize flavors.
        """
        super().__init__(name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate','oreo', 'mint']

    def display_flavors(self):
        print(f"At {self.name.title()}, our available flavors are:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
        

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def upgrade_battery(self):
        print("Upgrading battery...")
        if self.battery.battery_size != 100:
            self.battery.battery_size = 100
        print(f"The battery has been upgraded to {self.battery.battery_size}-kWh.")
    
if __name__ == "__main__":
    dog = Dog('Willie', 6)
    dog.roll_over()

    resto_1 = Restaurant('Pilipili', 'Italian')
    resto_2 = Restaurant('Kindo', 'Asian')
    resto_3 = Restaurant('Saint-Michel', 'French')
    resto_1.describe_restaurant()
    resto_2.describe_restaurant()
    resto_3.describe_restaurant()

    resto_1.get_number_served()
    resto_1.set_number_served(10)
    resto_1.get_number_served()

    my_new_car = Car('audi', 'a4', 2019)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    my_new_car.update_odometer(23)
    my_new_car.read_odometer()

    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
    my_tesla.upgrade_battery()
    my_tesla.battery.get_range()

    my_icecream_stand = IceCreamStand('miko', 'italian')
    my_icecream_stand.display_flavors()