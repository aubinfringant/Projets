from Jeux.Snake.Front.assets import *
class Snake:

    def __init__(self):

        self.grow = False
        self.direction = [(0,-1)]
        self.old_direction = self.direction[0]

        lignes = [230, 275, 320, 365, 410, 455, 500, 545, 590, 635, 680, 725]
        colonnes = [30, 75, 120, 165, 210, 255, 300, 345, 390, 435, 480, 525]

        self.grid_cord = [[(i, j)
                           for i in colonnes]
                          for j in lignes]

        self.grid_index = [(i,j)
                           for i in range(len(lignes))
                           for j in range(len(lignes))]

        self.apple, self.grid, self.heads, self.bodys, self.tails, self.turn_horaires, self.turn_antis = load_assets()


        self.snake = [[self.heads[3], (5, 5)],
                      [self.bodys[3][0], (5, 6)],
                      [self.bodys[3][0], (5, 7)],
                      [self.tails[3][0], (5, 8)]]

    def get_cord(self, segment):
        """
        Retourne les coordonnées en pixels d'un segment du serpent.
        :return: Tuple (x, y) en pixels
        """
        i, j = self.snake[segment][1]
        return self.grid_cord[i][j]

    def get_grid_cord(self, i, j):
        """
        Retourne les coordonnées en pixels pour un indice de grille.
        :return: Tuple (x, y) en pixels
        """
        return self.grid_cord[i][j]

    def turn(self, direction):
        """
        Ajoute une direction à la queue des directions.
        Empêche les virages interdits (sens inverse ou répétition).
        Limite à maximum 2 directions en queue (pour éviter les bugs de timing).
        """
        last_input = self.direction[0]
        opposite_direction = (-last_input[0], -last_input[1])

        if direction != opposite_direction and direction != last_input and len(self.direction) < 2:
            self.direction.insert(0, direction)


    def get_img_idx(self):
        """
        Détermine l'index d'image correspondant à la direction actuelle.
        :return: 0=haut, 1=droite, 2=bas, 3=gauche
        """
        if self.direction[0] == (0, -1):
            img_idx = 3
        elif self.direction[0] == (0, 1):
            img_idx = 1
        elif self.direction[0] == (-1, 0):
            img_idx = 0
        elif self.direction[0] == (1, 0):
            img_idx = 2

        return img_idx

    def get_body_img(self):
        """
        Retourne l'image appropriée du corps lors d'un virage.
        Détecte les changements de direction et retourne l'image du virage correspondant.
        :return: Image pygame du segment de corps
        """

        if self.old_direction == (0, 1) and self.direction[0] == (-1, 0):
            body_img = self.turn_antis[2]  # right up
        elif self.old_direction == (0, -1) and self.direction[0] == (-1, 0):
            body_img = self.turn_horaires[2]  # left up

        elif self.old_direction == (0, 1) and self.direction[0] == (1, 0):
            body_img = self.turn_horaires[0]  # right down
        elif self.old_direction == (0, -1) and self.direction[0] == (1, 0):
            body_img = self.turn_antis[0]  # left down

        elif self.old_direction == (-1, 0) and self.direction[0] == (0, -1):
            body_img = self.turn_antis[3]  # up -> left
        elif self.old_direction == (1, 0) and self.direction[0] == (0, -1):
            body_img = self.turn_horaires[1]  # down left

        elif self.old_direction == (-1, 0) and self.direction[0] == (0, 1):
            body_img = self.turn_horaires[3]  # up right
        elif self.old_direction == (1, 0) and self.direction[0] == (0, 1):
            body_img = self.turn_antis[1]  # down right

        return body_img

    def get_tail_img_idx(self):
        """
        Détermine l'index d'image de la queue selon sa direction avec
        l'avant dernier segment.
        :return: 0=haut, 1=droite, 2=bas, 3=gauche
        """
        tail_x, tail_y = self.snake[-1][1]
        prev_x, prev_y = self.snake[-2][1]
        tail_dir_x = prev_x - tail_x
        tail_dir_y = prev_y - tail_y

        if (tail_dir_x, tail_dir_y) == (0, -1):
            tail_img_idx = 3  # haut
        elif (tail_dir_x, tail_dir_y) == (0, 1):
            tail_img_idx = 1  # bas
        elif (tail_dir_x, tail_dir_y) == (-1, 0):
            tail_img_idx = 0  # gauche
        elif (tail_dir_x, tail_dir_y) == (1, 0):
            tail_img_idx = 2  # droite

        return tail_img_idx

    def move(self):
        """
        Bouge le serpent d'une case dans la direction actuelle.
        Détecte les collisions (murs ou auto-collision) et gère la croissance.
        Met à jour les images en fonction des virages.
        :return: Boolean - True si mouvement réussi, False si collision
        """
        head_x, head_y = self.snake[0][1]
        delta_x, delta_y = self.direction[0]
        new_head_index = (head_x + delta_x, head_y + delta_y)
        img_idx = self.get_img_idx()
        new_head = [self.heads[img_idx], new_head_index]

        for i,segment in enumerate(self.snake):
            if i == len(self.snake)-1 and not self.grow:
                continue
            if new_head[1] == segment[1]:
                return False

        if not (0 <= new_head[1][0] <= 11 and 0 <= new_head[1][1] <= 11):
            return False

        if self.old_direction != (delta_x, delta_y):
            body_img = self.get_body_img()
        else:
            body_img = self.bodys[img_idx][0]

        self.snake[0][0] = body_img
        self.snake.insert(0, new_head)

        if self.grow:
            self.grow = False
        else:
            self.snake.pop()

        tail_img_idx = self.get_tail_img_idx()
        self.snake[-1][0] = self.tails[tail_img_idx][0]

        self.old_direction = (delta_x, delta_y)

        if len(self.direction) > 1:
            self.direction.pop()

        return True

    def __str__(self):
        return str(self.snake)