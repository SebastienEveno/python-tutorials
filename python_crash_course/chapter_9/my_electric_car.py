import car

if __name__ == "__main__":
    my_beetle = car.Car('volkswagen', 'beetle', 2019)
    print(my_beetle.get_descriptive_name())
    
    my_tesla = car.ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
