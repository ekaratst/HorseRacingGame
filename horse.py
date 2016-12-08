import arcade
from models import World, Horse

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)
        self.backgroung = arcade.Sprite('images/background.png')
        self.backgroung.set_position(400, 300)

        self.horseA1_sprite = arcade.Sprite('images/racerA1.png')
        self.horseB1_sprite = arcade.Sprite('images/racerB1.png')
        self.world = World(width, height)

    def on_draw(self):
        arcade.start_render()
        self.backgroung.draw()
        self.horseA1_sprite.draw()
        self.horseB1_sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)
        self.backgroung.set_position(self.backgroung.center_x, self.backgroung.center_y)
        self.horseA1_sprite.set_position(self.world.horseA1.x, self.world.horseA1.y)
        self.horseB1_sprite.set_position(self.world.horseB1.x, self.world.horseB1.y)


if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()