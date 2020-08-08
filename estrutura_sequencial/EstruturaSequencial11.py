def tempo_download (Temposeg):
    while 1:
    print('Quanto tempo levara seu download ?')
arquivo = float(input('Diga qual o tamanho do arquivo que ira baixar ?'))
net = float(input('Qual a Velocidade de sua conexão'))
TempoSeg = arquivo/(net/8)
TempoSeg = TempoSeg/60
print('%.2f Minutos' %TempoSeg)