from Library.Jeux.Snake.Front.display import *
from Library.Jeux.Snake.Class.Snake import *

snake = Snake()
print(snake)

running = True
while running:
    running = main_menu()
    if running:
        running = intro(snake)
        while running:
            running = start(snake)

pygame.quit()