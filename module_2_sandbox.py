from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def __init__(self, employee_id: int):
        self.__employee_id = employee_id

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

def main():
    employee = HourlyEmployee(123, 40, 10)
    #employee = ""

    #employee = Employee(777)

    print(employee)

    #print(type(employee))
    print(isinstance(employee, HourlyEmployee))
    print(isinstance(employee, Employee))
    print(isinstance(employee, str))

if __name__ == "__main__":
    main()