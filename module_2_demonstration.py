from student.student import Student
from department.department import Department
from course.course import Course
from course.lecture_course import LectureCourse
from course.lab_course import LabCourse

def main():
    # Given students populated into a list.
    students = []
    student_number = 1000

    for i in range(10):
        name = "Student" + str(i)
        student_number += 1
        try:
            student = Student(student_number, name, Department.COMPUTER_SCIENCE)
            students.append(student)
        except ValueError as e:
            print(e)

    # 1. Create an instance of the Course class with valid inputs.
    # If an exception occurs, print the exception instance.
    # Comment out once tested.
    """ try:
        # Valid
        course = Course("ISD", Department.COMPUTER_SCIENCE, 90, 35, 33)

        # Capacity not int
        #course = Course("ISD", Department.COMPUTER_SCIENCE, 90, "35", 33)

        # Enrollment not int
        #course = Course("ISD", Department.COMPUTER_SCIENCE, 90, 35, "33")
    except Exception as error:
        print(error) """

    # 2. Define a Lecture Course with a capacity of 20 and a current enrollment of 19
    # Use any valid values for the other parameters.
    # print the object
    try:
        lecture_course = LectureCourse("ISD", Department.COMPUTER_SCIENCE, 90, 20, 19, "Lecture Hall 1")

        # Invalid lecture hall
        #lecture_course = LectureCourse("ISD", Department.COMPUTER_SCIENCE, 90, 20, 19, "")

        print(lecture_course)

        """ confirmation = course.enroll_student(Student(123, "Damien Altenburg", Department.COMPUTER_SCIENCE))
        print(confirmation)

        confirmation = course.enroll_student(Student(234, "Kenny Omega", Department.COMPUTER_SCIENCE))
        print(confirmation)

        confirmation = course.enroll_student(Student(345, "Chris Jericho", Department.COMPUTER_SCIENCE))
        print(confirmation) """
    except Exception as error:
        print(error)

    # 3. Define a Lab Course with a capacity of 20 and a current enrollment of 8
    # Use any valid values for the other parameters.
    # print the object.
    try:
        lab_course = LabCourse("ISD", Department.COMPUTER_SCIENCE, 90, 20, 8, "Laptop")

        print(lab_course)

        lab_course = LabCourse("ISD", Department.COMPUTER_SCIENCE, 90, 20, 8, "")

        print(lab_course)

        """ confirmation = course.enroll_student(Student(123, "Damien Altenburg", Department.COMPUTER_SCIENCE))
        print(confirmation)

        confirmation = course.enroll_student(Student(234, "Kenny Omega", Department.COMPUTER_SCIENCE))
        print(confirmation)

        confirmation = course.enroll_student(Student(345, "Chris Jericho", Department.COMPUTER_SCIENCE))
        print(confirmation) """
    except Exception as error:
        print(error)

    # 4. Using a loop, enroll the students from the students list above
    # into the lecture course defined above.  Print the message returned
    # from the enroll_student method.
    for student in students:
        confirmation = lecture_course.enroll_student(student)
        print(confirmation)

    # 5. Using a loop, enroll the students from the students list above
    # into the lab course defined above.  Print hte message returned from
    # the enroll_student method.
    for student in students:
        confirmation = lab_course.enroll_student(student)
        print(confirmation)

if __name__ == "__main__":
    main()
