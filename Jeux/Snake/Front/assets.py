import os
def load_assets():
    BASE = os.path.join(os.path.dirname(__file__), 'Assets') + os.sep
    import pygame
    pygame.init()
    pygame.display.set_mode((600,800))
    def img(nom, size=(45,45)):
        i = pygame.image.load(BASE + nom).convert_alpha()
        return pygame.transform.scale(i, size) if size else i

    apple = img('apple.png')
    grid = img('grille.png',(540,540))

    head = [pygame.transform.rotate(img('snake_head_down.png'),180),
            pygame.transform.rotate(img('snake_head_down.png'),90),
            pygame.transform.rotate(img('snake_head_down.png'),0),
            pygame.transform.rotate(img('snake_head_down.png'),270),]


    body_up = [pygame.transform.rotate(img(f"snake_body_down_up_{c}.png"),180) for c in range(15,0,-1)]
    body_right = [pygame.transform.rotate(img(f"snake_body_down_up_{c}.png"),90) for c in range(15,0,-1)]
    body_down = [pygame.transform.rotate(img(f"snake_body_down_up_{c}.png"),0) for c in range(15,0,-1)]
    body_left = [pygame.transform.rotate(img(f"snake_body_down_up_{c}.png"),270) for c in range(15,0,-1)]

    body = [body_up, body_right, body_down, body_left]

    turn_horaire = [pygame.transform.rotate(img('snake_turn_down_right.png'),0),
                    pygame.transform.rotate(img('snake_turn_down_right.png'),270),
                    pygame.transform.rotate(img('snake_turn_down_right.png'),180),
                    pygame.transform.rotate(img('snake_turn_down_right.png'),90),]

    turn_anti = [pygame.transform.rotate(img('snake_turn_down_left.png'),0),
                 pygame.transform.rotate(img('snake_turn_down_left.png'),90),
                 pygame.transform.rotate(img('snake_turn_down_left.png'),180),
                 pygame.transform.rotate(img('snake_turn_down_left.png'),270),]

    tail_up = [pygame.transform.rotate(img(f"snake_tail_down_{c}.png"),180) for c in range(15,0,-1)]
    tail_right = [pygame.transform.rotate(img(f"snake_tail_down_{c}.png"),90) for c in range(15,0,-1)]
    tail_down = [pygame.transform.rotate(img(f"snake_tail_down_{c}.png"),0) for c in range(15,0,-1)]
    tail_left = [pygame.transform.rotate(img(f"snake_tail_down_{c}.png"),270) for c in range(15,0,-1)]

    tail = [tail_up,tail_right,tail_down,tail_left]

    return apple, grid, head, body, tail, turn_horaire, turn_anti