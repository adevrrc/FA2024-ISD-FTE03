from abc import ABC, abstractmethod
from datetime import date, timedelta

class Employee(ABC):
    @abstractmethod
    def __init__(self, employee_id: int):
        self.__employee_id = employee_id
        self._protected_attribute = 0

    @property
    def employee_id(self):
        return self.__employee_id

    @abstractmethod
    def calculate_pay(self):
        pass

    def __str__(self):
        return f"Employee: {self.__employee_id}"

class HourlyEmployee(Employee):
    def __init__(self, employee_id: int, hours: float, rate: float):
        super().__init__(employee_id)
        self.__hours = hours
        self.__rate = rate

    def calculate_pay(self):
        return self.__hours * self.__rate

    def __str__(self):
        return f"HourlyEmployee: {self.__hours} {self.__rate}"

class SalaryEmployee(Employee):
    def __init__(self, employee_id: int, annual_salary: float):
        super().__init__(employee_id)
        self.__annual_salary = annual_salary

    def calculate_pay(self):
        return self.__annual_salary / 26

""" class TestSalaryEmployee(unittest.TestCase):
    def test_init_initialize_object(self):
        # Arrange

        # Act
        employee = SalaryEmployee(123, 23000)

        self.assertEqual(123, employee._Employee__employee_id)
        self.assertEqual(23000, employee._SalaryEmployee__annual_salary)
        self.assertEqual(0, employee._protected_attribute) """

def pay_employee(employee: Employee):
    if not isinstance(employee, Employee):
        raise TypeError("Not an Employee.")

    pay = employee.calculate_pay()

    print(f"Employee {employee.employee_id} is payed ${pay:.2f}.")

def main():
    employee = HourlyEmployee(123, 40, 10)
    #employee = ""

    #employee = Employee(777)

    print(employee)

    #print(type(employee))
    print(isinstance(employee, HourlyEmployee))
    print(isinstance(employee, Employee))
    print(isinstance(employee, str))

    salary_employee = SalaryEmployee(345, 26000)

    pay_employee(employee)
    pay_employee(salary_employee)
    #pay_employee("hahaha I'm not an Employee")

    today = date.today()

    number_of_days_in_five_years = 5 * 365.25

    five_years = timedelta(days=number_of_days_in_five_years)

    print(five_years)

    print(today)

    five_years_ago = today - five_years

    print(five_years_ago.weekday())

if __name__ == "__main__":
    main()