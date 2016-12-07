import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.horse = arcade.Sprite('images/horse1.png')
        self.horse.set_position(100, 500)

    def on_draw(self):
        arcade.start_render()

    def on_draw(self):
        arcade.start_render()

        self.horse.draw()

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()