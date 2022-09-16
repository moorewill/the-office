from collections import defaultdict
from typing import Set

from employee import Employee


class TheOffice:
    """A class representing an office that holds information about its employees and their sales.
    It exposes methods make and view sales for each employee.
    Args:
        regional_manager (str): The name of the employee.
        employees (Set[Employee]): A set of employee objects.
        location (str): The name of the region the office is located.
    """

    def __init__(self, regional_manager: str, employees: Set[Employee], location: str):
        self.regional_manager = regional_manager
        self.employees = employees
        self.location = location
        self.sales = defaultdict(int)

    def __str__(self) -> str:
        """Represents the class object as a string providing a welcome message
        and the name of the `regional_manager`.
        Returns:
            str: Welcome message including the name of the `regional_manager`.
        """
        return f"Welcome to The Office! The boss here is {self.regional_manager}."

    def record_sale(self, employee: Employee) -> None:
        """Record a salr for an employee
        Args:
            employee (Employee): The employee whose sales number we are interested in.

        """
        self.sales[employee] += 1

    def get_employee_sales(self, employee: Employee) -> int:
        """Method that returns the number of sales given an employee.

        Args:
            employee (Employee): The employee whose sales number we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """
        return self.sales[employee]

    def _fire_employee(self, employee: Employee) -> None:
        """Fires an employee, removing them from the office
        Args:
            employee (Employee): The employee whose sales number we are interested in.

        """
        self.employees.remove(employee)
