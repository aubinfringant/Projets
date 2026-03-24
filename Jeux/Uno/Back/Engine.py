def distribute(nbplayers,nbcards,deck):
    hands = []
    for i in range(nbplayers):
        hands.append(deck.draw(7))
    return hands

def playable(card,top):
    if card.color == top.color or card.value == top.value:
        return True
    elif type(card.value) is str:
        if card.value in ("joker","joker4"):
            return True
    return False

def show_deck(deck):
    for i in range(len(deck)):
        print(deck[i])

def show_card(players):
    for i in range(len(players)):
        for j in range(len(players[i])):
            print(players[i][j])

def choose_first_card(deck,top):
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

def can_draw(hand,top):
    for card in hand:
        if playable(card, top):
            return False
    return True

def have_draw(hand,card,top,deck,counter,players_turn):
    if card.value == "Draw":
        counter += 2
        top = card
        hand.pop(hand.index(top))
        deck.deck.insert(0, top)
        choosing = False
        print(top, players_turn % 4)
        return hand,top,deck,choosing
    return hand,top,deck,True

def get_top(hand,choice,deck,players_turn):
    top = hand.pop(choice)
    deck.deck.insert(0, top)
    print(top, players_turn % 4)
    return top

def card_effects(top,direction,players_turn,counter,next_hand,deck):
    turn = players_turn % 4
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
            print("Draw", turn)
    elif top.value == "joker4":
        next_hand.extend(deck.draw(4))
        players_turn += 1 * direction
        print("Draw", turn)

    players_turn += 1 * direction
    return direction, players_turn, counter, next_hand
