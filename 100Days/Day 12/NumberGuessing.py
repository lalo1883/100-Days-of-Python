import random

b = 1


def play(mode):
    global b
    while b < mode:
        h_choice = input('Type a number: ')
        h_choice = int(h_choice)
        if h_choice == c_choice:
            print(f'You win in {b} attempts!')
            break
        elif b == mode - 1 and h_choice != c_choice:
            print('You lost!')
            print(f'Answer {c_choice}')
            break
        elif h_choice > c_choice:
            print(f'Choose a short number!')
            b = b + 1
            print(f'Attempts: {b}')
        elif h_choice < c_choice:
            print(f'Choose a larger number!')
            b = b + 1
            print(f'Attempts: {b}')


def get_computer_choice():
    computer_choice = random.randint(1, 101)
    return computer_choice


a = True
while a:
    continue_playing = input('Do you want to play the guessing number game?: |yes| - |No|: ').lower()
    c_choice = get_computer_choice()
    # print(c_choice)
    if continue_playing == 'yes':
        b = 1
        difficult = input('What difficult you want to play: |Easy|-|Normal|-|Hard|: ').lower()
        if difficult == 'hard':
            play(6)
        elif difficult == 'normal':
            play(11)
        elif difficult == 'easy':
            play(21)
    else:
        a = False
