"""Cho-Han, by Al Sweigart, al@inventwithpython.com
The traditional Japanese dice game of odd-even
Tags: short, beginners, game
"""

# I need to figure out how keep keep the game going in rounds

import random
import sys

JAPANESE_NUMBERS = {1: "ICHI", 2: "NI", 3: "SAN", 4: "SHI", 5: "GO", 6: "ROKU"}

print('''Cho-Ha, by Al Al Sweigart, al@inventwithpython.com
      In this traditional Japanese dice game are rolled in a bammboo cup
      by the dealer sitting on the floorThe player must guess if the dice
      total to an odd (han) or even (cho)  number.

      ''')
purse = 50019.

while True:

    # Place your bet
    print(f"You have, {purse}. How much would you like to bet? (or QUIT)")
    while True:
        pot = input('> ')
        if pot.upper() == "QUIT":
            print("Thanks for playing")
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number: ')
        elif float(pot) > purse:
            print("You do not have enough money to make that bet!")
        else:
            # This is a valid bet
            pot = float(pot)
            break  # Leave loop once bet is placed

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The dealer swrils the cup and you hear dice rattling.")
    print('The dealer slams the cup on the floor still covering the dice,')
    print("and asks, whats your bet?")

    print('Please enter CHO (even) or HAN (odd)')

    # Let player bet cho or han
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print("Please enter CHO or HAN")
            continue
        else:
            break

    # Reveal the dice results
    print('The dealer lifts the cup to reveal:')
    print('', JAPANESE_NUMBERS[dice1], ' - ', JAPANESE_NUMBERS[dice2])
    print(f'{dice1} + {dice2}')
    total = dice1 + dice2
    print(f"the total is {total}")

    # Determine if the player won
    rollEven = total % 2 == 0
    if rollEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results
    if playerWon:
        print('You won, take the pot!')
        # purse = purse + pot
        print('The house collects a 10% fee from the pot')
        fee = pot * 0.1
        purse = purse + pot - fee
        print(f'Your purse is now {purse}')
    else:
        print('You lost!')
        purse = purse - pot
        print(f'Your purse is now {purse}')

    # check if the player is our of money
    if purse == 0:
        print("You have run out of money!")
        print('Thanks for playing')
        sys.exit()
