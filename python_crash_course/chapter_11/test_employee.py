import unittest
from employee_functions import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Elon', 'Musk', 60000)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary_amount, 65000)

    def test_give_custom_raise(self):
        self.employee.give_raise(7000)
        self.assertEqual(self.employee.annual_salary_amount, 67000)

if __name__ == "__main__":
    unittest.main()
