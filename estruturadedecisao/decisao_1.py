# Faça um Programa que peça dois números e imprima o maior deles.
from builtins import ValueError
class AnaNumerica:
    def numeromaior(self):
        print()
print('Digite dois numeros para saber qual é o maior')
print('________________________________________________________')
N2 = 0
while N2 == 0:
    try:
        N1 = float(input('Primeiro Numero : '))
        N2 = float(input('Segundo Numero : '))
        print('')
    except ValueError:
            print('Digite um numero Valido')
if N1 < N2:
    Maior = N2
    print('O Maior Numero é o 2º com %.f' %Maior)
    if Maior >= 0:
        print('Esse é um numero positivo')
    else:
        print('Esse é um numero negativo')
else:
    Maior = N1
    print('O Maior Numero é o 1º com %.f' %Maior)
    if Maior >= 0:
        print('Esse é um numero positivo')
    else:
        print('Esse é um numero negativo')
pass