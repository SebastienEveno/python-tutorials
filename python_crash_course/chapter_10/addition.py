def enter_a_number():
    while True:
        number_1 = input("Please enter a number:\n")
        try:
            number_1 = int(number_1)
        except ValueError:
            print("You did not enter a number.\n")
        else:
            return number_1

if __name__ == "__main__":
    a = enter_a_number()
    b = enter_a_number()
    print(f"The sum is equal to {a + b}.")