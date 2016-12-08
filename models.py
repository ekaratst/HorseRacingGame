import arcade.key

class HorseA:
    DIR_STAYSTILL_A = 0
    DIR_MOVE_A = 1

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction_a = HorseA.DIR_MOVE_A

    def switch_direction_a(self):
        if self.direction_a == HorseA.DIR_STAYSTILL_A:
            self.direction_a = HorseA.DIR_MOVE_A
        else:
            self.direction_a = HorseA.DIR_STAYSTILL_A

    def animate(self, delta):
        if self.x < 630:
            if self.direction_a == HorseA.DIR_STAYSTILL_A:
                self.x += 20

            self.direction_a = HorseA.DIR_MOVE_A

class HorseB:
    DIR_STAYSTILL_B = 0
    DIR_MOVE_B = 1

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction_b = HorseB.DIR_MOVE_B

    def switch_direction_b(self):
        if self.direction_b == HorseB.DIR_STAYSTILL_B:
            self.direction_b = HorseB.DIR_MOVE_B
        else:
            self.direction_b = HorseB.DIR_STAYSTILL_B

    def animate(self, delta):
        if self.x < 630:
            if self.direction_b == HorseB.DIR_STAYSTILL_B:
                self.x += 20

            self.direction_b = HorseB.DIR_MOVE_B

class Background:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.horseA1 = HorseA(self, 13, 315)
        self.horseB1 = HorseB(self, 13, 120)
        self.background = Background(self, 400, 300)

    def animate(self, delta):
        self.horseA1.animate(delta)
        self.horseB1.animate(delta)

    state_a = 1
    state_b = 1
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            self.horseA1.switch_direction_a()
            self.state_a = 1
        elif key == arcade.key.LEFT:
            self.horseA1.switch_direction_a()
            self.state_a = 2
        if key == arcade.key.D:
            self.horseB1.switch_direction_b()
            self.state_b = 1
        elif key == arcade.key.A:
            self.horseB1.switch_direction_b()
            self.state_b = 2

    def get_state_a(self):
        return self.state_a

    def get_state_b(self):
        return self.state_b
