from random import randint
def print_green(skk): print("\033[92m {}\033[00m" .format(skk))
def print_red(skk): print("\033[91m {}\033[00m" .format(skk))
def print_yellow(skk): print("\033[93m {}\033[00m" .format(skk))
def print_light_purple(skk): print("\033[94m {}\033[00m" .format(skk))

computer_number = randint(1, 100)

while True:
    player_input = input('Guess the number between 1 and 100: ')
    if not player_input.isdigit():
        print_green('Invalid input. Try again...')
        continue
    player_input = int(player_input)
    if player_input == computer_number:
        print_red('You guess it!')
        break
    elif player_input > computer_number:
        print_yellow('Too high!')
    else:
        print_light_purple('Too low!')
