"""The module contains a program for demonstrating module 4 concepts.
"""

__version__ = "11.2024"
__author__ = "Damien Altenburg"

from user_interface.student_listing import StudentListing
from user_interface.grade_point_average_calculator import GradePointAverageCalculator

# GIVEN:
from PySide6.QtWidgets import QApplication

# GIVEN:
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = StudentListing()
    mainWindow.show()
    sys.exit(app.exec())
