"""The module contains a program for demonstrating module 5 concepts.
"""

__version__ = "11.2024"
__author__ = "Damien Altenburg"

# Same client code as module_4_demonstration.py, but
# containing a more user-friendly name as the exe will be
# named based on this filename.
from user_interface.student_listing import StudentListing
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = StudentListing()
    mainWindow.show()
    sys.exit(app.exec())
