#!/usr/bin/env python3

from random import randint


def generate_number():
    """Generates and returns 4-digit secret number as list."""
    unique_number = []
    while len(unique_number) < 4:
        candidate = str(randint(1, 9))
        if candidate not in unique_number:
            unique_number.append(candidate)
    return unique_number


def process_user_input(unique_number, attempts):
    """Process input from user.
    That is check if the input is valid number and then checks for bulls and
    cows. Exits application on 'q' press.
    """
    user_input = input(">>> ")

    if user_input == 'q':
        print("Exiting!")
        return False
    elif is_valid(user_input):
        return check_number(user_input, unique_number, attempts)
    else:
        return True


def is_valid(user_input):
    """Checks if input is valid."""
    if is_number(user_input):
        if is_correct_length(user_input):
            if is_non_repeting(user_input):
                return True
            else:
                print("Input number has repeating digits!")
                return False
        else:
            print("Input doesn't have exactly 4 digits!")
            return False
    else:
        print("Input is not a valid number!")
        return False


def is_number(user_input):
    """Returns True when input is integer."""
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def is_correct_length(user_input):
    """Returns true when input has 4 digit."""
    return len(user_input) == 4


def is_non_repeting(user_input):
    """Returns True if number doesn't have repeating digits."""
    for index, char in enumerate(user_input):
        if char in user_input[:index]+user_input[index+1:]:
            return False
    return True


def check_number(user_input, unique_number, attempts):
    """Check how many digits is correct. When all are correct program ends."""
    bulls = 0
    cows = 0
    for index, digit in enumerate(user_input):
        if digit == unique_number[index]:
            bulls += 1
        else:
            if digit in unique_number:
                cows += 1
    if bulls == 4:
        return eval_victory(attempts)
    else:
        print("%s bulls, %s cows" % (bulls, cows))
        return True


def eval_victory(num_of_tries):
    """Evaluates success of player."""
    result = ""
    if num_of_tries < 4:
        result = "amazing"
    elif num_of_tries < 11:
        result = "very good"
    elif num_of_tries < 16:
        result = "average"
    elif num_of_tries < 21:
        result = "not so good"
    else:
        result = "bad"
    print("Correct, you've guessed the right number in %s guesses!" %
          num_of_tries)
    print("That's %s!" % result)


print("Hi there!")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("Enter a number")
unique_number = generate_number()
attempts = 1

while process_user_input(unique_number, attempts):
    attempts += 1
