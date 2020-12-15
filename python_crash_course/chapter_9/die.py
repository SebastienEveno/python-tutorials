"""A class that can be used to represent a die."""

from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

if __name__ == "__main__":
    my_die = Die()
    my_die.roll_die()

    my_die_10 = Die(10)
    my_die_10.roll_die()