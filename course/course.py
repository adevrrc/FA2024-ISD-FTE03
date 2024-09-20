"""
Description: Defines the Course class.
Author: Damien Altenburg
"""
from department.department import Department
from student.student import Student
from abc import ABC, abstractmethod

class Course(ABC):
    """Represents a course at an educational institution.
    """

    @abstractmethod
    def __init__(self, name: str, department: Department, credit_hours: int, capacity: int, current_enrollment: int):
        """Initializes a new instance of the Course class.

        Args:
            name (str): The name of the course.
            department (Department): The department the course is delivered.
            credit_hours (int): The number of credit hours.
            capacity (int): The number of students that may enroll in the course.
            current_enrollment (int): The number of students currently in the course.

        Raises:
            ValueError: Raised when the name contains no non-whitespace characters,
                        the credit_credit hours is less than or equal to zero,
                        the capacity or current_enrollment is not an integer value.
            TypeError: Raised when the department or credit_hours is not the expected type.
        """
        if len(name.strip()) == 0:
            raise ValueError("The name cannot be blank.")

        if not isinstance(department, Department):
            raise TypeError(f"The department object must be a Department type.")

        if not isinstance(credit_hours, int):
            raise TypeError(f"The credit_hours object must be an int type.")

        if not isinstance(capacity, int):
            raise ValueError("Capacity must be numeric.")

        if not isinstance(current_enrollment, int):
            raise ValueError("Enrollment must be numeric.")

        self.__name = name
        self.__department = department
        self.__credit_hours = credit_hours
        self._capacity = capacity
        self._current_enrollment = current_enrollment

    @property
    def name(self) -> str:
        """Gets the name of the course.

        Returns:
            The name of the course.
        """
        return self.__name

    @property
    def department(self) -> Department:
        """Gets the department the course is delivered within.

        Returns:
            The faculty department the course is managed from.
        """
        return self.__department

    @property
    def credit_hours(self) -> int:
        """Gets the number of credit hours for this course.

        Returns:
            The number of instructional hours for the course.
        """
        return self.__credit_hours

    @abstractmethod
    def enroll_student(self, student: Student) -> str:
        """Enrolls a student into this course.

        Args:
            student (Student): The student to be enrolled into this course.

        Returns:
            Returns a confirmation message indicating the enrollment status.
        """
        pass

    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string representation of the object.

        Returns:
            The "informal" or nicely printable string representation of the object."""
        return (
            f"Course: {self.__name}\n"
            f"Department: {self.__department.name.replace('_', ' ').title()}\n"
            f"Credit Hours: {self.__credit_hours}"
        )
