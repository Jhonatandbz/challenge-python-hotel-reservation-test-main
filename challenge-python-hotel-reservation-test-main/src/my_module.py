'''
Não sabia se podia criar outros scripts, então resolvi fazer o código inteiro aqui,
caso eu soubesse que pode, teria feito um para a class Hotel separadamente.
Caso deseje, o usuário pode executar esse script no terminal (python my_module.py "tipo_do_cliente: data1, data2, data3, ..., dataN")
'''

import sys

class Hotel:
    def __init__(self, name, rate:int, costWeek, costWeekend):
        self.name = name
        self.rate = rate
        self.costWeek = costWeek
        self.costWeekend = costWeekend

    def value(self, client, days:list):
        price = 0
        for day in days:
            if('sun' in day or 'sat' in day):
                price = price + self.costWeekend[client]
            else:
                price = price + self.costWeek[client]

        return price



def get_cheapest_hotel(number):   #DO NOT change the function's name
    cheapest_hotel = "Not find"

    request = number.lower().replace(":", ",").split(",")   #Tratar os dados de entrada

    bestPrice = {'cost': 0, 'hotel': 0}

    for calc in range(len(hotels)):

        price = hotels[calc].value(request[0], request[1:])

        if price < bestPrice['cost'] or bestPrice['cost']==0: 
            bestPrice['cost'] = price
            bestPrice['hotel'] = calc

        elif price == bestPrice['cost']: 
            if hotels[calc].rate > hotels[bestPrice['hotel']].rate:   
                bestPrice['hotel'] = calc
                
    cheapest_hotel = hotels[bestPrice['hotel']].name
    return cheapest_hotel


hotels = []

lakewood = Hotel('Lakewood', 3, {'regular':110, 'rewards':80}, {'regular':90, 'rewards':80})
bridgewood = Hotel('Bridgewood', 4, {'regular':160, 'rewards':110}, {'regular':60, 'rewards':50})
ridgewood = Hotel('Ridgewood', 5, {'regular':220, 'rewards':100}, {'regular':150, 'rewards':40})

hotels.extend([lakewood, bridgewood, ridgewood])

if len(sys.argv)>1: print(get_cheapest_hotel(sys.argv.pop())) #verifica se tem alguma entrada do usuário
