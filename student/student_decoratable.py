from abc import ABC, abstractmethod

class StudentDecoratable(ABC):
    @abstractmethod
    def grade_point_average(self) -> float:
        pass