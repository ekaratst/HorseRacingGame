import arcade
from models import Horse

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)
        self.backgroung = arcade.Sprite('images/background.png')
        self.backgroung.set_position(400, 300)

        self.horseA1 = Horse(37, 400)
        self.horseA1_sprite = arcade.Sprite('images/racerA1.png')
        #self.horseA1.set_position(37, 400)
        self.horseB1 = Horse(20, 180)
        self.horseB1_sprite = arcade.Sprite('images/racerB1.png')
        #self.horseB1.set_position(20, 180)

    def on_draw(self):
        arcade.start_render()
        self.backgroung.draw()
        self.horseA1_sprite.draw()
        self.horseB1_sprite.draw()

    def animate(self, delta):
        horseA1 = self.horseA1
        horseB1 = self.horseB1

        horseA1.animate(delta)
        horseB1.animate(delta)
        self.backgroung.set_position(self.backgroung.center_x, self.backgroung.center_y)
        self.horseA1_sprite.set_position(horseA1.x, horseA1.y)
        self.horseB1_sprite.set_position(horseB1.x, horseB1.y)


if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()