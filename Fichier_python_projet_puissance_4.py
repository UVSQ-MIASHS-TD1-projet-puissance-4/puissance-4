import numpy as np

# Fonction qui crée un nouveau plateau de jeu vide
def creer_plateau():
    return np.zeros((6, 7), dtype=int)

# Fonction qui affiche le plateau de jeu
def afficher_plateau(plateau):
    print(np.flip(plateau, 0))

# Fonction qui place un jeton dans la colonne choisie
def placer_jeton(plateau, ligne, colonne, jeton):
    plateau[ligne][colonne] = jeton

# Fonction qui vérifie si la colonne choisie est valide
def colonne_valide(plateau, colonne):
    return plateau[5][colonne] == 0

# Fonction qui trouve la première ligne vide de la colonne choisie
def trouver_ligne_vide(plateau, colonne):
    for ligne in range(6):
        if plateau[ligne][colonne] == 0:
            return ligne

# Fonction qui vérifie si un joueur a gagné
def gagnant(plateau, jeton):
    # Vérifier les lignes
    for ligne in range(6):
        for colonne in range(4):
            if plateau[ligne][colonne] == jeton and plateau[ligne][colonne+1] == jeton and plateau[ligne][colonne+2] == jeton and plateau[ligne][colonne+3] == jeton:
                return True

    # Vérifier les colonnes
    for ligne in range(3):
        for colonne in range(7):
            if plateau[ligne][colonne] == jeton and plateau[ligne+1][colonne] == jeton and plateau[ligne+2][colonne] == jeton and plateau[ligne+3][colonne] == jeton:
                return True

    # Vérifier les diagonales ascendantes
    for ligne in range(3):
        for colonne in range(4):
            if plateau[ligne][colonne] == jeton and plateau[ligne+1][colonne+1] == jeton and plateau[ligne+2][colonne+2] == jeton and plateau[ligne+3][colonne+3] == jeton:
                return True

    # Vérifier les diagonales descendantes
    for ligne in range(3, 6):
        for colonne in range(4):
            if plateau[ligne][colonne] == jeton and plateau[ligne-1][colonne+1] == jeton and plateau[ligne-2][colonne+2] == jeton and plateau[ligne-3][colonne+3] == jeton:
                return True

# Fonction principale qui gère le déroulement du jeu
def jouer():
    # Créer le plateau de jeu
    plateau = creer_plateau()

    # Initialiser les variables
    fini = False
    joueur = 1

    # Boucle principale
    while not fini:
        # Afficher le plateau de jeu
        afficher_plateau(plateau)

        # Demander au joueur de choisir une colonne
        colonne = int(input("Joueur " + str(joueur) + ", choisissez une colonne (0-6) : "))

        # Vérifier si la colonne est valide
        if colonne_valide(plateau, colonne):
            # Trouver la première ligne vide de la colonne choisie
            ligne
