from Jeux.Bataille.Front.assets import load_assets
import pygame
import sys

def display_num_of_card(p1 = str, p2 = str):
    """
    Place les eléments sur l'écran.
    """
    font = pygame.font.SysFont("calibri", 50, True)
    card_joueur = font.render(p1, True, (255, 255, 255))
    card_ordi = font.render(p2, True, (255, 255, 255))

    screen.blit(card_joueur, (128, 150))
    screen.blit(card_ordi, (528, 150))


def display_table(trick, p1, p2):
    """
    Placer le tapis et les cartes en bataille.
    """
    screen.blit(carpet, (0, 0))
    screen.blit(card_back, (100, 200))
    screen.blit(card_back, (500, 200))

    for i in range(0, len(trick.cards), 2) :
        screen.blit(cards_sprite[trick.cards[i].card], (210, 200 + 25 * i))
        screen.blit(cards_sprite[trick.cards[i+1].card], (390, 200 + 25 * i))

    display_num_of_card(str(len(p1)), str(len(p2)))

def player_turn(trick, p1, p2):
    """
    Echange les 2 cartes en fonction de la carte choisie
    pour pouvoir donner la bonne avec .drop()
    ou donne la derniere carte si une carte restante.
    """

    if len(p1.hand) > 1:
        choice = display_choose(trick, p1.hand, p2.hand)

    else:
        choice = 0

    p1.hand[0], p1.hand[choice] = p1.hand[choice], p1.hand[0]

    trick.cards.append(p1.drop())
    trick.cards.append(p2.drop())

    display_table(trick, p1.hand, p2.hand)

def display_choose(trick,p1,p2):
    """
    Gére l'affichage des cartes a choisir et de la selection de la carte.
    :return: Integer
    """
    card1 = cards_sprite[p1[0].card]
    card2 = cards_sprite[p1[1].card]

    while True:
        clock.tick(60)
        display_table(trick, p1, p2)
        size_trick = len(trick.cards)
        screen.blit(cards_sprite[p2[0].card], (390, 200 + 25 * (size_trick + 1 // 2)))

        if size_trick == 0:
            screen.blit(cards_sprite[p2[0].card], (390, 200 + 25 * (size_trick // 2)))

        display_num_of_card(str(len(p1)), str(len(p2)))

        screen.blit(card1, (100, 500))
        screen.blit(card2, (220, 500))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):

                    x, y = pygame.mouse.get_pos()

                    if 100 < x < 200 and 500 < y < 650:
                        return 0
                    if 220 < x < 320 and 500 < y < 650:
                        return 1

def display_game_over(p1,p2):
    """
    Gére l'affichage de la fin de la partie.
    :return: Boolean
    """
    display_table("", p1, p2)
    pygame.display.flip()
    font = pygame.font.SysFont("calibri", 70, True)

    while True:
        clock.tick(60)

        msg1 = font.render("GAME OVER", True, (200, 100, 100))
        msg2 = font.render("Joueur 1 GAGNE !", True, (200, 100, 100))

        if len(p1) == 0:
            msg1 = font.render("GAME OVER", True, (200, 100, 100))
            msg2 = font.render("Joueur 2 GAGNE !", True, (200, 100, 100))

        screen.blit(msg1, (165, 50))
        screen.blit(msg2, (110, 380))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1,3):
                    return True

pygame.init()
pygame.display.set_caption("BATAILLE")
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
card_back,cards_sprite,carpet = load_assets()
