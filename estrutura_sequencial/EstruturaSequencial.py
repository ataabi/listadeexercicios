print('Alo Mundo')
while 1:
    try:
        n = float(input('Digite um Numero :'))
        break
    except:
        print('O Numero informado é invalido')
print('O Numero informado foi %.1f' %n)

print('Digite 2 Numeros a serem somados')
n1 = float(input(':'))
n2 = float(input(':'))
n3 = n1+n2
print('A soma dos numeros é : %.1f' %n3)

print('Notas Bimestrais :')
n1 = float(input(':'))
n2 = float(input(':'))
n3 = float(input(':'))
n4 = float(input(':'))
media = (n1+n2+n3+n4)/4
print('Sua Media Bimestral é: %1.2f' %media)



