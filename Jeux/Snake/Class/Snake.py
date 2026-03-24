from Library.Jeux.Snake.Front.assets import *
class Snake:


    def __init__(self):
        self.up = 0
        self.right = 1
        self.left = 2
        self.down = 3

        self.direction = 3
        lignes = [230, 275, 320, 365, 410, 455, 500, 545, 590, 635, 680, 725]
        colonnes = [30, 75, 120, 165, 210, 255, 300, 345, 390, 435, 480, 525]

        self.grille_cord = [[[i, j]
                            for i in colonnes]
                            for j in lignes]
        print(self.grille_cord)

        a,b,self.heads, self.bodys, self.tails, self.turn_horaires, self.turn_antis = load_assets()
        self.head = [self.heads[3],self.grille_cord[5][5]]
        self.body = [[self.bodys[3][0],self.grille_cord[5][6]],[self.bodys[3][0],self.grille_cord[5][7]]]
        self.tail = [self.tails[3][0],self.grille_cord[5][8]]
        self.whole = [self.head,self.body,self.tail]

    def __str__(self):
        return str(self.whole)

    def move(self, direction, whole):
        self.head = [self.heads[direction],self.head[1][0]-45]

