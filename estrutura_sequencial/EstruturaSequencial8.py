#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo

print('Bem vindo ao calculador de salario.')
print('Quanto voçê ganha por hora e quantas horas trabalhou esse mês ?')
Ghora = float(input('Quanto ganha por Hora :'))
Htra = float(input('Quantas horas voÇê tranalhou :'))
Sabru = Ghora*Htra
print('Seu Salario Bruto é : R$%.2f' %Sabru)
INSS = Sabru*0.08
print('Pagou ao INSS: R$%.2f' %INSS)
Sind = Sabru*0.05
print('quanto pagou ao sindicato R$%.2f' %Sind)
IR = Sabru*0.11
SAliq = Sabru - INSS - Sind - IR
print('O salario liquido R$%.2f' %SAliq)
