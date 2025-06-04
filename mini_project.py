import sys # For sys.exit()

class Department:
    """Represents a single academic department with its name and fees."""
    def __init__(self, name: str, fees: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Department name cannot be empty.")
        if not isinstance(fees, (int, float)) or fees < 0:
            raise ValueError("Fees must be a non-negative number.")
        self.name = name
        self.fees = fees

    def display_info(self):
        """Prints the department's welcome message and fees."""
        print(f"\nWelcome to {self.name}!")
        print(f"Fees for {self.name}: Rs. {self.fees}")


class College:
    """Represents the college, holding its name and available departments."""
    COLLEGE_NAME = "SGM College Karad" # Class attribute for college name

    def __init__(self, departments: dict[int, Department]):
        """
        Initializes the College with a dictionary of Department objects.
        The keys (int) serve as selection numbers for the user.
        """
        if not isinstance(departments, dict) or not departments:
            raise ValueError("College must be initialized with a dictionary of departments.")
        self.departments = departments

    def display_welcome(self):
        """Prints the college welcome message and lists available departments."""
        print(f"\n===== Welcome to {College.COLLEGE_NAME} =====")
        print("\nAvailable Departments:")
        for num, dept in self.departments.items():
            print(f"  {num}. {dept.name.replace('Welcome in ', '')}") # Clean up welcome string for listing


class Student:
    """Represents a prospective student, including their SSC marks and eligibility."""
    def __init__(self, name: str = "Prospective Student"):
        self.name = name
        self.ssc_marks = 0
        self.is_eligible_by_marks = False

    def check_ssc_eligibility(self, min_marks: int = 70) -> bool:
        """
        Prompts the student for SSC marks and determines eligibility.
        Returns True if eligible, False otherwise.
        """
        print(f"\n--- {self.name}, Check Your Marks Eligibility ---")
        try:
            marks_input = input("Enter Your SSC Marks (out of 100): ")
            M = int(marks_input)
            self.ssc_marks = M

            if M >= min_marks:
                print(f"Congratulations! With {M} marks, you are eligible for admission based on marks.")
                self.is_eligible_by_marks = True
                return True
            else:
                print(f"Sorry, your marks ({M}) are below the minimum ({min_marks}) for direct admission. Please check other criteria or consider other options.")
                self.is_eligible_by_marks = False
                return False
        except ValueError:
            print(f"Invalid input: '{marks_input}'. Please enter a whole number for marks.")
            self.is_eligible_by_marks = False
            return False


def main():
    """Main function to run the college admission application."""

    # 1. Define Departments and their Fees
    # Using a dictionary for easy lookup by selection number
    college_departments = {
        1: Department("Arts Department", 1800),
        2: Department("Commerce Department", 5500),
        3: Department("Science Department", 14000)
    }

    # 2. Create College Instance
    # The College now contains a structured collection of Department objects
    sgm_college = College(college_departments)

    # 3. Create a Student Instance
    current_student = Student("Applicant") # You could prompt for student's name here

    # 4. Perform Eligibility Check
    if current_student.check_ssc_eligibility(min_marks=70): # Pass min_marks as an argument
        sgm_college.display_welcome() # Display college welcome and departments

        while True: # Loop until valid department choice
            try:
                dep_choice = int(input("\nEnter department choice (1 for Art, 2 for Commerce, 3 for Science): "))
                if dep_choice in sgm_college.departments:
                    selected_dept = sgm_college.departments[dep_choice]
                    selected_dept.display_info()
                    break # Exit loop on valid choice
                else:
                    print("Invalid department choice. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number corresponding to the department choice.")
    else:
        print("\nAdmission process ended due to eligibility criteria not met.")
        # Optionally exit the program gracefully if not eligible
        # sys.exit(0) # Requires 'import sys' at the top


# This ensures main() runs only when the script is executed directly
if __name__ == "__main__":
    main()