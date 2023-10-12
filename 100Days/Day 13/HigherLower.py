from Data import data
import random


def get_account_details(ac1, ac2):
    account1_name = ac1['name']
    account2_name = ac2['name']
    a = ac1['follower_count']
    b = ac2['follower_count']
    print(f'Option A ---- {account1_name}, {a}')
    print(f'Option B ---- {account2_name}, {b}')


def right_answer(acc1, acc2, counter):
    get_account_details(acc1, acc2)
    option = input('Who do you think that has more followers?: A | B: ').lower()
    if option == 'a' and acc1['follower_count'] > acc2['follower_count']:
        print('Right answer')
        counter += 1
    elif option == 'b' and acc1['follower_count'] < acc2['follower_count']:
        print('Right answer')
        counter += 1
    else:
        print('Wrong answer')
        print(f'Total points: {counter}')
        return False, counter

    new_account1 = random.choice(data)
    new_account2 = random.choice(data)
    return right_answer(new_account1, new_account2, counter)


account1 = random.choice(data)
account2 = random.choice(data)
counter = 0

while True:
    result, counter = right_answer(account1, account2, counter)
    if not result:
        break
