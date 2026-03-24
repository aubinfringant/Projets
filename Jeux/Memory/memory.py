import time
from Library.Jeux.Memory.Class.Grid import *
from Library.Jeux.Memory.Front.display import *


grille = Grid(4,4)
grille.add_card()
cartes_trouvees = []
choix = []
main_menu()
stop = grille.full()
while not stop:
    for _ in range(2):
        choix.append(choix_cartes(grille,cartes_trouvees,choix))
    choix_cartes(grille, cartes_trouvees, choix)
    if choix[0][0] == choix[1][0]:
        grille.find_card(choix[0][0])
        cartes_trouvees.append(choix[0][0])
        choix = []
    else:
        choix = []
    jeu(grille,cartes_trouvees)
    stop = grille.full()
