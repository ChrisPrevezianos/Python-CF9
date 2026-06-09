class Student:
    """
    A class that represents a student with a first name and a last name.

    Attributes:
        firsname (str): The first name of the student.
        lastname (str): The last name of the student.
    """
    def __init__(self, firstname: str, lastname: str = "Papadreou"):
        """
        Initialize a Student object with the provided first name and last name.

        Args:
            firstname (str): The first name of the student.
            lastname (str): The last name of the student.
        """
        self.firstname = firstname
        self.lastname = lastname

def main():
    # Create student objects
    student = Student("Kostas")

    print(f"First name: {student.firstname}")
    print(f"Last name: {student.lastname}")

    # TODO: friends
    student.friends = ["Alice", "Bob", "Charlie"]
    print(student.friends) 

if __name__ == "__main__":
    main()
