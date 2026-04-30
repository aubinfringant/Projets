from Library.Jeux.Puissance4.Back.engine import *
from Library.Jeux.Puissance4.Front.display import *

launch=fondu()

while launch:
    start = main_menu()
    if not start:
        break

    mode = menu()
    if not mode:
        break

    turn = 1
    grid = [[0] * 7 for _ in range(6)]

    while True:
        turn = turn % 2

        if turn == 1:
            run, columns = choice(grid, turn)

        else:
            if mode == 1:
                run, columns = bot_choice(grid)
            else:
                run, columns = choice(grid, turn)

        if not run:
            break

        if free_column_verif(columns, grid):
            run = drop(turn, columns, grid, free_row(columns, grid))
            grid[free_row(columns, grid) - 1][columns] = 1 if turn == 1 else 2

            turn += 1

        running, winner = verification(grid)
        if not running or not run:
            break

    if winner:
        run = game_over(winner, grid)
    elif not running and winner is None:
        run = game_over(winner, grid)

    if not run:
        break

pygame.quit()