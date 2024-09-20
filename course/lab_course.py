from course.course import Course
from department.department import Department
from student.student import Student
import math

class LabCourse(Course):
    """Represents a course delivered in a lab.
    """

    def __init__(self, name: str, department: Department, credit_hours: int,
                 capacity: int, current_enrollment: int, lab_equipment: str):
        """Initializes a new instance of the LabCourse class.

        Args:
            name (str): The name of the course.
            department (Department): The department the course is delivered.
            credit_hours (int): The number of credit hours.
            capacity (int): The number of students that may enroll in the course.
            current_enrollment (int): The number of students currently in the course.
            lab_equipment (str): The lab equipment required for the course.

        Raises:
            ValueError: Raised when the name contains no non-whitespace characters,
                        the credit_credit hours is less than or equal to zero,
                        the capacity or current_enrollment is not an integer value, or
                        the lecture_hall is contains no non-whitespace characters.
            TypeError: Raised when the department or credit_hours is not the expected type.
        """
        super().__init__(name, department, credit_hours, capacity, current_enrollment)

        if len(lab_equipment.strip()) == 0:
            lab_equipment = "None"

        self.__lab_equipment = lab_equipment

    def enroll_student(self, student: Student) -> str:
        """Enrolls a student into this course.

        Args:
            student (Student): The student to be enrolled into this course.

        Returns:
            Returns a confirmation message indicating the enrollment status.
        """
        confirmation_message = (
            f"{student.name} has NOT been enrolled in lab: "
            f"{self.name} due to insufficient capacity."
        )

        if self._current_enrollment < math.floor(self._capacity / 2):
            self._current_enrollment += 1

            confirmation_message = \
                f"{student.name} has been successfully enrolled in {self.name}."

        return confirmation_message

    def __str__(self)-> str:
        """Returns the "informal" or nicely printable string representation of the object.

        Returns:
            The "informal" or nicely printable string representation of the object."""
        return super().__str__() + f"\nLab Equipment: {self.__lab_equipment}"
