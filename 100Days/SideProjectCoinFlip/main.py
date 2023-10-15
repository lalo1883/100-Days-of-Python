

import time

import random


def drop_coin():
    lista = []
    for i in range(1, 11):
        coin = random.randint(0, 1)
        lista.append(coin)
    total_value = sum(lista)
    print(f'Lista: {lista} \n suma: {total_value}')
    return total_value


b = 0
a = True
while a:
    if drop_coin() != 10:
        b += 1
        print(f'Try number: {b}')
        # time.sleep(.5)

    else:
        print(f'total tries: {b}')
        a = False