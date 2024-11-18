"""The module defines the GradePointAverageCalculator class."""

__version__ = "11.2024"
__author__ = "Damien Altenburg"

# GIven Imports
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Slot, Signal
from demo_superclasses.gpa_window import GPAWindow

class GradePointAverageCalculator(GPAWindow):
    """A window that allows for GradePointAverage to be calculated.
    Inherited from GPAWindow which provides the gui design.
    """

    new_gpa = Signal(str, float)
    
    def __init__(self, student_number: str, name: str):
        """Initializes the window widgets and displays received data.
        
        Args:
            student_number (str):  The student number of the student 
                being displayed.
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

        self.calculate_button.clicked.connect(self.__on_calculate_clicked)

    @Slot()
    def __enable_button(self):
        """Validates the input fields and if valid, enables the 
        Calculate button.
        """
        is_credit_hours_entered = (self.credit_edit_1.text() != ""
                                   and self.credit_edit_2.text() != ""
                                   and self.credit_edit_3.text() != "")
        
        self.calculate_button.setEnabled(is_credit_hours_entered)      

    def __on_calculate_clicked(self):
        """Calculates the grade point average based on the data 
        provided.
                
        Emits a signal with the student number and calculated gpa when 
        complete.
        """
        line_edit_widgets = [self.credit_edit_1,
                            self.credit_edit_2,
                            self.credit_edit_3
                            ]

        credit_hours = []

        for line_edit_widget in line_edit_widgets:
            try:
                credit_hour = float(line_edit_widget.text())

                credit_hours.append(credit_hour)
            except ValueError:
                QMessageBox.information(self, 
                                        "Credit Hours", 
                                        "Credit Hours must be numeric.")

                line_edit_widget.setFocus()

                # Don't do the rest of the function when there is an error
                return

        grade_select_widgets = [self.grade_select_1,
                                self.grade_select_2,
                                self.grade_select_3
                                ]
        
        grades = []

        for grade_select_widget in grade_select_widgets:
            # Look up the grade value
            grades.append(self.GRADE_LOOKUP[grade_select_widget.currentText()])

        total_grades = 0
        total_credit_hours = 0

        for grade, credit_hour in zip(grades, credit_hours):
            total_grades += grade * credit_hour
            total_credit_hours += credit_hour

        grade_point_average = 0 if total_credit_hours == 0 else total_grades / total_credit_hours

        self.grade_point_average_label.setText(f"{grade_point_average:.2f}")

        self.new_gpa.emit(self.student_number_label.text(), grade_point_average)    
