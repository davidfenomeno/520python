#!/usr/bin/python3

nomes = ['david','maria','pedro','sophia']

s = input('buscar por nome: ')

for nome in nomes:
    if s ==nome:
        print('esta na lista')
        break

else:
    print('nao esta na lista')