
import random

a = True
while a:
    new_game = input('Do you want to play a game of Blackjack? Type "y" or "n": ').lower()
    if new_game == 'y':
        blac_jack_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        user_card1 = random.choice(blac_jack_cards)
        user_card2 = random.choice(blac_jack_cards)

        computer_card1 = random.choice(blac_jack_cards)
        computer_card2 = random.choice(blac_jack_cards)

        user_cards = [user_card1, user_card2]
        user_value = sum(user_cards)

        computer_cards = [computer_card1, computer_card2]
        computer_value = sum(computer_cards)

        # Define if you lose or win and show values and cards

        if user_value == 21 and computer_value == 21:
            print('Computer wins')
            #Show cards and values
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
            break
        elif user_value == 21:
            print('You win')
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
            break
        elif computer_value == 21:
            print('You lose')
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
            break

        # Modify value of Ace
        if user_card1 and user_value > 21:
            user_card1 = 1
            user_value = sum(user_cards)
        elif user_card2 and user_value > 21:
            user_card2 = 1
            user_value = sum(user_cards)

        if computer_card1 and computer_value > 21:
            computer_card1 = 1
            computer_value = sum(computer_cards)
        elif computer_card2 and computer_value > 21:
            computer_card2 = 1
            computer_value = sum(computer_cards)

        # Reveal computer 1st card

        print(f'Your cards: {user_cards}, current score: {user_value}')
        print(f'Computer\'s first card: {computer_card1}')

        # Review if someone went over 21



        # Ask the user for another card

        b = True
        while b:
            option = input('Type \'y\' to get another card, type \'n\' to pass: ').lower()
            if option == 'y':
                user_extra_card = random.choice(blac_jack_cards)
                user_cards.append(user_extra_card)
                user_value = sum(user_cards)
                if user_value > 21:
                    print('You went over.')
                    break
                elif user_value == 21:
                    print('You won!')
                    break
                else:
                    print(f'Your cards: {user_cards}, current score: {user_value}')
                    print(f'Computer\'s first card: {computer_card1}')
            else:
                b = False

        if computer_value <= 16:
            computer_extra_card = random.choice(blac_jack_cards)
            computer_cards.append(computer_extra_card)
            computer_value = sum(computer_cards)
            if computer_value > 21:
                print('Computer went over. You win')
                # print(f'Your cards: {user_cards}, current score: {user_value}')
                # print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
                break

        if user_value == 21 and computer_value == 21:
            print('Computer wins')
            #Show cards and values
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
        elif user_value == 21:
            print('You win')
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
        elif computer_value == 21:
            print('You lose')
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
        elif computer_value > 21:
            print('You Win')
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
        elif user_value > 21:
            print('You lose')
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
        elif computer_value < user_value:
            print('You win')
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
        elif user_value < 21:
            print('You lose')
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
        elif computer_value == user_value:
            print('It a draw')
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')
        elif computer_value and user_value > 21:
            print('It a draw you both went over')
            print(f'Your cards: {user_cards}, current score: {user_value}')
            print(f'Computer\'s cards: {computer_cards}, current score: {computer_value}')

    else:
        a = False

