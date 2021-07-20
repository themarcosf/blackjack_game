import random

def players():
    numPlayers = int(input('Qual o número de jogadores?: '))
    for i in range(numPlayers):
        aux = input(f'Digite o nome do jogador {i+1}: ')
        initialPlayers.append(aux)
        initialPoints.append(0)
    return initialPlayers, initialPoints

# Supoe que as cartas sejam devolvidas para o baralho após serem retiradas
def deck():
    deck = ['Ás',2,3,4,5,6,7,8,9,10,'Valete','Dama','Rei']
    aux = random.randint(0,12)
    return deck[aux]

# Função hand só deve ser chamada enquanto houver jogadores ativos
def hand(cluster):
    decision = input(f'{cluster[0]}, você deseja comprar uma carta? [sim ou não]: ')
    if decision == 'sim':
        card, newPoints = draw()
        totalPoints = cluster[1] + newPoints
        print(f'A carta sorteada foi {card}. A sua pontuação anterior era de {cluster[1]} pontos e seu total agora é de {totalPoints} pontos.')
        return newPoints
    elif decision == 'não':
        return 0

def draw():
    card = deck()
    if card == 'Ás':
        points = 1
    elif card == 'Valete' or card == 'Dama' or card == 'Rei':
        points = 10
    else:
        points = card
    return [card, points]

def verifier():
    for idx, cluster in enumerate(game_start_status):
        newPoints = hand(cluster)
        if newPoints != 0:
            totalPoints = game_start_status[idx][1] + newPoints
            if totalPoints < 21:
                initialPoints.remove(cluster[1])
                initialPoints.insert(idx, totalPoints)
            else:
                newCluster = (cluster[0], totalPoints)
                game_end_status.append(newCluster)
                initialPlayers.remove(cluster[0])
                initialPoints.remove(cluster[1])
        elif newPoints == 0:
            game_end_status.append(cluster)
            initialPlayers.remove(cluster[0])
            initialPoints.remove(cluster[1])

initialPlayers = []
initialPoints = []
game_end_status = []

players()
game_start_status = list(zip(initialPlayers, initialPoints))
while game_start_status != []:
    verifier()
    game_start_status = list(zip(initialPlayers, initialPoints))

for i in game_end_status:
    print(f'{i[0]}: você terminou o jogo com {i[1]} pontos')
