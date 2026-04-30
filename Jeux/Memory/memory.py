from Jeux.Memory.Front.display import *
from Class.GridMemory import *

run = main_menu()

while run:

    grid = Grid(4,4)
    grid.add_card()

    found_cards = []
    choices = []

    play = run

    while play:
        for _ in range(2):
            choice = card_choice(grid,found_cards,choices)
            if choice:
                choices.append(choice)
            else:
                run = False
                break

        if not choice:
            run = False
            break

        run = card_choice(grid, found_cards, choices, pause=True)

        if not run:
            break

        if choices[0][0] == choices[1][0]:
            grid.find_card(choices[0][0])
            found_cards.append(choices[0][0])

        choices = []

        if grid.full():
            run = main_menu()
            break
