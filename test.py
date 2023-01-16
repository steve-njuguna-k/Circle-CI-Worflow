import unittest
from main import Employee

class Testing(unittest.TestCase):
    def test_add_employee(self):
        employee = Employee('Mike', 'Brown', 50000, 'Software Developer', 'Active', 'IT')
        self.assertEqual(employee.first_name, 'Mike')
        self.assertEqual(employee.last_name, 'Brown')
        self.assertEqual(employee.salary, 50000)
        self.assertEqual(employee.position, 'Software Developer')
        self.assertEqual(employee.employment_status, 'Active')
        self.assertEqual(employee.department, 'IT')

    def test_increase_salary(self):
        employee = Employee('Mike', 'Brown', 50000, 'Software Developer', 'Active', 'IT')
        increament = 20
        new_salary = (employee.salary * increament/100) + employee.salary
        employee.salary = new_salary
        self.assertEqual(employee.salary, 60000.0)
    
    def test_decrease_salary(self):
        employee = Employee('Mike', 'Brown', 50000, 'Software Developer', 'Active', 'IT')
        increament = 20
        new_salary = employee.salary - (employee.salary * increament/100)
        employee.salary = new_salary
        self.assertEqual(employee.salary, 40000.0)

    def test_terminate_employement(self):
        employee = Employee('Mike', 'Brown', 50000, 'Software Developer', 'Active', 'IT')
        employee.employment_status = 'Terminated'
        self.assertEqual(employee.employment_status, 'Terminated')

    def test_start_employement(self):
        employee = Employee('Mike', 'Brown', 50000, 'Software Developer', 'Terminated', 'IT')
        employee.employment_status = 'Active'
        self.assertEqual(employee.employment_status, 'Active')
    
    def test_change_position(self):
        employee = Employee('Mike', 'Brown', 50000, 'Software Developer', 'Terminated', 'IT')
        employee.position = 'DevOps Engineer'
        self.assertEqual(employee.position, 'DevOps Engineer')
        
if __name__ == '__main__':
    unittest.main()