#!/usr/bin/env python3

from random import randint


def generate_number():
    unique_number = []
    while len(unique_number) < 4:
        candidate = str(randint(1, 9))
        if candidate not in unique_number:
            unique_number.append(candidate)
    return unique_number


def check_number(user_input, unique_number, attempts):
    bulls = 0
    cows = 0
    for index, digit in enumerate(user_input):
        if digit == unique_number[index]:
            bulls += 1
        else:
            if digit in unique_number:
                cows += 1
    if bulls == 4:
        print("Congratulation you win! It took you %s tries." % attempts)
        return False
    else:
        print("%s bulls, %s cows" % (bulls, cows))
        return True


def is_number(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def is_valid(user_input):
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


def is_correct_length(user_input):
    return len(user_input) == 4


def is_non_repeting(user_input):
    for index, char in enumerate(user_input):
        if char in user_input[:index]+user_input[index+1:]:
            return False
    return True


def process_user_input(unique_number, attempts):
    user_input = input(">>> ")
    if is_valid(user_input):
        return check_number(user_input, unique_number, attempts)
    else:
        if user_input == 'q':
            print("Exiting!")
            return False
        else:
            return True


print("Hi there!")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("Enter a number")
unique_number = generate_number()
attempts = 1

while process_user_input(unique_number, attempts):
    attempts += 1
