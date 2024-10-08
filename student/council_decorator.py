from student.student_decorator import StudentDecorator

class CouncilDecorator(StudentDecorator):
    @property
    def grade_point_average(self) -> float:
        grade_point_average = super().grade_point_average

        increases = {
            4.13: .35,
            3.67: .19,
            2.4: .04
        }

        increase = 0

        for average in increases:
            if grade_point_average > average:
                increase = increases[average]
                break

        return grade_point_average + increase