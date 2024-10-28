# GIven Imports
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Slot, Signal

from demo_superclasses.gpa_window import GPAWindow

class GradePointAverageCalculator(GPAWindow):
    """
    A window that allows for GradePointAverage to be calculated.
    Inherited from GPAWindow which provides the gui design.
    """
    
    def __init__(self, student_number: str, name: str):
        """
        Initializes the window widgets and displays received data.
        args:
            student_number (str):  The student number of the student being displayed.
            name (str): The name of the student being displayed.
        """
        super().__init__()

        self.GRADE_LOOKUP = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0, 
                            "C+": 2.5, "C": 2, "D": 1, "F": 0}
        
        self.name_label.setText(name)
        self.student_number_label.setText(student_number)

        self.credit_edit_1.textChanged.connect(self.__enable_button)
        self.credit_edit_2.textChanged.connect(self.__enable_button)
        self.credit_edit_3.textChanged.connect(self.__enable_button)

    @Slot()
    def __enable_button(self):
        """
        Validates the input fields and if valid, enables the Calculate button.
        """
        is_credit_hours_entered = (self.credit_edit_1.text() != ""
                                   and self.credit_edit_2.text() != ""
                                   and self.credit_edit_3.text() != "")
        
        self.calculate_button.setEnabled(is_credit_hours_entered)      

    def __on_calculate_clicked(self):
        """
        Calculates the grade point average based on the data provided.
        Emits a signal with the student number and calculated gpa when complete.
        Formula: ((grade1 * cr_hours1) + (grade2 * cr_hours2) + etc) / sum(cr_hours#)
        """


