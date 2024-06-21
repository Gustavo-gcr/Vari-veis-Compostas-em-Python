# variaveis compostas, quantos espaços vc quiser, 3 tipos de variaves compostas, tuplas, listas e dicionario
repetir=False
while not repetir:
    numero=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
    ler=int(input('Digite um numero entre 0 e 10 que você deseja que seja escrito por extenso:'))
    if ler<0 or ler>10:
        while ler<0 or ler>10:
         ler=int(input('Digite um numero VÁLIDO entre 0 e 10 que você deseja que seja escrito por extenso:'))

    print(f'Esse numero extenso fica {numero[ler]}')
    repetir=bool(input('Deseja continuar no sistema:'))
    if repetir=='sim':
        repetir=False
    else:
        repetir=True
print('\nFim do primeiro teste\n')
#---------------------------------------------------

brasileirao_2014 = (
    'Cruzeiro',
    'São Paulo',
    'Internacional',
    'Corinthians',
    'Atlético Mineiro',
    'Fluminense',
    'Grêmio',
    'Athletico Paranaense',
    'Santos',
    'Goias',
    'Palmeiras',
    'Figueirense',
    'Flamengo',
    'Coritiba',
    'Chapecoense',
    'Sport',
    'Vitória',
    'Bahia',
    'Botafogo',
    'Criciúma'
)
#Cabuleirao- Cabuloso campeao
Cabuleirao = (
    '',
    'Cruzeiro - 80 pontos',
    'São Paulo - 70 pontos',
    'Internacional - 69 pontos',
    'Corinthians - 69 pontos',
    'Atlético Mineiro - 61 pontos',
    'Fluminense - 61 pontos',
    'Grêmio - 61 pontos',
    'Athletico Paranaense - 57 pontos',
    'Santos - 50 pontos',
    'Goiás - 47 pontos',
    'Palmeiras - 40 pontos',
    'Figueirense - 46 pontos',
    'Flamengo - 52 pontos',
    'Coritiba - 47 pontos',
    'Chapecoense - 43 pontos',
    'Sport - 52 pontos',
    'Vitória - 38 pontos',
    'Bahia - 37 pontos',
    'Botafogo - 34 pontos',
    'Criciúma - 32 pontos'
)
sair=0

while sair!=5:
    escolha=int(input('OLA, Voltamos a 2014 para o Brasileirao!!\nEscolha oque deseja saber:\n1)Os 5 primeiros colocados.\n2)Os ultimos 4 colocados.\n3)Uma lista em ordem alfabetica\n4)As colocações do cabuloso e do atletico mineiro.\n5)Sair do programa.\n'))
    if escolha==1:
        print(Cabuleirao[1:5])
    elif escolha==2:
        print(Cabuleirao[17:])
    elif escolha==3:
        print(sorted(brasileirao_2014))
    elif escolha==4:
        print('Cruzeiro:',Cabuleirao.index('Cruzeiro - 80 pontos'))
        print('Atletico:',Cabuleirao.index('Atlético Mineiro - 61 pontos'))
        
    escolha=int(input('Obrigado, vou retornar os modulos do menu!!!\n\nEscolha oque deseja saber:\n1)Os 5 primeiros colocados.\n2)Os ultimos 4 colocados.\n3)Uma lista em ordem alfabetica\n4)As colocações do cabuloso e do atletico mineiro.\n5)Sair do programa.\n'))   
print('Fim do segundo teste')    
       