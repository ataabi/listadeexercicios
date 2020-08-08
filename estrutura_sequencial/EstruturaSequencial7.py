print('Quantos quilos de peixe você tem ?')
peso = float(input(':'))
excesso = peso - 50
multa = excesso * 4
if excesso >= 0:
    print('O valor da multa é : R$%.f' %multa)
    print('o Peso excedente é : %.fKg' %excesso)
else :print('Nao tem Multa')




