from Library.Jeux.Uno.Front.display import *
from Library.Jeux.Uno.Class.DeckUno import *
from Library.Jeux.Uno.Back.Engine import *

def init():
    deck = DeckUno()
    counter,players_turn = 0,0
    direction = 1

    players = distribute(4,7, deck)
    top,deck = choose_first_card(deck,players)
    running = main_menu()

    show_card(players)

    while running:
        deck = joker_reset(deck)
        players[0] = deck.sort(players[0])
        hand = players[players_turn % 4]
        next_hand = players[(players_turn + 1 * direction) % 4]

        if players_turn % 4 == 0:

            choosing = True
            while choosing:
                players[0] = deck.sort(players[0])

                running,choice = choix_cartes(players,deck,top,direction)
                if type(choice) is int:
                    choice -= 1
                    card = hand[choice]

                if not running:
                    break

                if top.value == "Draw" and counter !=0:
                    hand,top,deck,choosing = have_draw(hand,card,top,deck,
                                                       counter,players_turn)

                elif choice == "Draw":
                    if can_draw(hand, top):
                        hand.extend(deck.draw(1))

                elif choice is not None:
                    if card.color is None:
                        running,color = choix_couleur(card)

                        card.color = color
                        card.card = (card.value,color)

                        top = get_top(hand,choice,deck,players_turn)
                        choosing = False

                    elif playable(card, top):
                        top = get_top(hand, choice, deck, players_turn)
                        choosing = False

            direction, players_turn, counter, next_hand = card_effects(top,direction,players_turn,
                                                                       counter,next_hand,deck)
            running, _ = display(players,deck,top,direction)
            pygame.time.wait(1200)
            running, _ = display(players, deck, top, direction)

        else:
            choosing = True
            while choosing:

                for card in hand:
                    if top.value == "Draw" and counter !=0:
                        hand,top,deck,choosing = have_draw(hand,card,top,deck,
                                                           counter,players_turn)
                        if not choosing:
                             break

                if choosing:
                    for card in hand:
                        if playable(card, top):
                            if card.color is None:
                                if hand[0].color is None:
                                    card.color = random.choice(deck.colors)
                                    card.card = (card.value, card.color)
                                else:
                                    card.color = hand[0].color
                                    card.card = (card.value, card.color)
                            top = get_top(hand, hand.index(card), deck, players_turn)
                            choosing = False
                            break

                if choosing:
                    hand.extend(deck.draw(1))
                    print("Draw",players_turn % 4)
                    running, _ = display(players, deck, top, direction)
                    pygame.time.wait(150)
                    running, _ = display(players, deck, top, direction)

            direction, players_turn, counter, next_hand = card_effects(top, direction, players_turn,
                                                                       counter, next_hand, deck)
            running, _ = display(players,deck,top,direction)
            pygame.time.wait(1200)
            running, _ = display(players, deck, top, direction)


        for hand in players:
            if len(hand) == 0:
                running,choix = game_over(players, deck, top, players.index(hand)+1,direction)
                if choix:
                    return True

running = True
while running:
    running = init()
pygame.quit()