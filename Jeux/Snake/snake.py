from Jeux.Snake.Front.display import *
from Class.Snake import *
from Class.Apple import *

def main():
    snake = Snake()
    apple = Apple(snake)
    intro(snake, apple)

    clock = pygame.time.Clock()

    while len(apple.position) < 4:
        apple.random_position(snake)

    while True:
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
            restart = game_over(apple.eaten)
            if restart:
                return main()

        if snake.snake[0][1] in apple.position:
            snake.grow = True
            apple.remove_from_bag(snake.snake[0][1])

            if len(snake.snake) + len(apple.position) <= 143:
                apple.random_position(snake)

        affichage_snake(snake, apple)

        clock.tick(4)

start = main_menu()
if start:
    main()