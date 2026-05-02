from Jeux.Uno.Front.display import *
import random

def playing(deck, players, direction, counter, players_turn):
    """
    Boucle principale du jeu. Alterne entre les tours des joueurs et des bots jusqu'à un gagnant.
    """
    turn = 0
    while True:
        joker_reset(deck)
        players[0] = deck.sort(players[0])
        hand = players[players_turn % 4]
        next_hand = players[(players_turn + 1 * direction) % 4]

        if turn % 60:
            top = deck.deck.pop(0)
            deck.shuffle()
            deck.deck.insert(0, top)

        if players_turn % 4 == 0:
            players,next_hand,direction, players_turn,counter = (
                player_turn(deck,players,next_hand,direction, players_turn,counter))

        else:
            players,next_hand,direction, players_turn,counter = (
                bot_turn(deck,players,next_hand,direction, players_turn,counter))

        for hand in players:
            if len(hand) == 0:
                if game_over(players.index(hand)+1):
                    return
        turn += 1

def bot_turn(deck, players, next_hand,
             direction, players_turn, counter):
    """
    Gère le tour d'un bot. Le bot choisit automatiquement la meilleure carte à jouer.
    :return: Tuple - (players, next_hand, direction, players_turn, counter)
    """
    choosing = True
    while choosing:
        hand = players[players_turn % 4]
        top = deck.deck[0]
        put_draw = False
        if counter != 0:
            for card in hand:
                if card.value == "Draw":
                    hand = put_on_top(hand, hand.index(card), deck)
                    choosing = False
                    break
        else:
            for card in hand:
                if playable(card, top):
                    if card.color is None:
                        if hand[0].color is None:
                            card.color = random.choice(deck.colors)
                            card.card = (card.value, card.color)

                        else:
                            card.color = hand[0].color
                            card.card = (card.value, card.color)

                    hand = put_on_top(hand, hand.index(card), deck)
                    choosing = False
                    break

            if choosing:
                hand.extend(deck.draw(1))
                display_game(players, deck, direction)
                pygame.time.wait(150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    direction, players_turn, counter, next_hand = card_effects( direction, players_turn,
                                                               counter, next_hand, deck)
    display_game(players, deck, direction)

    pygame.time.wait(1200)

    return players, next_hand, direction, players_turn, counter



def player_turn(deck, players, next_hand,
                direction, players_turn, counter):
    """
    Gère le tour du joueur humain. Affiche le plateau et attend son choix de carte.
    :return: Tuple - (players, next_hand, direction, players_turn, counter)
    """
    while True:
        hand = players[0]
        hand = deck.sort(hand)
        top = deck.deck[0]
        put_draw = False

        choice = card_choice(players, deck, top, direction)
        if type(choice) is int:
            card = hand[choice]

        if counter != 0 and hand[choice].value == "Draw":
            hand = put_on_top(hand, choice, deck)
            break

        elif counter == 0:

            if choice == "Draw":
                if can_draw(hand, top):
                    hand.extend(deck.draw(1))

            elif choice is not None:
                if card.color is None:
                    color = color_choice(card)
                    if color:
                        card.color = color
                        card.card = (card.value, color)

                        hand = put_on_top(hand, choice, deck)
                        break
                elif playable(card, top):
                    hand = put_on_top(hand, choice, deck)
                    break

    direction, players_turn, counter, next_hand = card_effects(direction, players_turn,
                                                               counter, next_hand, deck)
    display_game(players, deck, direction)

    pygame.time.wait(1000)

    return players, next_hand, direction, players_turn, counter

def distribute(nbplayers, nbcards, deck):
    """
    Distribue les cartes initiales à chaque joueur.
    :return: List[List[Card]]
    """
    hands = []
    for i in range(nbplayers):
        hands.append(deck.draw(7))
    return hands

def playable(card, top):
    """
    Vérifie si une carte peut être jouée sur la carte au sommet.
    :return: Boolean
    """
    if card.color == top.color or card.value == top.value:
        return True

    elif type(card.value) is str:
        if card.value in ("joker","joker4"):
            return True

    return False

def choose_first_card(deck):
    """
    Choisit la première carte du jeu (évite les jokers et les +2).
    """
    top = deck.draw(1)[0]
    while top.value in ("joker", "joker4", "Draw"):
        top = deck.draw(1)[0]

    deck.deck.insert(0, top)


def joker_reset(deck):
    """
    Réinitialise la couleur de tous les jokers du deck à None.
    """
    for i in range(1, len(deck.deck)):
        card = deck.deck[i]

        if card.value in ("joker", "joker4"):
            card.color = None
            card.card = (card.value, None)

def can_draw(hand, top):
    """
    Vérifie si le joueur n'a aucune carte jouable et doit piocher.
    :return: Boolean
    """
    for card in hand:
        if playable(card, top):
            return False

    return True

def have_draw(hand):
    """
    Vérifie si la main contient au moins une carte "Draw" (+2).
    :return: Boolean
    """
    for card in hand:
        if card.value == "Draw":
            return True
    return False

def put_on_top(hand, choice, deck):
    """
    Place une carte de la main au sommet du deck et la retire de la main.
    :return: List[Card]
    """
    deck.deck.insert(0, hand.pop(choice))
    return hand

def card_effects(direction, players_turn, counter, next_hand, deck):
    """
    Applique les effets spéciaux de la carte jouée (Turn, Pass, Draw, joker4).
    :return: Tuple - (direction, players_turn, counter, next_hand)
    """
    top = deck.deck[0]
    if top.value == "Turn":
        direction *= -1

    elif top.value == "Pass":
        players_turn += 1 * direction

    elif top.value == "Draw":
        counter += 2

        if not have_draw(next_hand):
            next_hand.extend(deck.draw(counter))
            players_turn += 1 * direction
            counter = 0

    elif top.value == "joker4":
        next_hand.extend(deck.draw(4))
        players_turn += 1 * direction

    players_turn += 1 * direction

    return direction, players_turn, counter, next_hand