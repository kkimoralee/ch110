#Kimora Lee
#04-27-24
#P5HW
#Use of loops, functions and module import to complete assignments
#I have to psecdocode
print("Welcome to Math Quiz")
print("")

#random number generator code
import random
#asking for 2 random numbers to be generated at one time
def generate_numbers():
    return random.randint(1, 500), random.randint(1, 500)

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2
#displays the number of attempts 
def quiz(operation):
    num1, num2 = generate_numbers()
    attempts = 0
   
    if operation == '1':
        answer = add_numbers(num1, num2)
        print(f"  {num1}\n+ {num2}")
        print()
        print("Enter answer.")
    elif operation == '2':
        answer = subtract_numbers(num1, num2)
        print(f"  {num1} - {num2}")
        print()
        print("Enter answer.")
    while True:
        user_answer = int(input())
        attempts += 1
       #displays if the answer you entered is low, high or perfect
        #also shows how many guesses it took you
        if user_answer == answer:
            print(f"Congratulations!!!! The answer is correct.")
            print("Number of guesses:" ,attempts)
            break
        elif user_answer < answer:
            print("Sorry, guess is too low.")
            print()
            print("Try again:", end =" ")
        else:
            print("Sorry, guess is too high.")
            print()
            print("Try again:", end =" ")

def main_menu():
    while True:
        print("\nMAIN MENU\n" +
              "-------------------\n" +
              "1. Adding Random Numbers\n" +
              "2. Subtracting Random Numbers\n" +
              "3. Exit")
        print("")
        choice = input("Please choose one of the menu options: ")
       #gives you 3 options, either try again or exit to break the loop
        if choice in ['1', '2']:
            quiz(choice)
        elif choice == '3':
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# The main_menu function will be called to start the program
main_menu()
