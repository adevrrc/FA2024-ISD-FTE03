from student.student_decoratable import StudentDecoratable

class StudentDecorator(StudentDecoratable):
    def __init__(self, student: StudentDecoratable):
        self.__student = student

    @property
    def grade_point_average(self) -> float:
        return self.__student.grade_point_average