import art
import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
choice = 'y'

while choice == 'y':
    player_cards = []
    computer_cards = []
    choice = input("Do you want to play blackjack? y or n: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == 'y':
        print(art.logo)

        for i in range(2):
            player_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        if sum(player_cards) > 21:
            player_cards[0] = 1

        if sum(computer_cards) > 21:
            computer_cards[0] = 1

        if sum(player_cards) == 21:
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("Congratulations you got a blackjack, you win!")
            continue
        elif sum(computer_cards) == 21:
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("The dealer got a blackjack, you lose.")
            continue

        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        hit_check = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        while hit_check == 'y':
            player_cards.append(random.choice(cards))
            if 11 in player_cards and sum(player_cards) > 21:
                player_cards[player_cards.index(11)] = 1

            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")

            if sum(player_cards) < 21:
                hit_check = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            else:
                hit_check = 'n'

        while sum(computer_cards) < 17 and sum(player_cards) < 21:
            computer_cards.append(random.choice(cards))
            if 11 in computer_cards and sum(computer_cards) > 21:
                computer_cards[computer_cards.index(11)] = 1

        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
