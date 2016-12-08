import arcade
from models import World, HorseA, HorseB

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)
        self.world = World(width, height)
        self.background_sprite = ModelSprite('images/background.png', model=self.world.background)
        self.horseA1_sprite = ModelSprite('images/racerA1.png', model=self.world.horseA1)
        self.horseB1_sprite = ModelSprite('images/racerB1.png', model=self.world.horseB1)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_draw(self):
        arcade.start_render()
        self.background_sprite.draw()
        if self.world.getState_A() == 1:
            self.getSwitchBegin_A()
            self.horseA1_sprite.draw()
        elif self.world.getState_A() == 2:
            self.getSwitchAfter_A()
            self.horseA1_sprite.draw()
        if self.world.getState_B() == 1:
            self.getSwitchBegin_B()
            self.horseB1_sprite.draw()
        elif self.world.getState_B() == 2:
            self.getSwitchAfter_B()
            self.horseB1_sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)

    def getSwitchAfter_A(self):
        self.horseA1_sprite = ModelSprite('images/racerA2.png', model=self.world.horseA1)
        return  self.horseA1_sprite

    def getSwitchBegin_A(self):
        self.horseA1_sprite = ModelSprite('images/racerA1.png', model=self.world.horseA1)
        return  self.horseA1_sprite

    def getSwitchAfter_B(self):
        self.horseB1_sprite = ModelSprite('images/racerB2.png', model=self.world.horseB1)
        return  self.horseA1_sprite

    def getSwitchBegin_B(self):
        self.horseB1_sprite = ModelSprite('images/racerB1.png', model=self.world.horseB1)
        return  self.horseA1_sprite

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()