import random
    # Coder un morpion

    # Séparateur uniquement esthétique


def Separateur(): 
    print("            __________________________\n")

    # Creation d'une grille 

def initialiser_grille(taille_grille : int) -> list:
    '''
    La fonction initialiser_grille renvoie une grille de type list en fonction de la taille donnée en paramètre.
    '''
    assert isinstance(taille_grille, int), "Cela doit être un entier"
    assert taille_grille >= 1, "Vous ne pouvez pas utilisé une grille de inférieur à 1 case"

    grille = [[" " for ligne in range(taille_grille)] for colonne in range(taille_grille)]

    assert isinstance(grille, list)
    return grille

    # Afficher la grille

def affiche_grille(grille : list ,taille_grille : int):
    '''
    La fonction affiche_grille affiche une jolie grille de morpion en fonction d'une grille et de sa taille.
    '''
    numero_ligne = 0
    for i in range(taille_grille):
        print("  ",i,end="")
    print("")
    for ligne in grille:
        print("",taille_grille*"  - ")
        print(numero_ligne,end="")
        numero_ligne += 1
        for element in ligne:
            print("|",element,end=" ")
        print("|")

    # Vérifier si la case choisie est libre

def est_Libre(ligne : int , colonne : int ,grille : list) -> bool :
    '''
    La fonction est_Libre revoie un booléen True si la case est libre sinon elle renvoie False.
    '''
    if(grille[ligne][colonne]) == " ":
        return True
    return False

    # Vérifier si la grille est pleine

def grille_Pleine(grille : list,taille_grille : int) -> bool:
    '''
    La fonction grille_Pleine renvoie un booléen True si la grille est remplie sinon elle renvoie False.
    '''
    for ligne in range(taille_grille):
        for colonne in range(taille_grille):
            if(grille[ligne][colonne]) == " ":
                return False
    return True

    # Placer un symbole

def placer_symbole(symbole : str,ligne : int,colonne : int,grille : list):
    '''
    La fonction placer_symbole place le symbole défini a l'endroit indiquer en fonction de sa ligne et de sa colonne.
    '''
    grille[ligne][colonne] = symbole
    return ""
    
    # Tester si un coup est gagnant

def coup_Gagnant(symbole : str,ligne : int,colonne : int,grille : list) -> bool:
    '''
    La fonction coup_Gagnant renvoie un booléen True si un meme symbole est aligné en ligne, en colonne ou en diagonale au nombre de la taille de la grille.
    Elle teste chaque cas d'alignement.

    Entrée
    ----------
    Un symbole de type string
    Une ligne de type int
    Une colonne de type int
    Une grille de type list

    Sortie
    ---------
    Un booléen de type bool
    '''

    for ligne in grille:    # Cas où une ligne est alignée
        if ligne == [symbole for i in range(TAILLE_GRILLE)]:
            return True
        
    for colonne in range(TAILLE_GRILLE):    # Cas où une colonne est alignée
        tab = []
        for k in grille:
            tab.append(k[colonne])
        if tab == [symbole for i in range(TAILLE_GRILLE)]:
            return True
        
    nb_symbole= 0      # Cas où une diagonale est alignée
    for i in range(1,TAILLE_GRILLE+1):
        case1 = grille[TAILLE_GRILLE-i][TAILLE_GRILLE-i]
        if case1 == symbole:
            nb_symbole += 1
        if nb_symbole == TAILLE_GRILLE:
            return True
        
    nb_symbole= 0
    for i in range(TAILLE_GRILLE):
        case2 = grille[TAILLE_GRILLE-1-i][0+i]
        if case2 == symbole:
            nb_symbole += 1
        if nb_symbole == TAILLE_GRILLE:
            return True
    
    return False

    # Création d'une IA

jouer = []
def mouvement_ia(grille):
    angle = [(0,0),(TAILLE_GRILLE-1,0),(TAILLE_GRILLE-1,TAILLE_GRILLE-1),(0,TAILLE_GRILLE-1)]
    angle = random.choice(angle)
    mouvements_possibles = [(i, j) for i in range(TAILLE_GRILLE) for j in range(TAILLE_GRILLE) if grille[i][j] == " "]
    mouvement = random.choice(mouvements_possibles)
    nb_jeu = 0

    if TAILLE_GRILLE == 3:     # L'IA est "intelligente" sur une grille de 3x3 sinon elle joue aléatoirement
        if nb_jeu == 0:
            for i in range(TAILLE_GRILLE):      # Joue le symbole pour gagner la ligne
                nb_symbole = 0
                for j in range(TAILLE_GRILLE):
                    if grille[i][j] == "O":
                        nb_symbole += 1
                    if nb_symbole == 2:
                        for x in range(TAILLE_GRILLE):
                            if grille[i][x] == " ":
                                grille[i][x] = "O"
                                nb_jeu = 1
                            

        
        if nb_jeu == 0:
            for i in range(TAILLE_GRILLE):      # Joue le symbole pour gagner la colonne
                nb_symbole = 0
                for j in range(TAILLE_GRILLE):
                    if grille[j][i] == "O":
                        nb_symbole += 1
                    if nb_symbole == 2:
                        for x in range(TAILLE_GRILLE):
                            if grille[x][i] == " ":
                                grille[x][i] = "O"
                                nb_jeu = 1
        
        if nb_jeu == 0:    
            for i in range(TAILLE_GRILLE):      # Joue le symbole pour bloquer la ligne
                nb_symbole = 0
                for j in range(TAILLE_GRILLE):
                    if grille[i][j] == "X":
                        nb_symbole += 1
                    if nb_symbole == 2:
                        for x in range(TAILLE_GRILLE):
                            if grille[i][x] == " ":
                                grille[i][x] = "O"
                                nb_jeu = 1

        if nb_jeu == 0:
            for i in range(TAILLE_GRILLE):      # Joue le symbole pour bloquer la colonne
                nb_symbole = 0
                for j in range(TAILLE_GRILLE):
                    if grille[j][i] == "X":
                        nb_symbole += 1
                    if nb_symbole == 2:
                        for x in range(TAILLE_GRILLE):
                            if grille[x][i] == " ":
                                grille[x][i] = "O"
                                nb_jeu = 1

        if nb_jeu == 0:
            nb_symbole = 0      # Joue le symbole pour bloquer la diagonale
            for i in range(1,TAILLE_GRILLE+1):
                if grille[TAILLE_GRILLE-i][TAILLE_GRILLE-i] == "X":
                    nb_symbole += 1
                if nb_symbole == 2:
                    for j in range(1,TAILLE_GRILLE+1):
                        if grille[TAILLE_GRILLE-j][TAILLE_GRILLE-j] == " ":
                            grille[TAILLE_GRILLE-j][TAILLE_GRILLE-j] = "O"
                            nb_jeu = 1

        if nb_jeu == 0:
            nb_symbole = 0      # Joue le symbole pour bloquer la diagonale
            for i in range(TAILLE_GRILLE):
                if grille[TAILLE_GRILLE-1-i][0+i] == "X":
                    nb_symbole += 1
                if nb_symbole == 2:
                    for j in range(TAILLE_GRILLE):
                        if grille[TAILLE_GRILLE-1-j][0+j] == " ":
                            grille[TAILLE_GRILLE-1-j][0+j] = "O"
                            nb_jeu = 1

        if nb_jeu == 0:
            nb_symbole = 0      # Joue le symbole pour gagner la diagonale
            for i in range(1,TAILLE_GRILLE+1):
                if grille[TAILLE_GRILLE-i][TAILLE_GRILLE-i] == "O":
                    nb_symbole += 1
                if nb_symbole == 2:
                    for j in range(1,TAILLE_GRILLE+1):
                        if grille[TAILLE_GRILLE-j][TAILLE_GRILLE-j] == " ":
                            grille[TAILLE_GRILLE-j][TAILLE_GRILLE-j] = "O"
                            nb_jeu = 1

        if nb_jeu == 0:
            nb_symbole = 0      # Joue le symbole pour gagner la diagonale
            for i in range(TAILLE_GRILLE):
                if grille[TAILLE_GRILLE-1-i][0+i] == "O":
                    nb_symbole += 1
                if nb_symbole == 2:
                    for j in range(TAILLE_GRILLE):
                        if grille[TAILLE_GRILLE-1-j][0+j] == " ":
                            grille[TAILLE_GRILLE-1-j][0+j] = "O"
                            nb_jeu = 1
            
                                

        if grille[angle[0]][angle[1]] == " " and grille[1][1] != " " and nb_jeu == 0:    # Prend un angle aléatoire si le milieu est pris
            grille[angle[0]][angle[1]] = "O"
            jouer.append((angle[0],angle[1]))

        elif grille[1][1] == " " and nb_jeu == 0:   # Prend le milieu
            jouer.append((1,1))
            grille[1][1] = "O"

        elif nb_jeu == 0:
            jouer.append(mouvement)     # Joue aléatoirement
            grille[mouvement[0]][mouvement[1]] = "O"
    
    else:
        jouer.append(mouvement)     # Joue aléatoirement
        grille[mouvement[0]][mouvement[1]] = "O"

    return ""

    ##################### Debut du jeu #####################
    
Rejouer = "O"
nb_point_J1 = 0
nb_point_J2 = 0

print("\n"*100)
Separateur()
print("         Bienvenue dans le jeu du morpion !")
Separateur()

TAILLE_GRILLE = int(input("Entrez la taille de la grille sur laquelle vous souhaitez jouer : "))
Joueur1 = {"prenom" : "", "symbole" : "X", "point" : nb_point_J1 }
Joueur2 = {"prenom" : "", "symbole" : "O", "point" : nb_point_J2 }
Separateur()
JEU = int(input("Entrez le nombre de joueur, (1) ou (2) : "))
assert JEU == 1 or JEU == 2, "Choississez entre 1 ou 2 !"
Separateur()

if JEU == 1:        ########### Jeu avec 1 joueur ! ###########
    Joueur1['prenom'] = input("Entrez le prénom du joueur 1 : ")
    assert Joueur1["prenom"] != 'IA', "Tu ne peux pas jouer l'IA !!"
    Joueur2['prenom'] = "IA"

else:   ########### Jeu avec deux joueur ! ###########
    Joueur1['prenom'] = input("Entrez le prénom du joueur 1 : ")
    assert Joueur1["prenom"] != 'IA', "Tu ne peux pas jouer l'IA !!"
    Separateur()
    Joueur2['prenom'] = input("Entrez le prénom du joueur 2 : ")
    assert Joueur2["prenom"] != 'IA', "Tu ne peux pas jouer l'IA !!"
    Separateur()
    print("",Joueur1['prenom'],"tu joueras les X \n",
        Joueur2['prenom'],"tu joueras les O \n",
        "Un joueur va être tiré au sort")
Separateur()
ligne,colonne = 0, 0

while Rejouer == "O":
    GRILLE = initialiser_grille(TAILLE_GRILLE)
    JoueurActuel = random.choice([Joueur1, Joueur2])

    while grille_Pleine(GRILLE,TAILLE_GRILLE) == False and coup_Gagnant(JoueurActuel['symbole'],ligne,colonne,GRILLE) == False :
        if JoueurActuel["prenom"] == "IA":
            mouvement_ia(GRILLE)
            if coup_Gagnant(JoueurActuel['symbole'],ligne,colonne,GRILLE) == True:
                affiche_grille(GRILLE,TAILLE_GRILLE)
                Separateur()
                print(JoueurActuel['prenom'], ", tu as gagné !")

            elif grille_Pleine(GRILLE,TAILLE_GRILLE) == True:
                affiche_grille(GRILLE, TAILLE_GRILLE)
                Separateur()
                print("Égalité !")

            else:
                if JoueurActuel == Joueur1:
                    JoueurActuel = Joueur2
                else:
                    JoueurActuel = Joueur1
        else:

            print(JoueurActuel['prenom']," à ton tour !\n")
            ligne = -1
            colonne = -1
            affiche_grille(GRILLE,TAILLE_GRILLE)

            while ligne == -1:
                ligne = int(input("Quelle ligne souhaite-tu jouer ? "))
                if ligne not in [c for c in range(TAILLE_GRILLE)]:
                    print("Cette ligne n'est pas existante!")
                    ligne = -1
                else:
                    
                    while colonne == -1:
                        colonne = int(input("Quelle colonne souhaite-tu jouer ? "))
                        if colonne not in [c for c in range(TAILLE_GRILLE)]:
                            print("Cette colonne n'est pas existante!")
                            colonne = -1
                        else :
                            if est_Libre(ligne, colonne,GRILLE) == False:
                                print("Cette case est déjà remplie !")
                                ligne = -1
                                colonne = -1
                            else:
                                placer_symbole(JoueurActuel['symbole'], ligne, colonne,GRILLE)
                                Separateur()
                                
            if coup_Gagnant(JoueurActuel['symbole'],ligne,colonne,GRILLE) == True:
                affiche_grille(GRILLE,TAILLE_GRILLE)
                Separateur()
                print(JoueurActuel['prenom'], ", tu as gagné ! Tu es a ", JoueurActuel["point"] + 1, " vitoire(s)")

            elif grille_Pleine(GRILLE,TAILLE_GRILLE) == True:
                affiche_grille(GRILLE, TAILLE_GRILLE)
                Separateur()
                print("Égalité !")

            else:
                if JoueurActuel == Joueur1:
                    JoueurActuel = Joueur2
                else:
                    JoueurActuel = Joueur1

    Rejouer = "X"
    while Rejouer == "X":
        Separateur()
        Rejouer = input("Souhaitez-vous rejouer ? [O/N] ")         
