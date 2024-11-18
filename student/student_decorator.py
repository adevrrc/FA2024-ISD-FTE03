"""The module defines the StudentDecorator class."""

__version__ = "11.2024"
__author__ = "Damien Altenburg"

from student.student_decoratable import StudentDecoratable

class StudentDecorator(StudentDecoratable):
    """Represents the base decorator class for wrapping other Student 
    type objects.
    """
    def __init__(self, student: StudentDecoratable):
        """Initializes a new instance of the StudentDecorator class.

        Args:
            student (StudentDecoratable): The student to be decorated.
        """
        # The attribute stores a reference to the wrapped object
        self.__student = student

    @property
    def grade_point_average(self) -> float:
        """Returns the student's grade point average.

        Returns:
            float: The student's grade point average.
        """
        # Returns the grade point average of the wrapped Student.
        return self.__student.grade_point_average
