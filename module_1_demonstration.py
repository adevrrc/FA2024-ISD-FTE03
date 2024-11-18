"""The module contains a program for demonstrating module 1 concepts.
"""

__version__ = "11.2024"
__author__ = "Damien Altenburg"

# 1. Import as necessary.
from course.course import Course
from department.department import Department

def main():
    # 1. Create an instance of the Course class with valid inputs.
    #    Print the instance.
    #    If an exception occurs, print the exception instance.
    try:
        course = Course("COMP-2327 Intermediate Software Development", Department.COMPUTER_SCIENCE, 90)

        print(course)
        # Output: <course.course.Course object at 0x000001805BDAFC50>

        #print(course.__name)
        # Output: 'Course' object has no attribute '__name'
    except Exception as error:
        print(error)

    # 2. Create an instance of the Course class with invalid inputs.
    # Print the instance.
    # If an exception occurs, print the exception instance.
    try:
        # Quick check name
        # with whitespace
        #course = Course("   ", Department.COMPUTER_SCIENCE, 90)

        # with no characters
        #course = Course("", Department.COMPUTER_SCIENCE, 90)

        # Quick check department
        # with a float
        #course = Course("Intermediate Software Development", 45.6, 90)

        # Quick check credit hours
        # with a string
        course = Course("Intermediate Software Development", Department.COMPUTER_SCIENCE, "90")

        print(course)
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()
