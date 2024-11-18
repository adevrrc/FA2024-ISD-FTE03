"""The module contains a program for demonstrating module 3 concepts.
"""

__version__ = "11.2024"
__author__ = "Damien Altenburg"

from student.student import Student
from department.department import Department
from course import *
from patterns.singleton.singleton_student_manager import SingletonStudentManager
from student.volunteer_decorator import VolunteerDecorator
from student.council_decorator import CouncilDecorator

def main():
    student_manager = SingletonStudentManager()

    print(student_manager)
    print(type(student_manager))
    print(id(student_manager))

    obj = SingletonStudentManager()

    print(id(obj))

    # Given students populated into a list.
    students = []

    students.append(Student("John Brunelle", Department.MEDICINE))
    students.append(Student("Elizabeth Sinclair", Department.COMPUTER_SCIENCE))
    students.append(Student("Angela Brock", Department.EDUCATION))
    students.append(Student("Robert Flammand", Department.MEDICINE))
    students.append(Student("Arthur Armstrong", Department.COMPUTER_SCIENCE))
    students.append(Student("Chris Mullin", Department.EDUCATION))
    students.append(Student("Jackie Blanchard", Department.MEDICINE))
    students.append(Student("George Shanahan", Department.COMPUTER_SCIENCE))
    students.append(Student("Linda Eck", Department.EDUCATION))
    students.append(Student("Judy Gardener", Department.MEDICINE))
    students.append(Student("Donna Smith", Department.COMPUTER_SCIENCE))
    students.append(Student("Eric Best", Department.EDUCATION))

    for student in students:
        print(f"\n{str(student)}")

        ### DECORATOR ###
    student = students[0]

    print(student.grade_point_average)

    student = VolunteerDecorator(student)

    print(student.grade_point_average)

    student = CouncilDecorator(student)

    print(student.grade_point_average)

if __name__ == "__main__":
    main()
