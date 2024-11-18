"""The module defines the TestCourse class.

Usage: 
    To execute all tests in the terminal execute the following command:
    $ python -m unittest tests/test_course.py
"""

__version__ = "11.2024"
__author__ = "Damien Altenburg"

import unittest
from course.course import Course
from department.department import Department

class TestCourse(unittest.TestCase):
    """Tests for the Course class."""

    def setUp(self):
        """Setup runs AUTOMATICALLY before each test method and
        provides initial values for the class attributes.
        """
        self.course = Course("intermediate software development", Department.COMPUTER_SCIENCE, 90)

    def test_init_initializes_object(self):
        self.assertEqual("intermediate software development", self.course._Course__name)
        self.assertEqual(Department.COMPUTER_SCIENCE, self.course._Course__department)
        self.assertEqual(90, self.course._Course__credit_hours)

    def test_init_blank_name_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            course = Course("   ", Department.COMPUTER_SCIENCE, 90)

        self.assertEqual("The name cannot be blank.", str(context.exception))

    def test_init_invalid_department_raises_exception(self):
        with self.assertRaises(TypeError) as context:
            course = Course("intermediate software development", "computer science", 90)

        self.assertEqual("The department object must be a Department type.", str(context.exception))

    def test_init_invalid_credit_hours_raises_exception(self):
        with self.assertRaises(TypeError) as context:
            course = Course("intermediate software development", Department.COMPUTER_SCIENCE, 34.5)

        self.assertEqual("The credit_hours object must be an int type.", str(context.exception))

    def test_name_accessor_returns_correct_state(self):
        self.assertEqual("intermediate software development", self.course.name)

    def test_department_accessor_returns_correct_state(self):
        self.assertEqual(Department.COMPUTER_SCIENCE, self.course.department)

    def test_credit_hours_accessor_returns_correct_state(self):
        self.assertEqual(90, self.course.credit_hours)

    def test_str_returns_string_representation(self):
        expected = ("Course: Intermediate Software Development\n"
                    "Department: Computer Science\n"
                    "Credit Hours: 90")

        self.assertEqual(expected, str(self.course))
