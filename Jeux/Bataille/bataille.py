from Library.Jeux.Bataille.Front.display import *
from Library.Class.Deck_52 import *
from Library.Class.Player import *
from Library.Class.Pli import *
import random

deck = Deck()
deck.new_deck()
random.shuffle(deck.deck)
Joueur_1 = Player("Joueur_1")
Joueur_2 = Player("Joueur_2")

deck.tirer(Joueur_1.hand,26)
deck.tirer(Joueur_2.hand,26)

main_menu()

while len(Joueur_1.hand) > 0 and len(Joueur_2.hand) > 0:
    pli = Pli()

    pli.pli.append(Joueur_1.give_card())
    pli.pli.append(Joueur_2.give_card())

    jeu(pli.pli,Joueur_1.hand,Joueur_2.hand)
    retour = pli.result(Joueur_1, Joueur_2)

    while retour:
        jeu(pli.pli,Joueur_1.hand,Joueur_2.hand)
        retour = pli.result(Joueur_1, Joueur_2)
