import arcade.key

class HorseA:
    DIR_STAYSTILL_A = 0
    DIR_MOVE_A = 1

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction_a = HorseA.DIR_MOVE_A
        self.state_game_a = True

    def switch_direction_a(self):
        if self.direction_a == HorseA.DIR_STAYSTILL_A:
            self.direction_a = HorseA.DIR_MOVE_A
        else:
            self.direction_a = HorseA.DIR_STAYSTILL_A

    def animate(self, delta):
        if self.x < 633:
            self.state_game_a = True
            if self.direction_a == HorseA.DIR_STAYSTILL_A:
                self.x += 20
                print(self.x)
            self.direction_a = HorseA.DIR_MOVE_A
        else:
            self.state_game_a = False

    def get_state_game_a(self):
        return self.state_game_a

class HorseB:
    DIR_STAYSTILL_B = 0
    DIR_MOVE_B = 1


    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction_b = HorseB.DIR_MOVE_B
        self.state_game_b = True

    def switch_direction_b(self):
        if self.direction_b == HorseB.DIR_STAYSTILL_B:
            self.direction_b = HorseB.DIR_MOVE_B
        else:
            self.direction_b = HorseB.DIR_STAYSTILL_B

    def animate(self, delta):
        if self.x < 630:
            self.state_game_b = True
            if self.direction_b == HorseB.DIR_STAYSTILL_B:
                self.x += 20
            self.direction_b = HorseB.DIR_MOVE_B
        else:
            self.state_game_b = False

    def get_state_game_b(self):
        return self.state_game_b

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
    state_right_press = True
    state_left_press = False
    state_d_press = True
    state_a_press = False

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT and self.state_right_press == True:
            self.horseA1.switch_direction_a()
            self.state_right_press = False
            self.state_left_press = True
            self.state_a = 1
            self.state_press = False
        elif key == arcade.key.LEFT and self.state_left_press == True:
            self.horseA1.switch_direction_a()
            self.state_right_press = True
            self.state_left_press = False
            self.state_a = 2
        if key == arcade.key.D and self.state_d_press == True:
            self.horseB1.switch_direction_b()
            self.state_d_press = False
            self.state_a_press = True
            self.state_b = 1
        elif key == arcade.key.A and self.state_a_press == True:
            self.horseB1.switch_direction_b()
            self.state_d_press = True
            self.state_a_press = False
            self.state_b = 2

    def get_state_a(self):
        return self.state_a

    def get_state_b(self):
        return self.state_b
