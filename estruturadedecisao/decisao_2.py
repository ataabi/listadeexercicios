# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

class escolhadegenero:
    print()
print('Verificação de Genero')
print('Digite "M" para Homens, e "F" para Mulheres')
gen = input(': ')

if gen == 'M'or  gen == 'm':
    print('Você Escolheu Masculino')
elif gen == 'F' or  gen =='f':
    print('Você escolheu Feminino')
else:
    print('Sexo indefinido')