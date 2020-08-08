# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante
print('Verificação de Letras')
letra =  input('Digite uma letra: ')
vogal = ['a','A','b','B',"c",'C','d','D','e','E','i','I','y','Y','u','U']
if letra in vogal:
    print('A letra digitada é uma Vogal')
else:
    print('A letra digitada é uma consoante')