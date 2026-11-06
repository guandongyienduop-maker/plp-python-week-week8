
# ==========================================
# PERSONAL MINI-TOOLKIT
# ==========================================

import random

tasks = []

print("\nWELCOME TO PERSONAL MINI-TOOLKIT")


# TOOL 1: SIMPLE CALCULATOR
# Performs addition, subtraction, multiplication and division.

def simple_calculator():

    print("\n========== SIMPLE CALCULATOR ==========")

    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\n1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("\nChoose an operation (1-4): ")

        if operation == "1":
            print(f"\nResult: {num1 + num2}")

        elif operation == "2":
            print(f"\nResult: {num1 - num2}")

        elif operation == "3":
            print(f"\nResult: {num1 * num2}")

        elif operation == "4":
            if num2 != 0:
                print(f"\nResult: {num1 / num2}")
            else:
                print("\nCannot divide by zero.")

        else:
            print("\nInvalid operation.")

    except ValueError:
        print("\nPlease enter valid numbers.")

    print("Thank you for using the calculator!")


# TOOL 2: TO-DO LIST MANAGER
# Allows users to add, view and remove tasks.

def todo_list_manager():

    while True:

        print("\n========== TO-DO LIST MANAGER ==========")
        print("\n1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":

            task = input("\nEnter a new task: ")

            if task.strip():
                tasks.append(task)
                print(f"\nTask '{task}' added successfully!")
            else:
                print("\nTask cannot be empty.")

        elif choice == "2":

            print("\nYour Tasks:")

            if len(tasks) == 0:
                print("Your task list is empty.")

            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":

            if len(tasks) == 0:
                print("\nThere are no tasks to remove.")

            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    number = int(input("\nEnter task number to remove: "))

                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"\nTask '{removed}' removed successfully!")
                    else:
                        print("\nInvalid task number.")

                except ValueError:
                    print("\nPlease enter a valid number.")

        elif choice == "4":
            print("\nReturning to main menu...")
            break

        else:
            print("\nInvalid choice. Please select 1-4.")


# TOOL 3: NUMBER GUESSING GAME
# Allows users to guess a randomly selected number.

def number_guessing_game():

    print("\n========== NUMBER GUESSING GAME ==========")

    secret_number = random.randint(1, 10)
    attempts = 0

    print("\nGuess a number between 1 and 10!")

    while True:

        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"\nCongratulations! You guessed {secret_number}.")
                print(f"You used {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid whole number.")

    print("\nThank you for playing!")


# TOOL 4: NAME FORMATTER
# Displays names in uppercase, lowercase and title case.

def name_formatter():

    print("\n========== NAME FORMATTER ==========")

    name = input("\nEnter your full name: ").strip()

    if name:
        print("\nUppercase:", name.upper())
        print("Lowercase:", name.lower())
        print("Title case:", name.title())

    else:
        print("\nPlease enter a valid name.")

    print("\nName formatting completed!")


# MAIN MENU
# Repeats until the user chooses Quit.

while True:

    print("\n1. Simple Calculator")
    print("2. To-Do List Manager")
    print("3. Number Guessing Game")
    print("4. Name Formatter")
    print("5. Quit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        simple_calculator()

    elif choice == "2":
        todo_list_manager()

    elif choice == "3":
        number_guessing_game()

    elif choice == "4":
        name_formatter()

    elif choice == "5":
        print("\nThank you for using Personal Mini-Toolkit!")
        print("Goodbye! Have a wonderful day.")
        break

    else:
        print(f"\nSorry, '{choice}' is not a valid choice.")
        print("Please select a number between 1 and 5.")


