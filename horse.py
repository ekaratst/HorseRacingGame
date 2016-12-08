import arcade
from models import World, Horse

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
        self.backgroung_sprite = ModelSprite('images/background.png', model=self.world.background)
        self.horseA1_sprite = ModelSprite('images/racerA1.png', model=self.world.horseA1)
        self.horseB1_sprite = ModelSprite('images/racerB1.png', model=self.world.horseB1)


    def on_draw(self):
        arcade.start_render()
        self.backgroung_sprite.draw()
        self.horseA1_sprite.draw()
        self.horseB1_sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()