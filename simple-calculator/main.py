import sys


def add_two_numbers(a, b):
    return a+b


def subtract_two_numbers(a, b):
    return a-b


def multiply_two_numbers(a, b):
    return a*b


def divide_two_numbers(a, b):
    return a/b


while True:
    first_number = input("enter first number: ")
    second_number = input("enter second number: ")
    operation_needed = input("enter operation needed (+, -, *, /): ")

    if not first_number.isnumeric():
        print("please enter a number")
        sys.exit()

    if not second_number.isnumeric():
        print("please enter a number")
        sys.exit()

    if operation_needed not in ('+', '-', '*', '/'):
        print("please enter a valid operation !!!")
        sys.exit()

    first_number = int(first_number)
    second_number = int(second_number)

    if operation_needed == '+':
        print(add_two_numbers(first_number, second_number))
    elif operation_needed == '-':
        print(subtract_two_numbers(first_number, second_number))
    elif operation_needed == '*':
        print(multiply_two_numbers(first_number, second_number))
    elif operation_needed == '/':
        print(divide_two_numbers(first_number, second_number))
