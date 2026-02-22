import arcade
import random
"""This program is a simple maze controlled with arrow keys on the keybaord."""

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
MOVEMENT_SPEED = 2
SPRITE_SCALING_PLAYER = 1
SPRITE_SCALING_BOX = 1

# ***** change the player to not a ball****
class Player:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color, ):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

        # Attributes to store where our ball is
        

        # self.ball = arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.BANANA_YELLOW)
        # lLists for player, keys, walls
        # self.player_list = None
        # self.wall_list = None
    
        # # Set up the player
        # self.player_sprite = None

    # def setup():

    # def horizontal_wall( xAxis, yAxis, wdth, hght):
    #     """Build a  horizontal wall"""
    #     arcade.draw_rect_filled(arcade.XYWH(xAxis, yAxis, wdth, hght), arcade.csscolor.FIREBRICK)

    # def walls(horizontal_wall):
    #     horizontal_wall(0, 320, 200, 10)
    #     horizontal_wall(350, 320, 200, 10)


    def draw(self):

         # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        # print(self.wall_list[0,0])

        # Reset the score
        self.score = 0

        """ Draw the player """
        # *** change this to the player icon ***
        self.player_sprite = arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius, self.
                                  color)
        # self.player_sprite = arcade.Sprite("images/ladybug.png", SPRITE_SCALING_PLAYER)

        # self.ball_sprite = arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.BANANA_YELLOW)
        
        # self.ball = Player(50, 50, 3, 3, 15, arcade.color.AUBURN)
            
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

        # when ball hits the edge

        # self.ball_x += self.change_x 
        # self.ball_y += self.change_y

        # if self.ball_x < self.radius:
        #     self.ball_x = self.radius 

        # if self.ball_x > SCREEN_WIDTH - self.radius:
        #     self.ball_x = SCREEN_WIDTH - self.radius 

        # if self.ball_y < self.radius:
        #     self.ball_y = self.radius 

        # if self.ball_y > SCREEN_HEIGHT - self.radius:
        #     self.ball_y = SCREEN_HEIGHT - self.radius 


class Ball:
    def __init__(self, ball_x, ball_y, change_ball_x, change_ball_y, radius, color, ):

        self.ball_x = ball_x
        self.ball_y = ball_y
        self.change_ball_x = change_ball_x
        self.change_ball_y = change_ball_y
        self.radius = radius
        self.color = color

    def draw(self):

         # Sprite lists
        self.ball_list = arcade.SpriteList()

        """ Draw the ball """

        self.ball_sprite = arcade.draw_circle_filled(self.ball_x, self.ball_y, self.radius, self.color)


            
    def on_update(self):
        """ Move the ball """

        # when ball hits the edge

        self.ball_x += self.change_ball_x 
        self.ball_y += self.change_ball_y

        if self.ball_x < self.radius:
            self.change_ball_x *= -1

        if self.ball_x > SCREEN_WIDTH - self.radius:
            self.change_ball_x *= -1

        if self.ball_y < self.radius:
            self.change_ball_y *= -1

        if self.ball_y > SCREEN_HEIGHT - self.radius:
            self.change_ball_y *= -1
        
# repeat for other walls
# player can't pass through the wall. 
        # if self.position_y == wall - self.radious:
        #     self.change_y = wall - self.radious + 3

class Walls:
    """ Creates the walls """
def horizontal_wall( xAxis, yAxis, wdth, hght):
    """Build a  horizontal wall"""
    arcade.draw_rect_filled(arcade.XYWH(xAxis, yAxis, wdth, hght), arcade.csscolor.FIREBRICK)

def walls():
        horizontal_wall(0, 320, 200, 10)
        horizontal_wall(350, 320, 200, 10)

class MazeGame(arcade.Window):
    """ Window the game is displayed and played in."""
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, title):
        """ Constructor """
        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title)
        arcade.set_background_color(arcade.color.BLANCHED_ALMOND) 
        # self.background = None

        self.player = Player(50, 50, 0, 0, 15, arcade.color.AUBURN)
        self.ball = Ball(400, 320, 3, 4, 15, arcade.color.BLEU_DE_FRANCE)
       
        
    def setup(self):
        # load background image       
        try:
            self.background = arcade.load_texture("images/background.png")
        except Exception as e:
            print("Could not load background:", e)
            self.background = None  # fallback
        # self.background = arcade.load_texture( "images/background.png")
        

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        self.clear()
        # if self.background:
        #     arcade.draw_texture_rect(
        #         center_x=SCREEN_WIDTH / 2,
        #         center_y=SCREEN_HEIGHT / 2,
        #         width=SCREEN_WIDTH,
        #         height=SCREEN_HEIGHT,
        #         texture=self.background
        #     )

        self.player.draw()
        self.ball.draw()
                

        walls()

    def on_update(self, delta_time):
        self.player.on_update()
        self.ball.on_update()

        # wall_collision = arcade.check_for_collision(walls, 
        # self.player)

        # for walls in wall_collision:
        #     print("ouch")

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
    window.setup()
    arcade.run()

if __name__== "__main__":
    main()