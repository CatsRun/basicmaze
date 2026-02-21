import arcade
"""This program is a simple maze controlled with arrow keys on the keybaord."""

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
MOVEMENT_SPEED = 2
SPRITE_SCALING_PLAYER = 1

# ***** change the player to not a ball****
class Player:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

        # lLists for player, keys, walls

    
    def draw(self):
        """ Draw the player """
        # *** change this to the player icon ***
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius, self.
                                  color)
            
    def on_update(self):
        """ Move the player """
        self.position_y += self.change_y
        self.position_x += self.change_x

        # When the player hits the edge, bounce off
        if self.position_x < self.radius:
            self.position_x = self.radius + 5

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius + 5

        if self.position_y < self.radius:
            self.position_y = self.radius + 5

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius + 5

# player can't pass through the wall. 
        # if self.position_y == wall - self.radious:
        #     self.change_y = wall - self.radious + 3

# class Walls:
#     """ Creates the walls """



class MazeGame(arcade.Window):
    """ Window the game is displayed and played in."""
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, title):
        """ Constructor """

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title)

        # background color
        arcade.set_background_color(arcade.color.SILVER_CHALICE)

        # create player
        # ************************************
        # *** change player to not  a ball ***
        # ************************************
        self.player = Player(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        self.clear()
        self.player.draw()
        

    def on_update(self, delta_time):
        self.player.on_update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0

def main():
    window = MazeGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Castle Maze")
    
    arcade.run()

if __name__== "__main__":
    main()