# ==============================
# LEVEL 1 TASKS
# ==============================

# Task 1: String Reversal
def reverse_string(s):
    return s[::-1]

# Task 2: Temperature Conversion
def temp_convert(temp, unit):
    if unit == "C":
        return (temp * 9/5) + 32
    elif unit == "F":
        return (temp - 32) * 5/9

# Task 3: Email Validator
def check_email(email):
    return "@" in email and "." in email

# Task 4: Calculator
def calculator(a, b, op):
    if op == "+": return a + b
    elif op == "-": return a - b
    elif op == "*": return a * b
    elif op == "/": return a / b
    elif op == "%": return a % b

# Task 5: Palindrome Checker
def palindrome(s):
    return s == s[::-1]


# ==============================
# LEVEL 2 TASKS
# ==============================

import random

# Task: Guessing Game
def guessing_game():
    number = random.randint(1, 100)
    while True:
        guess = int(input("Guess number: "))
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print("Correct!")
            break


# Task: Password Checker
import re

def password_check(password):
    if (len(password) >= 8 and
        re.search("[A-Z]", password) and
        re.search("[a-z]", password) and
        re.search("[0-9]", password)):
        return "Strong"
    else:
        return "Weak"


# ==============================
# MAIN MENU (optional but best)
# ==============================

print("Choose Task:")
print("1. Reverse String")
print("2. Temperature Convert")
print("3. Email Check")
print("4. Calculator")
print("5. Palindrome")

choice = input("Enter choice: ")

if choice == "1":
    print(reverse_string(input("Enter string: ")))

elif choice == "2":
    t = float(input("Temp: "))
    u = input("Unit C/F: ")
    print(temp_convert(t, u))

elif choice == "3":
    print(check_email(input("Email: ")))

elif choice == "4":
    a = float(input("A: "))
    b = float(input("B: "))
    op = input("Operator: ")
    print(calculator(a, b, op))

elif choice == "5":
    print(palindrome(input("Enter string: ")))