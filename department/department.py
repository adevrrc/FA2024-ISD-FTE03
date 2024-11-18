"""The module defines the Department enumeration."""

__version__ = "11.2024"
__author__ = "Damien Altenburg"

from enum import Enum, auto

class Department(Enum):
    """
    An enumeration listing each of the departments in a school.

    Example: 
        >>> Department.MEDICINE
    """
    COMPUTER_SCIENCE = auto()
    """The computer science department."""

    EDUCATION = auto()
    """The education department."""

    ENGINEERING = auto()
    """The engineering department."""
    
    MEDICINE = auto()
    """The medicine department."""
