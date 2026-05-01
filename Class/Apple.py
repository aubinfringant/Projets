import random

class Apple:
    def __init__(self, snake):
        self.position = []
        self.eaten = 0

    def random_position(self, snake):
        while True:
            skip = False
            position = (random.randrange(12), random.randrange(12))

            for k in range(len(snake.snake)):
                if position == snake.snake[k][1]:
                    skip = True


            if not skip and position not in self.position:
                self.add_to_bag(position)
                return position

    def add_to_bag(self, position):
        self.position.append(position)

    def remove_from_bag(self, position):
        self.position.remove(position)
        self.eaten += 1