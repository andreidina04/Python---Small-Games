import random

while True:
    choice = input("Roll the dice? (y/n) ").lower() # Select if you want to roll the dice (y = yes / n = no)
    if choice == 'y':
        die1 = random.randint(1,6) # Randomize a number from 1 to 6
        die2 = random.randint(1,6) # Randomize a number from 1 to 6
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing')
        break # The game closes if the player selects 'n'.
    else:
        print('Invalid input. Retry!') # If the player's selection is anything other than 'y' or 'n', the game will notify them

#Simple game of dice in Python
