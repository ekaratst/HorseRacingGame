import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)
        self.backgroung = arcade.Sprite('images/background.png')
        self.backgroung.set_position(400, 300)
        self.horseA1 = arcade.Sprite('images/racerA1.png')
        self.horseA1.set_position(37, 400)
        self.horseB1 = arcade.Sprite('images/racerB1.png')
        self.horseB1.set_position(20, 180)

    # def on_draw(self):
    #     arcade.start_render()

    def on_draw(self):
        arcade.start_render()
        self.backgroung.draw()
        self.horseA1.draw()
        self.horseB1.draw()

    def animate(self, delta):
        self.backgroung.set_position(self.backgroung.center_x, self.backgroung.center_y)
        self.horseA1.set_position(self.horseA1.center_x , self.horseA1.center_y)
        self.horseB1.set_position(self.horseB1.center_x, self.horseB1.center_y)


if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()