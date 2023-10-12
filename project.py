import re
import csv

def main():
    employees = []  # List to store employee details


    print("Welcome to the Employee Management System for Upstream Creatives")
    print("This program allows you to add employees and stores the data in a CSV file.")

    while True:
        employee_details = get_employee_details(employees)  # Pass employees list to the function
        if employee_details is None:
            break
        no_employees = len(employees) + 1
        employee_id = generate_id(no_employees)
        employee_details["Employee Code"] = employee_id
        employees.append(employee_details)  # Add employee details to the list
        print(f"Employee {employee_details['Full Name']} added with ID: {employee_id}")

        write_to_csv(employees)

        print("Employee added successfully!")
        print("The employee list is also stored in a CSV file (employees.csv) and can be accessed.")


    # Print all employees' details
    print("\nList of Employees:")
    for employee in employees:
        print(f"Full Name: {employee['Full Name']}")
        print(f"Email: {employee['Email']}")
        print(f"Employee Code: {employee['Employee Code']}")
        print("-" * 30)  # Separator for readability


def is_duplicate_email(email, employees):
    """Check if the given email already exists in the list of employees."""
    for emp in employees:
        if emp["Email"] == email:
            return True  # Email already exists, return True
    return False  # Email is unique, return False


def validate_email(email):
    '''validates email'''
    user_email = r"\w+\.\w+@upstreamcreatives\.com$"

    if re.match(user_email,email):
        return True  # Valid email format
    else:
        return False  # Invalid email format



def generate_id(no_employees):
    ''' Generates Employee ID'''
    return f"UC{no_employees:03}"

def get_employee_details(employees):
    while True:
        employee_fname = input("Enter employee First Name (or 'quit' to exit/ view employee List): ")
        if employee_fname.lower() == 'quit':
            return None

        if not employee_fname.strip():
            print("Error⚠️: First Name cannot be blank. Please try again.")
            continue

        employee_Lname = input("Enter employee Last Name: ")
        if not employee_Lname.strip():
            print("Error⚠️: Last Name cannot be blank. Please try again.")
            continue


        print("Please use the email convention: name.surname@upstreamcreatives.com")
        email = input("Employee Email Address: ")

        if is_duplicate_email(email, employees):
            print("Error⚠️: Email/Employee already exists. Please enter a different email.")
        else:
            while not validate_email(email):
                print("Invalid email Format. Please try again.")
                email = input("Employee Email Address: ")
            #return {"Full Name": employee_name, "Email": email}
            return {"Full Name": employee_fname + " "+ employee_Lname, "Email": email}


        #employees.append({"Full Name": employee_fname + " " + employee_Lname, "Email": email})



# Function to write data to CSV file
def write_to_csv(data):
    with open("employees.csv", "w", newline="") as csvfile:
        fieldnames = ["Full Name", "Email", "Employee Code"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)



if __name__ == "__main__":
    main()
