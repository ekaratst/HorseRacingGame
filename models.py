import arcade.key

class Horse:
    DIR_STAYSTILL = 0
    DIR_MOVE = 1

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = Horse.DIR_MOVE

    def switch_direction(self):
        if self.direction == Horse.DIR_STAYSTILL:
            self.direction = Horse.DIR_MOVE
        else:
            self.direction = Horse.DIR_STAYSTILL

    def animate(self, delta):
        if self.x < 630:
            if self.direction == Horse.DIR_STAYSTILL:
                self.x += 4

            self.direction = Horse.DIR_MOVE
            # else:
            #     self.x += 0

class Background:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.horseA1 = Horse(self, 37, 400)
        self.horseB1 = Horse(self, 20, 180)
        self.background = Background(self, 400, 300)

    def animate(self, delta):
        self.horseA1.animate(delta)
        self.horseB1.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            self.horseA1.switch_direction()
        elif key == arcade.key.LEFT:
            self.horseA1.switch_direction()
        if key == arcade.key.D:
            self.horseB1.switch_direction()
        elif key == arcade.key.A:
            self.horseB1.switch_direction()