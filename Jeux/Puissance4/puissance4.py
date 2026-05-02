from Jeux.Puissance4.Back.engine import *
from Jeux.Puissance4.Front.display import *
from Class.GameStart import *


Display = GameStart("Puissance 4", (200,200,200),(900, 800))
fondu()
while Display.main_menu():
    """
    Initialisation du programme
    """
    turn = 1
    grid = [[0] * 7 for _ in range(6)]

    mode = mode_choice()

    while True:
        """
        Boucle principale
        """
        turn = turn % 2

        if turn == 1:
            columns = choice(grid, turn)

        else:
            if mode == 1:
                columns = bot_choice(grid)
            else:
                columns = choice(grid, turn)


        if free_column_verif(columns, grid):
            drop(turn, columns, grid, free_row(columns, grid))
            grid[free_row(columns, grid) - 1][columns] = 1 if turn == 1 else 2

            turn += 1

        end,winner = verification(grid)

        if end:
            game_over(winner, grid)
            break

pygame.quit()