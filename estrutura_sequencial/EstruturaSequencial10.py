import math
print('Bem Vindo a Loga de Tintas Virtual')
print('Por favor informe quantos metros quadrados você irar pintar')
MQ = float(input(':'))
L18 = int(MQ/6)
L03 = int(MQ/6)
print('Você tera que comprar %.fl de Tinta' %L18)
L18 = math.ceil(L18)
G18 = L18/18
L03 = math.ceil(L03)
G03 = L03/3.6
if G18 < 1:
    G18 = 1
elif G03 < 1:
    G03 = 1

print('%.i Galoes de 18l' %G18)
print('%.i Galoes de 3,6l' %G03)