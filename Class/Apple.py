import random

class Apple:
    def __init__(self, snake):
        self.position = []
        self.eaten = 0

    def random_position(self, snake):
        """
        Génère une position aléatoire valide pour une nouvelle pomme.
        Positions valides :
        - Les positions hors limites (0-11, 0-11)
        - Les positions occupées par des segments du serpent
        - Les positions où une pomme existe déjà
        Ajoute automatiquement la pomme à la position trouvée.
        """
        while True:
            skip = False
            position = (random.randrange(12), random.randrange(12))

            for k in range(len(snake.snake)):
                if position == snake.snake[k][1]:
                    skip = True


            if not skip and position not in self.position:
                self.add_to_bag(position)

    def add_to_bag(self, position):
        """
        Ajoute une pomme à la liste des positions actives.
        """
        self.position.append(position)

    def remove_from_bag(self, position):
        """
        Retire une pomme de la liste et augmente le compteur de pommes mangées.
        """
        self.position.remove(position)
        self.eaten += 1