class Horse:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def animate(self, delta):
        if self.x < 630:
            self.x += 4
        