class Employee:
    def __init__(self, first_name, last_name, salary, position, status, department):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.position = position
        self.employment_status = status
        self.department = department
    
    def show_details(self):
        print('First Name: ', self.first_name)
        print('Last Name: ', self.last_name)
        print('Salary: ', self.salary)
        print('Position: ', self.position)
        print('Employment Status: ', self.employment_status)
        print('Department: ', self.department)
    
    def increase_salary(self, increament):
        new_salary = (self.salary * increament/100) + self.salary
        self.salary = new_salary
    
    def decrease_salary(self, decrement):
        new_salary = self.salary - (self.salary * decrement/100)
        self.salary = new_salary

    def terminate_employment(self):
        self.employment_status = 'Terminated'
    
    def start_employment(self):
        self.employment_status = 'Active'

    def change_department(self, department):
        self.department = department

    def change_position(self, position):
        self.position = position

if __name__ == '__main__':
    new_employee_one = Employee('Mike', 'Brown', 50000, 'Software Developer', 'Active', 'IT')
    new_employee_one.increase_salary(20)
    new_employee_one.start_employment()
    new_employee_one.change_department('DevOps')
    new_employee_one.show_details()