TAILLE_GRILLE = 3

def est_Libre(ligne, colonne,grille):
    if(grille[ligne][colonne]) == "#":
        return True
    return False

    # Vérifier si la grille est pleine

def grille_Pleine(grille):
    for ligne in range(TAILLE_GRILLE):
        for colonne in range(TAILLE_GRILLE):
            if(grille[ligne][colonne]) == "#":
                return False
    return True

    # Tester si un coup est gagant

def coup_Gagnant(symbole,ligne,colonne,grille):

    for ligne in grille:    # Cas où une ligne est alignée
        if ligne == [symbole for i in range(TAILLE_GRILLE)]:
            return True
        
    for colonne in range(TAILLE_GRILLE): # Cas où une colonne est alignée
        lst = []
        for k in grille:
            lst.append(k[colonne])
        if lst == [symbole for i in range(TAILLE_GRILLE)]:
            return True

    nb1= 0
    for i in range(1,TAILLE_GRILLE+1):
        case1 = grille[TAILLE_GRILLE-i][TAILLE_GRILLE-i]
        if case1 == symbole:
            nb1 += 1
        if nb1 == TAILLE_GRILLE:
            return True
        
    nb2= 0
    for i in range(TAILLE_GRILLE):
        case2 = grille[TAILLE_GRILLE-1-i][0+i]
        if case2 == symbole:
            nb2 += 1
        if nb2 == TAILLE_GRILLE:
            return True
    
    return False
################################################################################
##################################Jeu de tests##################################
################################################################################
# ce jeu de tests permet de tester les fonctions coup_Gagnant,
# est_Libre et grille_Pleine

#copier-coller le code de la fonction de test souhaitée dans votre projet puis
#appelez cette fonction dans la console

def test_coup_Gagnant():
    #grille1 présente un alignement horizontal de X
    grille1 = [['X', 'X', 'X'],
              ['O', '#', '#'],
              ['#', '#', 'O']]
    #grille2 présente un alignement vertical de O
    grille2 = [['X', 'O', 'X'],
               ['X', 'O', '#'],
               ['#', 'O', 'X']]
    #grille3 présente un alignement diagonal principal de X
    grille3 = [['X', 'O', '#'],
               ['#', 'X', '#'],
               ['#', 'O', 'X']]
    #grille4 présente un alignement diagonal gauche de O
    grille4 = [['X', '#', 'O'],
               ['#', 'O', 'X'],
               ['O', '#', 'X']]
    #grille5 est pleine match nul
    grille5 = [['O', 'X', 'X'],
               ['X', 'X', 'O'],
               ['O', 'O', 'X']]
    assert coup_Gagnant("X", 0, 0, grille1)
    assert coup_Gagnant("X", 0, 1, grille1)
    assert coup_Gagnant("X", 0, 2, grille1)
    assert not coup_Gagnant("O", 0, 0, grille1)
    assert coup_Gagnant("O", 0, 1, grille2)
    assert not coup_Gagnant("X", 0, 2, grille2)
    assert not coup_Gagnant("X", 1, 2, grille2)
    assert coup_Gagnant("O", 1, 1, grille2)
    assert coup_Gagnant("O", 2, 1, grille2)
    assert coup_Gagnant("X", 0, 0, grille3)
    assert coup_Gagnant("X", 1, 1, grille3)
    assert coup_Gagnant("X", 2, 2, grille3)
    assert not coup_Gagnant("O", 0, 1, grille3)
    assert not coup_Gagnant("O", 2, 1, grille3)
    assert coup_Gagnant("O", 0, 2, grille4)
    assert coup_Gagnant("O", 1, 1, grille4)
    assert coup_Gagnant("O", 2, 0, grille4)
    assert not coup_Gagnant("X", 1, 2, grille4)
    print("La fonction coup_Gagnant a passé tous les tests !")

def test_est_Libre():
    #grille1 présente un alignement horizontal de X
    grille1 = [['X', 'X', 'X'],
              ['O', '#', '#'],
              ['#', '#', 'O']]
    #grille2 présente un alignement vertical de O
    grille2 = [['X', 'O', 'X'],
               ['X', 'O', '#'],
               ['#', 'O', 'X']]
    #grille3 présente un alignement diagonal principal de X
    grille3 = [['X', 'O', '#'],
               ['#', 'X', '#'],
               ['#', 'O', 'X']]
    #grille4 présente un alignement diagonal gauche de O
    grille4 = [['X', '#', 'O'],
               ['#', 'O', 'X'],
               ['O', '#', 'X']]
    #grille5 est pleine match nul
    grille5 = [['O', 'X', 'X'],
               ['X', 'X', 'O'],
               ['O', 'O', 'X']]
    assert est_Libre(2, 0, grille2)
    assert est_Libre(1, 2, grille3)
    assert est_Libre(2, 1, grille4)
    print("La fonction est_Libre a passé tous les tests !")

def test_grille_Pleine():
    #grille1 présente un alignement horizontal de X
    grille1 = [['X', 'X', 'X'],
              ['O', '#', '#'],
              ['#', '#', 'O']]
    #grille2 présente un alignement vertical de O
    grille2 = [['X', 'O', 'X'],
               ['X', 'O', '#'],
               ['#', 'O', 'X']]
    #grille3 présente un alignement diagonal principal de X
    grille3 = [['X', 'O', '#'],
               ['#', 'X', '#'],
               ['#', 'O', 'X']]
    #grille4 présente un alignement diagonal gauche de O
    grille4 = [['X', '#', 'O'],
               ['#', 'O', 'X'],
               ['O', '#', 'X']]
    #grille5 est pleine match nul
    grille5 = [['O', 'X', 'X'],
               ['X', 'X', 'O'],
               ['O', 'O', 'X']]
    assert not grille_Pleine(grille1)
    assert not grille_Pleine(grille2)
    assert not grille_Pleine(grille3)
    assert not grille_Pleine(grille4)
    assert grille_Pleine(grille5)
    print("La fonction grille_Pleine a passé tous les tests !")


    
print(test_coup_Gagnant())
print(test_est_Libre())
print(test_grille_Pleine())