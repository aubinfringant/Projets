def free_column_verif(column,grid):
    """
    Vérifie si la colonne n'est pas rempli.
    :return: Boolean
    """
    return grid[0][column] == 0

def free_row(column,grid):
    """
    Renvoye la premiere ligne non vide.
    :return: Integer
    """
    for j in range(len(grid)):
        if grid[j][column] != 0:
            return j
    return len(grid)

def verification(grid):
    """
    Regarde si un joueur a gagné.
    :return: tuple(Boolean, Integer)
    """
    if 0 not in grid[0]:
        return True,0
    #ligne
    for ligne in range(0, 6):
        for column in range(0, 4):
            a = 0
            b = 0
            for jeton in range(0, 4):
                if grid[ligne][column + jeton] == 1:
                    a += 1
                    if a == 4:
                        return True, 1
                elif grid[ligne][column + jeton] == 2:
                    b += 1
                    if b == 4:
                        return True, 2
    #column
    for column in range(0, 7):
        for ligne in range(0, 3):
            a = 0
            b = 0
            for jeton in range(0, 4):
                if grid[ligne + jeton][column] == 1:
                    a += 1
                    if a == 4:
                        return True, 1
                elif grid[ligne + jeton][column] == 2:
                    b += 1
                    if b == 4:
                        return True, 2
    #diagonale haut-gauche/bas-droite
    for ligne in range(0, 3):
        for column in range(0, 4):
            a = 0
            b = 0
            for jeton in range(0, 4):
                if grid[ligne + jeton][column + jeton] == 1:
                    a += 1
                    if a == 4:
                        return True, 1
                elif grid[ligne + jeton][column + jeton] == 2:
                    b += 1
                    if b == 4:
                        return True, 2
    #diagonale haut-droite/bas-gauche
        for column in range(6, 2, -1):
            a = 0
            b = 0
            for jeton in range(0, 4):
                if grid[ligne + jeton][column - jeton] == 1:
                    a += 1
                    if a == 4:
                        return True, 1
                elif grid[ligne + jeton][column - jeton] == 2:
                    b += 1
                    if b == 4:
                        return True, 2
    return False, 0
"""
En dessous il y a se que m'a fait l'IA pour créer une IA imbatable.
Resultat une IA nulle.
"""
def play(grid, ligne, column, joueur):#IA
    grid[ligne-1][column] = joueur

def bot_choice(grid): #IA
    import math

    columns = 7
    PROFONDEUR = 4

    def score_fenetre(fenetre):
        score = 0

        if fenetre.count(2) == 4:
            score += 100
        elif fenetre.count(2) == 3 and fenetre.count(0) == 1:
            score += 5
        elif fenetre.count(2) == 2 and fenetre.count(0) == 2:
            score += 2

        if fenetre.count(1) == 3 and fenetre.count(0) == 1:
            score -= 80  # blocage urgent

        return score

    def evaluation(grid):
        score = 0

        # lignes
        for ligne in range(6):
            for col in range(4):
                fenetre = [grid[ligne][col+i] for i in range(4)]
                score += score_fenetre(fenetre)

        # columns
        for col in range(7):
            for ligne in range(3):
                fenetre = [grid[ligne+i][col] for i in range(4)]
                score += score_fenetre(fenetre)

        # diagonales
        for ligne in range(3):
            for col in range(4):
                fenetre = [grid[ligne+i][col+i] for i in range(4)]
                score += score_fenetre(fenetre)

        for ligne in range(3):
            for col in range(3, 7):
                fenetre = [grid[ligne+i][col-i] for i in range(4)]
                score += score_fenetre(fenetre)

        return score

    def minimax(grid, deep, alpha, beta, maximisant):
        coups = [c for c in range(columns) if free_column_verif(c, grid)]

        if deep == 0 or not coups:
            return evaluation(grid)

        if maximisant:
            max_eval = -math.inf
            for col in coups:
                ligne = free_row(col, grid)
                if ligne is None:
                    continue

                copy = [row[:] for row in grid]
                play(copy, ligne, col, 2)

                eval = minimax(copy, deep - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            return max_eval

        else:
            min_eval = math.inf
            for col in coups:
                ligne = free_row(col, grid)
                if ligne is None:
                    continue

                copy = [row[:] for row in grid]
                play(copy, ligne, col, 1)

                eval = minimax(copy, deep - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)

                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return min_eval

    # Choix du meilleur coup
    best_score = -math.inf
    best_col = 3  # centre par défaut

    for col in range(columns):
        if not free_column_verif(col, grid):
            continue

        ligne = free_row(col, grid)
        if ligne is None:
            continue

        copy = [row[:] for row in grid]
        play(copy, ligne, col, 2)

        score = minimax(copy, PROFONDEUR - 1, -math.inf, math.inf, False)

        if score > best_score:
            best_score = score
            best_col = col

    return best_col
