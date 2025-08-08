import random
import math

max_number = 20
min_number = 1
system_input = random.randint(min_number, max_number)
total_guesses = 3


while total_guesses > 0:
    try:
        user_input = int(
            input(f"guess the number (you have {total_guesses} chance left ): ").strip())
        total_guesses -= 1

        if user_input > max_number or user_input < min_number:
            print(f'Enter a number between {min_number} and {max_number}')
            total_guesses += 1
        elif user_input == system_input:
            print('correct')
            break
        elif abs(user_input-system_input) <= 5:
            print('close')

        elif user_input > system_input:
            print("too high")
        elif user_input < system_input:
            print('too low')
    except ValueError:
        print("enter a number NOT A STRING")


if total_guesses == 0 and user_input != system_input:
    print('out of guesses')
