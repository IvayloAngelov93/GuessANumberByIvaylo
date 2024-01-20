from random import randint
computer_number = randint(1, 100)
while True:
    player_input = input('Guess the number between 1 and 100: ')
    if not player_input.isdigit():
        print('Invalid input. Try again...')
        continue
    player_input = int(player_input)
    if player_input == computer_number:
        print('You guess it!')
        break
    elif player_input > computer_number:
        print('Too high!')
    else:
        print('Too low!')
