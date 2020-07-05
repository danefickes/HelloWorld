secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You Win!!")
        break
    elif guess_count >= guess_limit:
        print('GAME OVER')
        continue_game = input('Would you like to continue (y/n)? ')
        if continue_game.lower() == 'y':
            guess_count = 0
            continue
        if continue_game.lower() == "n":
            print('bye bye')
