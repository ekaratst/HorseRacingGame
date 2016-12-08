import arcade.key

class HorseA:
    DIR_STAYSTILL_A = 0
    DIR_MOVE_A = 1

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction_A = HorseA.DIR_MOVE_A

    def switch_direction_A(self):
        if self.direction_A == HorseA.DIR_STAYSTILL_A:
            self.direction_A = HorseA.DIR_MOVE_A
        else:
            self.direction_A = HorseA.DIR_STAYSTILL_A

    def animate(self, delta):
        if self.x < 630:
            if self.direction_A == HorseA.DIR_STAYSTILL_A:
                self.x += 4

            self.direction_A = HorseA.DIR_MOVE_A

class HorseB:
    DIR_STAYSTILL_B = 0
    DIR_MOVE_B = 1

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction_B = HorseB.DIR_MOVE_B

    def switch_direction_B(self):
        if self.direction_B == HorseB.DIR_STAYSTILL_B:
            self.direction_B = HorseB.DIR_MOVE_B
        else:
            self.direction_B = HorseB.DIR_STAYSTILL_B

    def animate(self, delta):
        if self.x < 630:
            if self.direction_B == HorseB.DIR_STAYSTILL_B:
                self.x += 4

            self.direction_B = HorseB.DIR_MOVE_B

class Background:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.horseA1 = HorseA(self, 37, 400)
        self.horseB1 = HorseB(self, 20, 180)
        # self.horseA2 = HorseA(self, 37, 400)
        # self.horseB2 = HorseB(self, 20, 180)
        self.background = Background(self, 400, 300)

    def animate(self, delta):
        self.horseA1.animate(delta)
        # self.horseA2.animate(delta)
        self.horseB1.animate(delta)
        # self.horseB2.animate(delta)

    state_a = 1
    state_b = 1
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            self.horseA1.switch_direction_A()
            self.state_a = 1
        elif key == arcade.key.LEFT:
            self.horseA1.switch_direction_A()
            self.state_a = 2
        if key == arcade.key.D:
            self.horseB1.switch_direction_B()
            self.state_b = 1
        elif key == arcade.key.A:
            self.horseB1.switch_direction_B()
            self.state_b = 2

    def getState_A(self):
        return self.state_a

    def getState_B(self):
        return self.state_b
