from Jeux.Snake.Front.display import *
from Class.Snake import *
from Class.Apple import *

fondu()
while main_menu():
    """
    Skip main_menu().
    """
    while True:
        """
        Initialisation du programme
        """
        snake = Snake()
        apple = Apple(snake)
        intro(snake, apple)

        clock = pygame.time.Clock()

        while len(apple.position) < 4:
            apple.random_position(snake)

        while True:
            """
            Boucle principale
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        snake.turn((0, -1))
                    elif event.key == pygame.K_RIGHT:
                        snake.turn((0, 1))
                    elif event.key == pygame.K_UP:
                        snake.turn((-1, 0))
                    elif event.key == pygame.K_DOWN:
                        snake.turn((1, 0))

            if not snake.move():
                if display_game_over(apple.eaten):
                    break


            if snake.snake[0][1] in apple.position:
                snake.grow = True
                apple.remove_from_bag(snake.snake[0][1])

                if len(snake.snake) + len(apple.position) <= 143:
                    apple.random_position(snake)

            display_all(snake, apple)

            clock.tick(4)