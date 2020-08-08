# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('Quais foram suas Notas Bimestrais :')
nbi = 1
total = 0
while nbi < 5:
    no = float(input('Qual sua Nota no %s Bimestre? ' %nbi))
    total = total + no
    nbi = nbi + 1
media = total / 4
print('Sua Media Anual é : %1.2f' % media)
