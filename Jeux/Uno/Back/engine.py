from Library.Jeux.Uno.Front.display import *
import random

def playing(deck, players, top, direction, counter, players_turn):
    while True:
        deck = joker_reset(deck)
        players[0] = deck.sort(players[0])
        hand = players[players_turn % 4]
        next_hand = players[(players_turn + 1 * direction) % 4]

        if players_turn % 4 == 0:
            deck,players,hand,next_hand,direction, players_turn,counter,top = (
                player_turn(deck,players,hand,next_hand,direction, players_turn,counter,top))

        else:
            deck,players,hand,next_hand,direction, players_turn,counter,top = (
                bot_turn(deck,players,hand,next_hand,direction, players_turn,counter,top))

        if not deck:
            return False

        for hand in players:
            if len(hand) == 0:
                choix = game_over(players.index(hand)+1)

                if not choix:
                    return False

                else:
                    return main_menu()

def bot_turn(deck, players, hand, next_hand,
             direction, players_turn, counter, top):
    choosing = True
    running = True
    while choosing:

        if top.value == "Draw" and counter != 0:
            for card in hand:
                hand, top, deck, choosing = have_draw(hand, card, top, deck,
                                                      counter)
                if not choosing:
                    break


        for card in hand:
            if playable(card, top):
                if card.color is None:
                    if hand[0].color is None:
                        card.color = random.choice(deck.colors)
                        card.card = (card.value, card.color)

                    else:
                        card.color = hand[0].color
                        card.card = (card.value, card.color)

                top = get_top(hand, hand.index(card), deck)
                choosing = False
                break

        hand.extend(deck.draw(1))
        running, _ = display(players, deck, top, direction)
        pygame.time.wait(150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    if not running:
        return (False,) * 8

    direction, players_turn, counter, next_hand = card_effects(top, direction, players_turn,
                                                               counter, next_hand, deck)
    running = display(players, deck, top, direction)

    if not running:
        return (False,) * 8

    pygame.time.wait(1200)

    return deck,players,hand,next_hand,direction, players_turn,counter,top



def player_turn(deck, players, hand, next_hand,
                direction, players_turn, counter, top):
    while True:
        hand = deck.sort(hand)

        running, choice = card_choice(players, deck, top, direction)
        if type(choice) is int:
            card = hand[choice]

        if not running:
            break

        if top.value == "Draw" and counter != 0:
            hand, top, deck, choosing = have_draw(hand, card, top, deck, counter)

        elif choice == "Draw":
            if can_draw(hand, top):
                hand.extend(deck.draw(1))

        elif choice is not None:
            if card.color is None:
                running, color = color_choice(card)

                card.color = color
                card.card = (card.value, color)

                top = get_top(hand, choice, deck)
                break

            elif playable(card, top):
                top = get_top(hand, choice, deck)
                break

    if not running:
        return (False,) * 8

    direction, players_turn, counter, next_hand = card_effects(top, direction, players_turn,
                                                               counter, next_hand, deck)
    running = display(players, deck, top, direction)

    if not running:
        return (False,) * 8

    pygame.time.wait(1000)

    return deck,players,hand,next_hand,direction, players_turn,counter,top

def distribute(nbplayers, nbcards, deck):
    hands = []
    for i in range(nbplayers):
        hands.append(deck.draw(7))
    return hands

def playable(card, top):
    if card.color == top.color or card.value == top.value:
        return True

    elif type(card.value) is str:
        if card.value in ("joker","joker4"):
            return True

    return False

def choose_first_card(deck):
    top = deck.draw(1)[0]
    while top.value in ("joker", "joker4", "Draw"):
        deck.deck.insert(0, top)
        top = deck.draw(1)[0]

    return top,deck

def joker_reset(deck):
    for i in range(1, len(deck.deck)):
        card = deck.deck[i]

        if card.value in ("joker", "joker4"):
            card.color = None
            card.card = (card.value, None)

    return deck

def can_draw(hand, top):
    for card in hand:
        if playable(card, top):
            return False

    return True

def have_draw(hand, card, top, deck, counter):
    if card.value == "Draw":
        counter += 2
        top = card

        hand.pop(hand.index(top))
        deck.deck.insert(0, top)

        return hand,top,deck,False

    return hand,top,deck,True

def get_top(hand, choice, deck):
    top = hand.pop(choice)
    deck.deck.insert(0, top)
    return top

def card_effects(top, direction, players_turn, counter, next_hand, deck):

    if top.value == "Turn":
        direction *= -1

    elif top.value == "Pass":
        players_turn += 1 * direction

    elif top.value == "Draw":
        counter += 2
        add = False

        for card in next_hand:
            if card.value == "Draw":
                add = True

        if not add:
            next_hand.extend(deck.draw(counter))
            players_turn += 1 * direction
            counter = 0

    elif top.value == "joker4":
        next_hand.extend(deck.draw(4))
        players_turn += 1 * direction

    players_turn += 1 * direction

    return direction, players_turn, counter, next_hand

# Debug
"""def show_deck(deck):
    for i in range(len(deck)):
        print(deck[i])

def show_card(players):
    for i in range(len(players)):
        for j in range(len(players[i])):
            print(players[i][j])"""