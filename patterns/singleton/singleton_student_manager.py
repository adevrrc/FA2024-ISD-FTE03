class SingletonStudentManager:
    """A class to manage unique student numbers.
    """
    # Static (Class) Variables
    __instance = None
    __next_student_number = 2024000
    
    def __new__(cls):
        """Creates the instance of the class.

        This is a singleton class. Only one instance of this will ever be
        instantiated.

        Returns:
            SingletonStudentManager: The instance of the class.
        """
        # if not None
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    @staticmethod
    def get_instance(self):
        """Returns the instance of this class.

        Returns:
            SingletonStudentManager: The instance of the class.
        """
        return self.__instance

    def get_next_student_number(self) -> int:
        """Returns the next available student number.

        Returns:
            int: The next available student number.
        """
        current_number = self.__next_student_number

        self.__next_student_number += 1
        
        return current_number
