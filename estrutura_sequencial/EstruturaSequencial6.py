print('Medidando seu peso ideal usando sua altura como base.')
print('Qual sua Altura ?')
while 1:
    try:
        altura = input(':')
        altp = float(altura)
        pesoh = (72.7*altp) - 58
        pesom = (62.1*altp) - 44.7
        print()
        print('Se for Homen, Digite (h)')
        print('Se for Mulher, Digite (m)')
        print('Você é ?')
        genero = input(':')
        if genero == 'h':
            print('Seu peso ideal é : %.2f' %pesoh)
            break
        elif genero == 'm':
            print('Seu peso ideia é : %.2f' % pesom)
            break
        else:
           print()
    except:
        print('Comando invalido, Tente novamente')
        continue