print('Teste de Import')
print('Digite 1 para Analize de Numeros')
print('Digite 2 para Escolha de Genero')
escolha = input(':? ')
if escolha == 1:
    from estruturadedecisao.decisao_1 import AnaNumerica
elif escolha == 2:
    from estruturadedecisao.decisao_2 import escolhadegenero

