import random
import sys


iteration = 0


number_of_rounds = input(
    "number of rounds needed (only odd number of rounds) :")

if not number_of_rounds.isnumeric():
    print("type a numeric value")
    sys.exit()


number_of_rounds = int(number_of_rounds)


if number_of_rounds < 1:
    print("it should be atleast 1")
    sys.exit()
if number_of_rounds % 2 == 0:
    print("not odd")
    sys.exit()


items = ['rock', 'paper', 'scissors']
human_score = 0
system_score = 0
winner = ""


def picking_an_item():
    global human_score
    global system_score
    global iteration
    user_input = input("your choose (ROCK/PAPER/SCISSORS) : ").strip().lower()
    system_input = random.choice(items)

    if user_input not in ('rock', 'paper', 'scissors'):
        iteration -= 1
        print("CHOOSE ANYTHING B/W ROCK | PAPER | SCISSORS")
    elif user_input == system_input:
        iteration -= 1
    elif user_input == 'rock' and system_input == 'paper':
        system_score += 1
    elif user_input == 'paper' and system_input == 'scissors':
        system_score += 1
    elif user_input == 'scissors' and system_input == 'rock':
        system_score += 1

    elif user_input == 'rock' and system_input == 'scissors':
        human_score += 1
    elif user_input == 'paper' and system_input == 'rock':
        human_score += 1
    elif user_input == 'scissors' and system_input == 'paper':
        human_score += 1

    print(f'you : {user_input} | system  : {system_input}')


if number_of_rounds >= 1:

    while iteration < number_of_rounds:
        picking_an_item()
        iteration += 1

    if human_score > system_score:
        winner = 'You WON the game'
    elif human_score < system_score:
        winner = 'System WON the game'
    else:
        winner = "TIE TIE"

    print(f'''
            YOUR SCORE : {human_score}
            SYSTEM SCORE : {system_score}
            WINNER : {winner}
        ''')

    # do_you_want_to_play_again = input(
    #     "do you want to play again ? : (Yes/No)").strip().lower()
    # if do_you_want_to_play_again == 'yes':
    #     iteration = 0
    # else:
    #     pass
