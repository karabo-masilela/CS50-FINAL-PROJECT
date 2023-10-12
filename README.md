# CS50 Final Project:Employee Management System for Upstream Creatives.

## Description
This Employee Management System is a simple yet powerful tool designed to streamline the employee onboarding process for Upstream Creatives. It provides an efficient way to add new employees to the system and allocate unique employee codes, ensuring each employee is easily identifiable within the organization. The system takes user input, including the employee's name, surname, and email address, following the convention: name.surname@upstreamcreatives.com.


#### Video Demo :
https://youtu.be/n36QMkKAPz8

## Features
** Employee Registration: Easily add new employees to the system by providing their name, surname, and email address. The system automatically
   generates a unique employee code following the specified convention.

** Email Validation: The application validates email addresses to ensure they adhere to the company's convention. If an invalid email format is
   entered, the system prompts the user to enter a valid one.

** Print Employee List : Returns the List of all Employees .

** User-Friendly Interface: The system provides a simple and intuitive interface, making it accessible for users with varying technical
   expertise.
** Data Persistence: Employee details are stored in a CSV file ("employees.csv") for future reference.

#### Files

**project.py: Contains the main functionality of the Employee Management System, including functions for adding employees, generating employee codes, and validating email addresses.

**test_project.py: Houses the pytest test cases for the functions implemented in project.py. These tests ensure the correctness of the system's core functionalities.

#### Design Choices
**Email Convention: The decision to enforce a specific email convention (name.surname@upstreamcreatives.com) was made to maintain consistency within the organization and simplify the email management process.

**User Feedback: The system provides clear and informative error messages, guiding users to correct any input mistakes. This design choice was made to enhance the user experience and reduce potential errors.

**Code Modularity: The code is organized into separate functions to enhance modularity and readability. Each function serves a specific purpose, making the codebase easier to maintain and debug.


#### Getting Started
To run the Employee Management System locally, follow these steps:

Clone this repository to your local machine.
Ensure you have Python installed on your system.
Run python project.py in your terminal to start the application.
Follow the on-screen prompts to add new employees and experience the system in action!

#### Dependencies
Python 3.x

## Notes
- Ensure proper email format (name.surname@upstreamcreatives.com) when entering email addresses.
- The employee list is stored in the `employees.csv` file and can be accessed at any time.

#### License
This project is licensed under the MIT License, making it open and free for anyone to use and modify.