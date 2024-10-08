from abc import ABC, abstractmethod

class StudentDecoratable(ABC):
    """This interface imposes the ability to retrieve the grade point average
    on the objects of each class that implement it.
    """
    @abstractmethod
    def grade_point_average(self) -> float:
        """Gets the student's grade point average.

        Returns:
            float: The student's grade point average.
        """
        pass