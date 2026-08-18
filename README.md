# Expense Tracker

A beginner-friendly Python Expense Tracker built as part of DecodeLabs Project 2.

## Overview

The Expense Tracker is a simple Python program that allows users to enter multiple expense amounts and calculates their total spending.

This project demonstrates fundamental Python programming concepts such as user input, loops, conditional statements, input validation, exception handling, and accumulator-based calculations.

## Features

* Add multiple expenses
* Calculate total spending automatically
* Display the current total after each expense
* Count the number of expenses entered
* Prevent negative expense values
* Handle invalid user input
* Display a final expense summary
* Simple command-line interface

## Technologies Used

* Python 3
* Variables and data types
* User input and output
* While loops
* Conditional statements
* Exception handling
* Basic mathematical operations

## How It Works

1. The program starts with a total expense of 0.
2. The user enters an expense amount.
3. The program checks whether the entered value is valid.
4. The expense is added to the running total.
5. The current total is displayed.
6. The user can continue entering expenses.
7. Entering `0` ends the input process.
8. The program displays the final expense summary.

## How to Run

### Option 1: Run on Google Colab

1. Open Google Colab.
2. Create a new notebook.
3. Upload the `Expense_Tracker_Project_2.py` file.
4. Open the Python file.
5. Copy the program code into a Colab code cell.
6. Run the code.
7. Enter your expense amounts when prompted.
8. Enter `0` when you are finished.
9. The program will display your total spending.

### Option 2: Run Using Python

Make sure Python 3 is installed on your computer.

Open a terminal or command prompt in the project folder and run:

```bash
python Expense_Tracker_Project_2.py
```

The program will ask you to enter your expenses.

Example:

```text
Enter expense amount: 100
Expense added: 100.00
Current total: 100.00

Enter expense amount: 50
Expense added: 50.00
Current total: 150.00

Enter expense amount: 20
Expense added: 20.00
Current total: 170.00

Enter expense amount: 0
```

## Example Output

```text
========================================
          EXPENSE TRACKER
========================================

Enter your expenses one by one.
Enter 0 when you are finished.

Enter expense amount: 100
Expense added: 100.00
Current total: 100.00

Enter expense amount: 50
Expense added: 50.00
Current total: 150.00

Enter expense amount: 20
Expense added: 20.00
Current total: 170.00

Enter expense amount: 0

========================================
           EXPENSE SUMMARY
========================================
Number of expenses: 3
Total Spent:        170.00
========================================
Thank you for using Expense Tracker!
```

## Project Structure

```text
Expense-Tracker-Python/
│
├── Expense_Tracker_Project_2.py
└── README.md
```

## Learning Objectives

This project demonstrates the practical use of:

* Variables
* Data types
* User input
* While loops
* If statements
* Accumulators
* Exception handling
* Numerical calculations
* Input validation

## Project Information

**Project:** Expense Tracker

**Program:** Python Programming

**Project Number:** 2

**Training Program:** DecodeLabs Industrial Training Kit

## Author

Rameen
