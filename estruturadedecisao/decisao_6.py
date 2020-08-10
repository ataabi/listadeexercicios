#Faça um Programa que leia três números e mostre o maior deles.

def numeromaior(n1,n2,n3):
    ""
print('Digite 3 Numeros')
n1 = float(input('Nº1 : '))
n2 = float(input('Nº2 : '))
n3 = float(input('Nº3 : '))
numeros = [n1,n2,n3]
numeros = sorted(numeros)
print(f'{numeros}')
print(f'O menor numero é {numeros.__getitem__(0)}')
print(f'O maior numero é {numeros.__getitem__(2)}')