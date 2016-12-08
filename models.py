class Horse:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def animate(self, delta):
        if self.x < 630:
            self.x += 4

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.horseA1 = Horse(self, 37, 400)
        self.horseB1 = Horse(self, 20, 180)

    def animate(self, delta):
        self.horseA1.animate(delta)
        self.horseB1.animate(delta)