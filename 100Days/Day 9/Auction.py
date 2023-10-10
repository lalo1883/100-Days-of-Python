
from replit import clear

list_of_biders = [

]

def addBidder(name, bid):
    dict = {}
    dict['Name'] = name
    dict['Bid'] = bid
    list_of_biders.append(dict)


def find_higher_bidder():
    higher_bid = 0
    highest_bidder = None
    for i in list_of_biders:
        bid = i['Bid']
        if bid > higher_bid:
            higher_bid = bid
            highest_bidder = i['Name']
    print(f'La mayor cantidad fue {higher_bid}')
    print(f'El ganador de la apuesta fue: {highest_bidder}')


a = True
while a:
    new_bidder = input('Agregar nuevo bidder SI, NO: ').lower()
    if new_bidder == 'si':
        clear()
        nombre = input('Escribe el nombre: ')
        bid = input('Escribe la cantidad: ')
        bid = int(bid)
        addBidder(nombre, bid)
    else:
        find_higher_bidder()
        a = False


