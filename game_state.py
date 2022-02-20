import pygame  # imports the pygame library
import player  # imports player class from the player.py file
import map_dict_draw  # imports the map drawing class from the map_dict_draw
RED = (200, 0, 0)  # RGB value for red assigned to the variable RED
BISQUE = "#FFE4C4"  # hexadecimal value of the colour bisque assigned to the variable BISQUE
BLACK = (0, 0, 0)  # RGB value for black assigned to the variable BLACK


class GameState:  # class is initialized
    def __init__(self, window_surface):
        self.transition_target = None
        self.window_surface = window_surface  # variable has window_surface parameter that is used
        self.running = True

        self.background_surf = None

        self.map = None
        self.player = None

    def start(self):
        self.transition_target = None
        self.running = True
        self.background_surf = pygame.Surface((800, 640))  # 800 640
        self.background_surf.fill(BLACK)
        self.player = player.Player(self.window_surface, 300, 500)

        self.map = map_dict_draw.Map(self.window_surface, 1, 0)
        self.map.empty_floor()
        self.map.empty_wall()
        self.map.open_floor_file()
        self.map.open_wall_file()

    def stop(self):
        self.running = False
        self.background_surf = None
        self.map = None
        self.player = None

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition_target = 'main_menu'
        self.player.on_key_press(event)
        self.player.on_key_release(event)

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # call the player and the relevant functions
        self.map.draw()
        self.player.draw(self.window_surface)
        self.player.update(time_delta)
