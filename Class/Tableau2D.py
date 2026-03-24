class Tableau2D:
    def __init__(self, width, height):
        self.tableau = [[0] * width for _ in range(height)]

    def __str__(self):
        return "\n".join(str(ligne) for ligne in self.tableau)

