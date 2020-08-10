#Crie um programa que leia nome e duas notas de varios alunos e
#guarde tudo em uma lista composta. No final, mostre um boletim
#contendo a média de cada um e permita que o usuário possa
#mostrar as notas de casa aluno individualmente

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) /2
    if media < 7:
        status = 'Reprovado'
    if media >= 7:
        status = 'Aprovado'
    if media == 10:
        status = 'Aprovado com Distinção'
    ficha.append([nome, [nota1, nota2], media, status])
    resp = str(input('Quer continuar[S/N]'))
    if resp in 'Nn':
        break
print('-=' * 35)
print(f'{"No.":<4}{"NOME":<10}{"MÈDIA":<8}{"Status":<8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f} {a[3]:<24}')
while True:
    try:
        print('-' * 35)
        opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if opc == 999:
            print('FINALIZANDO...')
            break
        if opc <= len(ficha) - 1:
            print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}{ficha[opc][3]}')
    except: opc == str
    print('Digite o Número do Aluno e nao o nome')
print('<<< VOLTE SEMPRE >>>')