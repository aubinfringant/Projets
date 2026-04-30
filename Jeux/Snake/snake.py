from Jeux.Snake.Front.display import *
from Jeux.Snake.Class.Snake import *

snake = Snake()

running = True
while running:
    running = main_menu()
    if running:
        running = intro(snake)
        while running:
            running = start(snake)

pygame.quit()