import math
print('Bem vindo a Tinta Store, para saber quanto irar gastar, ')
MQ = int(input('informe quantos metros quadrados ira pintar ? : '))
LT = MQ//3
print('Irar usar %.f Litros de Tinta,' %LT)
VDT = LT / 18
VDT = int(math.ceil(VDT))
print('%.f Baldes de Tinta' %VDT)
VDT = VDT*80
print('e vai te custar R$%.2f para pintar os %.fm²' % (VDT , MQ))