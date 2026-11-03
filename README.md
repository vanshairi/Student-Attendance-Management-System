# Student Attendance Management System

A menu-driven Student Attendance Management System developed using **Python** and **MySQL**. The application simplifies student record management and daily attendance tracking through a command-line interface.

## Features

- **Add Students:** Register students using their roll numbers and names.
- **View Student List:** Display all registered students.
- **Update Student Details:** Modify existing student names.
- **Mark Attendance:** Record daily attendance as Present (P) or Absent (A).
- **Update Attendance:** Modify previously recorded attendance.
- **View Absentees:** Retrieve the list of students absent on a particular date.
- **Working Days:** Calculate the total number of recorded working days.
- **Attendance Percentage:** Calculate an individual student's attendance percentage.

## Technology Stack

- **Programming Language:** Python
- **Database:** MySQL
- **Database Connector:** mysql-connector-python

## Database Structure

- Database Name: `ATTENDANCE`
- Table Name: `RECORD`
- Student details and daily attendance records are maintained in MySQL.

## Prerequisites

- Python 3
- MySQL Server
- mysql-connector-python

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/vanshairi/Student-Attendance-Management-System.git
   ```

2. Install the required Python package:

   ```bash
   pip install mysql-connector-python
   ```

3. Create a MySQL database named `ATTENDANCE`.

4. Configure the MySQL connection details in the Python source code.

5. Run the application:

   ```bash
   python main.py
   ```

## Future Improvements

- Graphical user interface.
- Improved database structure.
- Advanced attendance reports.
- Enhanced authentication and data security.

## Author

**Vansh Airi**

- GitHub: https://github.com/vanshairi
- LinkedIn: https://www.linkedin.com/in/vanshairi/
