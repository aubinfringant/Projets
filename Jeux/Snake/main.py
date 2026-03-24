apple_number = 0
apple_sack = []


def start():
    # on place la tête du serpent à gauche du corps
    snake[0][1][1] = snake[1][1][1]
    snake[0][1][0] = snake[1][1][0]-3
    apple_eaten = 0
    running = True
    direction = direction
    direction_avant = direction
    clock = pygame.time.Clock()
    clock.tick(60)
    time_start = pygame.time.get_ticks()
    time.sleep(0.4)
    timer_finish_body = pygame.time.get_ticks()
    timer_start_head = pygame.time.get_ticks()//24-time_start//24
    case_vide=141
    move=-1
    direction_liste = [left]
    snake_old_head = snake[0]
    snake_old_head_cord = snake_old_head[1][:]
    #création des pommes de départ
    while apple_number <= 0:
        create_apple()
    while running:
        # raffraîchissement de l'écran
        screen.fill((200, 200, 200))
        screen.blit(grille, (30, 230))

        # calcule du nombre de case
        case_vide = 144 - len(snake) - len(apple_sack)

        # sauvegarde de la fin du serpent si le serpent grandi (mode de fonctionnement)
        snake_old_tail=snake[-1]
        snake_old_tail_sprite=snake_old_tail[0]
        snake_old_tail_cord=snake_old_tail[1][:]
        # sauvegarde du segment du seprent aprés la tête si le serpent grandi (mode de fonctionnement)
        snake_old_second_last_body=snake[-2]
        snake_old_second_last_sprite=snake_old_second_last_body[0]
        snake_old_second_last_cord=snake_old_second_last_body[1][:]

        # image par seconde: la tête,le 1er segement et la queue bouge 15 fois plus vite que le corps
        timer_finish_head = pygame.time.get_ticks() // 24 - time_start // 24

        # on vérifie si le serpent ne se mord pas ou a atteint les limites
        verification()



        # affichage des pommes
        for i in range(0,len(apple_sack)):
            screen.blit(apple, list(apple_sack[i]))

        # affichage du serpent de la tête à la queue
        for i in range(-1,-len(snake)-1,-1):
            screen.blit(snake[i][0],snake[i][1])


        # initialisation des actions dans pygame et arrêt si on ferme la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()

        # récupération de la direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and direction_avant != right:
            direction_liste.append(left)
        elif keys[pygame.K_UP] and direction_avant != down:
            direction_liste.append(up)
        elif keys[pygame.K_RIGHT] and direction_avant != left:
            direction_liste.append(right)
        elif keys[pygame.K_DOWN] and direction_avant != up:
            direction_liste.append(down)

        # mouvement du corps entier
        if move==14:
            # récupérer la direction
            if direction_liste == []:
                direction=direction_avant
            else :
                direction=direction_liste[-1]

            # bouger en fonction de la direction
            if direction == left:

                # on décale les segments du corps vers la tête
                # on réoriente les segments
                segment_swap()


                # on bouge la tête pour ne pas perdre (fonctionnement)
                if snake[0][1][0] > 25:
                    snake[0][1][0] -= 3
                    snake[0][0] = liste_head[left]

                # si la tête est sortie des limites c'est perdu
                else:
                    game_over()
            elif direction == right:
                segment_swap()
                if snake[0][1][0] < 530:
                    snake[0][1][0] += 3
                    snake[0][0] = liste_head[right]
                else:
                    game_over()
            elif direction == up:
                segment_swap()
                if snake[0][1][1] > 225:
                    snake[0][1][1] -= 3
                    snake[0][0] = liste_head[down]
                else:
                    game_over()
            elif direction == down:
                segment_swap()
                if snake[0][1][1] < 730:
                    snake[0][1][1] += 3
                    snake[0][0] = liste_head[up]
                else:
                    game_over()
            move=0
            direction_avant=direction
            direction_liste = []
        # on bouge la tête, le premier segment et la queue avec fluidité (même principe que le corps)
        if (timer_finish_head-timer_start_head) == 1:
            timer_start_head = pygame.time.get_ticks()//24-time_start//24
            move += 1
            if direction == left:
                if snake[0][1][0] > 25:
                    snake[0][1][0] -= 3
                    snake_body()
                    snake[0][0] = liste_head[left]
                    snake_tail()
                else:
                    game_over()
            elif direction == right:
                if snake[0][1][0] < 530:
                    snake[0][1][0] += 3
                    snake_body()
                    snake[0][0] = liste_head[right]
                    snake_tail()
                else:
                    game_over()
            elif direction == up:
                if snake[0][1][1] > 225:
                    snake[0][1][1] -= 3
                    snake_body()
                    snake[0][0] = liste_head[down]
                    snake_tail()
                else:
                    game_over()
            elif direction == down:
                if snake[0][1][1] < 730:
                    snake[0][1][1] += 3
                    snake_body()
                    snake[0][0] = liste_head[up]
                    snake_tail()
                else:
                    game_over()


        # on vérifie si la tête est à sur pomme
        for i in range(0,len(apple_sack)):

            #si les cases sont pleines de pomme ou de serpent alors on enlève une pomme max
            if case_vide==0 :
                i-=1
            if snake[0][1] == apple_sack[i]:
                apple_eaten += 1
                apple_number -= 1
                apple_sack.remove(apple_sack[i])

                # création d'un nouveau segment et on fait reculer la queue pour faire de la place
                snake_old_new_tail=[snake_old_tail_sprite,snake_old_tail_cord]
                snake_old_new_second_last_body = [snake_old_second_last_sprite,snake_old_second_last_cord]
                snake.pop()
                snake.append(snake_old_new_tail)
                snake.insert(-1, snake_old_new_second_last_body)

                # si on mange une pomme une autre se crée
                create_apple()

        # affichage des changement
        pygame.display.update()
        clock.tick(60)
def segment_swap(self):
    for i in range( len(snake)-1,1,-1):
        snake[i][1] = snake[i - 1][1][:]
    snake[1][1] = snake_old_head_cord #
    snake_body()
    snake_tail()
    snake[1][1] = snake[0][1][:] #
    snake_old_head = snake[0][:]
    snake_old_head_cord = snake_old_head[1][:]
def create_apple(self):
    if case_vide >=1:
        apple_cord = random.choice(random.choice(liste_grille))
        for i in range(0,len(apple_sack)):
            if apple_cord in apple_sack:
                return create_apple()
        for i in range(0, len(snake)):
            if apple_cord == snake[i][1]:
                return create_apple()

        apple_sack.append(apple_cord)
        apple_number += 1
def verification(self):
    for i in range(1,len(snake)):
        if snake[0][1] == snake[i][1]:
            game_over()
    if apple_eaten == 141:
        pygame.display.flip()
        game_over()
def game_over(self):
    running = False
    if apple_eaten == 141:
        msg=font.render("VOUS AVEZ GAGNEE !!!",True,(200,0,0))
    else :
        msg=font.render("VOUS AVEZ PERDU !!!",True,(200,0,0))
    time_gameover=pygame.time.get_ticks()
    time=time_gameover-time_start
    print(time)
    while True:
        screen.blit(msg,(50,50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == (1 or 3):
                    return main_menu()
def snake_tail(self):
    if snake[-1][1][0] > snake[-2][1][0]:
        snake[-1][0] = liste_frame_tail[left][move]
    elif snake[-1][1][0] < snake[-2][1][0]:
        snake[-1][0] = liste_frame_tail[right][move]
    elif snake[-1][1][1] < snake[-2][1][1]:
        snake[-1][0] = liste_frame_tail[down][move]
    elif snake[-1][1][1] > snake[-2][1][1]:
        snake[-1][0] = liste_frame_tail[up][move]
def snake_body(self):
    for i in range(-1, len(snake) - 2):
        if snake[i][1][1] > snake[i + 2][1][1] and snake[i][1][0] > snake[i + 2][1][0] and snake[i+1][1][0]==snake[i][1][0]:
            snake[i + 1][0] = liste_turn[0] #down_left
        elif snake[i][1][1] > snake[i + 2][1][1] and snake[i][1][0] < snake[i + 2][1][0] and snake[i+1][1][0]==snake[i][1][0]:
            snake[i + 1][0] = liste_turn[1] #down_right
        elif snake[i][1][1] < snake[i + 2][1][1] and snake[i][1][0] < snake[i + 2][1][0] and snake[i+1][1][1]==snake[i][1][1]:
            snake[i + 1][0] = liste_turn[2] #left_down
        elif snake[i][1][1] > snake[i + 2][1][1] and snake[i][1][0] < snake[i + 2][1][0] and snake[i+1][1][1]==snake[i][1][1]:
            snake[i + 1][0] = liste_turn[3] #left_up
        elif snake[i][1][1] < snake[i + 2][1][1] and snake[i][1][0] > snake[i + 2][1][0] and snake[i+1][1][1]==snake[i][1][1]:
            snake[i + 1][0] = liste_turn[4] #right_down
        elif snake[i][1][1] > snake[i + 2][1][1] and snake[i][1][0] > snake[i + 2][1][0] and snake[i+1][1][1]==snake[i][1][1]:
            snake[i + 1][0] = liste_turn[5] #right_up
        elif snake[i][1][1] < snake[i + 2][1][1] and snake[i][1][0] > snake[i + 2][1][0] and snake[i+1][1][0]==snake[i][1][0]:
            snake[i + 1][0] = liste_turn[6] #up_left
        elif snake[i][1][1] < snake[i + 2][1][1] and snake[i][1][0] < snake[i + 2][1][0] and snake[i+1][1][0]==snake[i][1][0]:
            snake[i + 1][0] = liste_turn[7] #up_right
        elif snake[i][1][1] == snake[i + 2][1][1] and snake[i][1][0] > snake[i + 2][1][0]:
            snake[i + 1][0] = liste_body[right]
        elif snake[i][1][1] == snake[i + 2][1][1]and snake[i][1][0] < snake[i + 2][1][0]:
            snake[i + 1][0] = liste_body[left]
        elif snake[i][1][0] == snake[i + 2][1][0] and snake[i][1][1] > snake[i + 2][1][1]:
            snake[i + 1][0] = liste_body[up]
        elif snake[i][1][0] == snake[i + 2][1][0]and snake[i][1][1] < snake[i + 2][1][1]:
            snake[i + 1][0] = liste_body[down]
        if i == 0:
            continue
        else:
            if snake[i][1][1] == snake[i + 2][1][1] and snake[i][1][0] > snake[i + 2][1][0]:
                snake[i + 1][0] = liste_body[right]
            elif snake[i][1][1] == snake[i + 2][1][1]and snake[i][1][0] < snake[i + 2][1][0]:
                snake[i + 1][0] = liste_body[left]
            elif snake[i][1][0] == snake[i + 2][1][0] and snake[i][1][1] > snake[i + 2][1][1]:
                snake[i + 1][0] = liste_body[up]
            elif snake[i][1][0] == snake[i + 2][1][0]and snake[i][1][1] < snake[i + 2][1][1]:
                snake[i + 1][0] = liste_body[down]
    if snake[0][1][1] == snake[2][1][1] and snake[0][1][0] > snake[2][1][0]:
        snake[1][0] = liste_frame_body[right][move]
    elif snake[0][1][1] == snake[2][1][1] and snake[0][1][0] < snake[2][1][0]:
        snake[1][0] = liste_frame_body[left][move]
    elif snake[0][1][0] == snake[2][1][0] and snake[0][1][1] > snake[2][1][1]:
        snake[1][0] = liste_frame_body[down][move]
    elif snake[0][1][0] == snake[2][1][0] and snake[0][1][1] < snake[2][1][1]:
        snake[1][0] = liste_frame_body[up][move]
