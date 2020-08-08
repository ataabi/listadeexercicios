# Faça um Programa que converta metros para centímetros.
print('Transformando Metros em Centimetros')
m = float(input('Quantos Metros : '))
c = m*100
print('%.0f Metros equivale a %.0f Centimetros '% (m, c))

print('Calcuro da Area de um circulo com base no raio')
r = float(input('Raio do circulo : '))
p = 3.14
a = p*r**2
print('A aréa do circulo é : %.3f ' %a)

print('Calculo da area de um quadrado e o seu dobro')
q = float(input('Are do quadrado : '))
respq = q**2
respq2 = respq*2
print('A Area do quadrado é %.0f e o dobro é %.0f' %(respq, respq2))
