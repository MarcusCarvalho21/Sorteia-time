import random

qtdJogadores = int(input('Informe o número de jogadores por time.\n'))
jogadores = []

for n in range(qtdJogadores*2):
    nomeJogador = input("Informeo o nome do "+str(n+1)+"º jogador: \n")
    jogadores.append(nomeJogador)

print('\n\n')
time1 = random.sample(jogadores,5)
time2 = []

for n in range(qtdJogadores*2):
    if not time1.__contains__(jogadores[n]):
        time2.append(jogadores[n])

print(' TIME 1')
for n in range(qtdJogadores):
    print(time1[n])
print(' TIME 2')
for n in range(qtdJogadores):
    print(time2[n])