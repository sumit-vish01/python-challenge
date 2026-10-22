# print("Hello world")

# import sys

# print(sys.version)

# print("python is fun!"); print("really"); print("bye bye")

# print("hello world", end=" ")
# print("I will print on the same line.")

# name = input("enter your name:", end=" ")
# print("how are you and what about you?")

# print("i am", 35, "years old")
# print("sumit", 89, "my age name")
# print("how is your day", 2000220, "today is my day")


# name = input("Enter the name of the game:")
# print("how are u ", name)

# age = input("enter the age : ")
# print("what was your age", age)

# gender = input("Enter the gender: ")
# print("what was your age", gender)

# newname = input("Enter the newname: ")
# print("what was your older name", newname)

# x = "python"
# y = "is"
# z = "awsome"
# print(x + y + z)

# x = "awsome"

# def myfunc():
#     print("Python is " + x)

# myfunc()

# x = "awsome"

# def myfunc():
#     x = "Fantastic"
#     print("python is " + x)


# myfunc()

# print("python is "+ x)

# a = "Hello world!"
# print(a[1])

import random

attempts = 7

def display_rules():
    print("Welcome to number gussing !\n")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.\n")


def play_game(number, attempts=1):
    if attempts > attempts:
        print("\nGame over!")
        print("The correct number was:", number)
        return

    guess = input(f"Attempts {attempts}/7 - enter your guess: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a vlid number.\n")
        return play_game(number, attempt)

    if guess < 1 or guess > 100:
        print("please enter a number between 1 and 100.\n")
        return play_game(number, attempt)

    check_guess = lambda x, y: "correct" if x == y else(
        "low" if x < y else "high"
    )
    result = check_guess(guess, number)

    if result == "correct":
        print("\nCongratulatiions! You guessed the correct number!")
        print("You guessed it in", attempt, "attempt(s).")
        return

    if result == "correct":
        print("\nCongratulations! YOu guessed the correct number!")
        print("YOu guessed it in", attempt, "attempt(s).")
        