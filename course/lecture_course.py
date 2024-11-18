"""The module defines the Course class."""

__version__ = "11.2024"
__author__ = "Damien Altenburg"

from course.course import Course
from department.department import Department
from student.student import Student
import math

class LectureCourse(Course):
    """Represents a course delivered with lectures."""

    def __init__(self, name: str, department: Department, credit_hours: int,
                 capacity: int, current_enrollment: int, lecture_hall: str):
        """Initializes a new instance of the LectureCourse class.

        Args:
            name (str): The name of the course.
            department (Department): The department the course is 
            delivered.
            credit_hours (int): The number of credit hours.
            capacity (int): The number of students that may enroll in 
            the course.
            current_enrollment (int): The number of students currently 
            in the course.
            lecture_hall (str): The name of the lecture hall in which 
            the course will be delivered.

        Raises:
            ValueError: Raised when the name contains no non-whitespace 
                characters, the credit_credit hours is less than or 
                equal to zero, the capacity or current_enrollment is not
                an integer value, or the lecture_hall is contains no 
                non-whitespace characters. TypeError: Raised when the 
                department or credit_hours is not the expected type.
        """
        super().__init__(name, department, credit_hours, capacity, current_enrollment)

        if len(lecture_hall.strip()) == 0:
            raise ValueError("Lecture Hall cannot be blank.")

        self.__lecture_hall = lecture_hall

    def enroll_student(self, student: Student) -> str:
        """Enrolls a student into this course.

        Args:
            student (Student): The student to be enrolled into this 
            course.

        Returns:
            Returns a confirmation message indicating the enrollment 
            status.
        """
        confirmation_message = (
            f"{student.name} has NOT been enrolled in "
            f"lecture: {self.name} due to insufficient capacity."
        )

        # There is a 10% threshold on capacity
        maximum_capacity = math.floor(self._capacity + 1.1)

        if self._current_enrollment < maximum_capacity:
            self._current_enrollment += 1

            confirmation_message = \
                f"{student.name} has been successfully enrolled in {self.name}."

        return confirmation_message

    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string 
        representation of the object.

        Returns:
            The "informal" or nicely printable string representation of 
            the object.
        """
        return super().__str__() + f"\nLecture Hall: {self.__lecture_hall}"
