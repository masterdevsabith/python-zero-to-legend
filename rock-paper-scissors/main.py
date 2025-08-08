human_score = 0
system_score = 0

items = ['rock', 'paper', 'scissors']

number_of_rounds = input(
    "number of rounds needed (only odd number of rounds) :")

if int(number_of_rounds) % 2 == 0:
    print("not odd")


while int(number_of_rounds) >= 1 and number_of_rounds.isnumeric() and int(number_of_rounds) % 2 != 0:
    print("HI")
