#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
def alunos():
    ''
print('Media das Notas dos Alunos ')
aluno = input('Digite o nome do Aluno : ')
nota1 = float(input('Digite a primeira nota do aluno : '))
nota2 = float(input('Digite a segunda note do aluno : '))
alunos1 = [[aluno,nota1,nota2],[]]
alunos2 = []
for i in range(1, len(alunos1)):
    change = alunos1[i] - alunos1[i-1]
    alunos2.append(change)

media = (((alunos.__getitem__(1))+(alunos.__getitem__(2)))/((alunos.__len__())-1))
print(f'A média de {alunos.__getitem__(0)} é {media}')
if media == 10:
    print(f'{alunos.__getitem__(0)} Aprovado com Distinçãoo')
elif media < 7:
    print(f'{alunos.__getitem__(0)} Reprovado')
elif media >= 7:
    print(f'{alunos.__getitem__(0)} Aprovado')