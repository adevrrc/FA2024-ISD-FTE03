from student.student_decorator import StudentDecorator

class VolunteerDecorator(StudentDecorator):
    @property
    def grade_point_average(self) -> float:
        return super().grade_point_average + .25