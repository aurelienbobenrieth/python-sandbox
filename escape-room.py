# Escape room simplifié sans interface graphique

# Pour pouvoir utiliser area dans nos futures fonctions,
# on devra utilisé le mot clé "global"
area = None
obstacleArea = None

playerPosLine = 0
playerPosColumn = 0

maxLine = None
maxColumn = None

obstacle1Line = None
obstacle1Column = None

obstacle2Line = None
obstacle2Column = None

def checkmindimensions(numberLine, numberColumn):
    if numberLine < 4 or numberColumn < 4:
        return False
    else:
        return True

def readdimensions():
    numberline = int(input('Entrez le nombre de lignes (min 4)'))
    numbercolumn = int(input('Entrez le nombre de colonnes (min 4)'))

    while not checkmindimensions(numberline, numbercolumn):
        print('Les dimensions minimum ne sont pas respectées (min 4x4)')
        numberline, numbercolumn = readdimensions()

    return numberline, numbercolumn

def checkobstaclecoord(obstacleline, obstaclecolumn):
    global maxLine
    global maxColumn

    if (
        obstacleline < 0
        or obstacleline >= maxLine
        or obstaclecolumn < 0
        or obstaclecolumn >= maxColumn
        or (
            obstacleline == 0
            and obstaclecolumn == 0
        )
    ):
        return False
    else:
        return True

def readobstaclecoord(i):
    obstacleline = int(input(f'Entrez la ligne de l\'obstacle: {i}'))
    obstaclecolumn = int(input(f'Entrez la colonne de l\'obstacle: {i}'))

    while not checkobstaclecoord(obstacleline, obstaclecolumn):
        print('La position entrée n\'est pas valide')
        obstacleline, obstaclecolumn = readobstaclecoord(i)

    return obstacleline, obstaclecolumn

def savemaxdimensions(line, column):
    global maxLine
    global maxColumn

    maxLine = line
    maxColumn = column

def initareas(numberLine, numberColumn, obstacle1Line, obstacle1Column, obstacle2Line, obstacle2Column):
    global area
    global obstacleArea

    area = [["*" for x in range(numberColumn)] for y in range(numberLine)]

    obstacleArea = [["*" for x in range(numberColumn)] for y in range(numberLine)]
    obstacleArea[obstacle1Line][obstacle1Column] = "O"
    obstacleArea[obstacle2Line][obstacle2Column] = "O"

def initplayerpos():
    global area
    area[0][0] = 'P'

def displayArea():
    global area
    global obstacleArea

    displayedarea = area.copy()

    for i in range(len(displayedarea)):
        for j in range(len(displayedarea[i])):
            if obstacleArea[i][j] == 'O' and area[i][j] == 'P':
                displayedarea[i][j] = 'X'
            elif obstacleArea[i][j] == 'O':
                displayedarea[i][j] = 'O'

    for i in range(len(displayedarea)):
        print(area[i])

def readdirection():
    direction = int(input('Entrez votre direction, 2: en bas, 4: à gauche, 8: en haut, 6: à droite'))
    return direction

def checkdirection(direction):
    if direction != 8 and direction != 6 and direction != 2 and direction != 4:
        return False
    else:
        return True

def playeroutofarea(playerPosLine, playerPosColumn):
    global maxLine
    global maxColumn

    if playerPosLine >= maxLine or playerPosLine < 0 or playerPosColumn >= maxColumn or playerPosColumn < 0:
        return True
    else:
        return False

def playerinobstacle(playerPosLine, playerPosColumn):
    global obstacleArea

    if obstacleArea[playerPosLine][playerPosColumn] == '*':
        return False
    else:
        return True

def checkifgameiswon():
    global playerPosLine
    global playerPosColumn

    return playeroutofarea(playerPosLine, playerPosColumn)

def checkfifgameislost():
    global playerPosLine
    global playerPosColumn

    return playerinobstacle(playerPosLine, playerPosColumn)

def moveplayer(direction):
    global playerPosLine
    global playerPosColumn

    # Supprimer la position précédente
    area[playerPosLine][playerPosColumn] = '*'

    match direction:
        case 2:
            playerPosLine += 1
        case 4:
            playerPosColumn -= 1
        case 8:
            playerPosLine -= 1
        case 6:
            playerPosColumn += 1

    # Apliquer la nouvelle position si on est pas en dehors du tableau
    if not playeroutofarea(playerPosLine, playerPosColumn):
        area[playerPosLine][playerPosColumn] = 'P'

def play():
    direction = readdirection()
    while not checkdirection(direction):
        print('Entrez une direction valide, 2: en bas, 4: à gauche, 8: en haut, 6: à droite')
        direction = readdirection()

    moveplayer(direction)
    displayArea()

def replay():
    replay = input('Souhaitez-vous rejouer (oui ou non) ?')

    while replay != 'oui' and replay != 'non':
        replay = input('Je n\'ai pas compris, souhaitez-vous rejouer (oui ou non) ?')

    if replay == 'oui':
        return True
    else:
        return False


def launchgame():
    numberLine, numberColumn = readdimensions()
    savemaxdimensions(numberLine, numberColumn)

    obstacle1Line, obstacle1Column = readobstaclecoord(1)
    obstacle2Line, obstacle2Column = readobstaclecoord(2)

    initareas(numberLine, numberColumn, obstacle1Line, obstacle1Column, obstacle2Line, obstacle2Column)
    initplayerpos()

    print('C\'est parti')
    displayArea()

    while not (checkifgameiswon() or checkfifgameislost()):
        play()

    if (checkifgameiswon()):
        print('Vous avez gagné !')
    else:
        print('Vous avez perdu !')

    if replay():
        print('__________')
        launchgame()


launchgame()
