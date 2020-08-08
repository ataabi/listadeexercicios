print('Temperatura em Farenheit para Celsius')
F = float(input('Graus em Farenheit : '))
C = (5*(F-32)/9)
print('A temperatura é %.1fC°' %C)

print('Temperatura em Celsius  para Farenheit')
C = float(input('Graus em Celsius : '))
F = (C*9/5)+32
print('A temperatura é %.1fF°' %F)

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

print('Calculo do Salario mensal')
hora = float(input('Horas Trabalhadas : '))
gh = float(input ('Ganho por hora : '))
resu = hora*gh
print('Voce deve recever R$%.2f este mes' %resu)
