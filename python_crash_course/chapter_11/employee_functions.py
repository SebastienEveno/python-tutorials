class Employee:
    def __init__(self, first_name, last_name, annual_salary_amount):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary_amount = annual_salary_amount
    
    def give_raise(self, amount=5000):
        self.annual_salary_amount += amount