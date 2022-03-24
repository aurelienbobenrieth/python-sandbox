# Tic-Tac-Toe simplifié sans interface graphique

# Pour pouvoir utiliser area dans nos futures fonctions,
# on devra utilisé le mot clé "global"
area = None

# Ici on stockera si c'est au joueur 1 ou 2 de jouer
player = 1

# On prépare des variables pour stocker le coup du joueur à un instant T
playedLine = None
playedColumn = None

def initarea():
    global area
    area = [["*" for x in range(3)] for y in range(3)]

def readcoord():
    global player

    # Pour ne pas complexifier la chose, ici on admet que l'utilisateur
    # ne rentrera jamais de valeur vide (sinon vous pouvez tester cela
    # déclenche une erreur
    line = int(input(f'Joueur {player}: Entrez la ligne (0, 1, ou 2)'))
    column = int(input(f'Joueur {player}: Entrez la colonne (0, 1, ou 2)'))

    while not checkcoord(line, column):
        print('Les valeurs entrées ne sont pas valides')
        line, column = readcoord()

    return line, column

def checkcoord(line, column):
    # On vérifie que x et y ne sortent pas du tableau
    if column >= 3 or line >= 3 or column < 0 or line < 0:
        outOfArea = True
    else:
        outOfArea = False

    # Mais on doit aussi vérifier qu'un jouer n'essaie pas de jouer
    # par dessus un précédent coup
    if not outOfArea and area[line][column] != '*':
        alreadyTaken = True
    else:
        alreadyTaken = False

    # On retourne vrai si on est pas en dehors de l'area
    # ou si la place n'est pas déjà prise
    return not(outOfArea or alreadyTaken)

def getplayersymbol():
    if player == 1:
        return 'O'
    else:
        return 'X'

def applycoord(line, column):
    global area
    global player

    symbol = getplayersymbol()

    area[line][column] = symbol

def checkifgameiswon():
    global area
    global player
    global playedLine
    global playedColumn

    # On va prendre le coup que le joueur vient de jouer et on va
    # tester si cela crée une victoire de manière horizontale,
    # verticale ou diagonale
    return checkhoriz(playedLine, playedColumn) or checkvert(playedLine, playedColumn) or checkdiag(playedLine, playedColumn)

# On teste si à partir de la case sélectionnée on a 3 éléments alignés horizontalement
def checkhoriz(line, column):
    global area
    # Si on est à la première case on regarde les deux d'après
    if column == 0:
        return area[line][column + 1] == getplayersymbol() and area[line][column + 2] == getplayersymbol()
    # Si on est à la dernière case on regarde les deux d'avant
    elif column == 2:
        return area[line][column - 1] == getplayersymbol() and area[line][column - 2] == getplayersymbol()
    # Sinon (on est au milieu on regarde avant et après)
    else:
        return area[line][column - 1] == getplayersymbol() and area[line][column + 1] == getplayersymbol()

# On teste si à partir de la case sélectionnée on a 3 éléments alignés verticalement
def checkvert(line, column):
    global area
    # Si on est à la première case on regarde les deux d'après
    if line == 0:
        return area[line + 1][column] == getplayersymbol() and area[line + 2][column] == getplayersymbol()
    # Si on est à la dernière case on regarde les deux d'avant
    elif line == 2:
        return area[line - 1][column] == getplayersymbol() and area[line - 2][column] == getplayersymbol()
    # Sinon (on est au milieu on regarde avant et après)
    # Sinon (on est au milieu on regarde avant et après)
    else:
        return area[line - 1][column] == getplayersymbol() and area[line + 1][column] == getplayersymbol()

# On teste si à partir de la case sélectionnée on a 3 éléments alignés diagonalement
def checkdiag(line, column):
    # Si on est en [0, 0], ou [1, 1] ou [2, 2] on teste la diagonale d'en haut à gauche à en bas à droite
    if (line == 0 and column == 0) or (line == 1 and column == 1) or (line == 2 and column == 2):
        return area[0][0] == getplayersymbol() and area[1][1] == getplayersymbol() and area[2][2] == getplayersymbol()
    # Si on est en [2, 0] ou [1, 1] ou [0, 2] on teste la diagonale d'en bas à gauche à en haut à droite
    if (line == 2 and column == 0) or (line == 1 and column == 1) or (line == 0 and column == 2):
        return area[2][0] == getplayersymbol() and area[1][1] == getplayersymbol() and area[0][2] == getplayersymbol()

def checkifareaisfull():
    global area

    for i in range(len(area)):
        for j in range(len(area[i])):
            # Si on trouve au moins une étoile c'est que la partie peut continuer
            if area[i][j] == '*':
                return False

    return False

def replay():
    replay = input('Souhaitez-vous rejouer (oui ou non) ?')

    while replay != 'oui' and replay != 'non':
        replay = input('Je n\'ai pas compris, souhaitez-vous rejouer (oui ou non) ?')

    if replay == 'oui':
        return True
    else:
        return False

def play():
    global playedLine
    global playedColumn

    playedLine, playedColumn = readcoord()

    # Si nos coordonnées sont valides on passe à la suite
    applycoord(playedLine, playedColumn)

    displayarea()

def changeplayer():
    global player

    # On change le joueur
    if player == 1:
        player = 2
    else:
        player = 1

# On utilise cette fonction pour afficher chaque sous tableau
# l'un en dessous de l'autre, sinon l'expérience de jeu de
# l'utilisateur va être compliquée
def displayarea():
    global area

    for i in range(len(area)):
        print(area[i])

def launchgame():
    global player

    initarea()

    # On affiche une première fois un terrain vide
    print('C\'est parti !')
    displayarea()

    play()

    # Tant qu'un joueur n'a pas gagné OU que le tableau n'est pas rempli
    while not checkifgameiswon() and not checkifareaisfull():
        changeplayer()
        play()

    if checkifgameiswon():
        if player == 1:
            print('Le joueur 1 a gagné !')
        else:
            print('Le joueur 2 a gagné !')
    else:
        print('Aucune joueur n\'a gagné...')

    if replay():
        print('__________')
        launchgame()

# Init
launchgame()