import pygame
import player
import map_dict_draw
# trying to draw different tiles in layers
RED = (200, 0, 0)
BISQUE = "#FFE4C4"
BLACK = (0, 0, 0)


class GameState:
    def __init__(self, window_surface):
        self.transition_target = None
        self.window_surface = window_surface
        self.running = True

        self.title_font = pygame.font.Font(None, 64)
        self.instructions_font = pygame.font.Font(None, 32)

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.instructions_text = None
        self.instructions_text_pos_rect = None

        self.map = None
        self.player = None

    def start(self):
        self.transition_target = None
        self.running = True
        self.background_surf = pygame.Surface((800, 640))
        self.background_surf.fill(BISQUE)
        self.player = player.Player(self.window_surface, 300, 500)

        self.map = map_dict_draw.Map(self.window_surface, 1, 0)
        self.map.empty_floor()
        self.map.empty_wall()
        self.map.open_floor_file()
        self.map.open_wall_file()

        # self.title_text = self.title_font.render('The Game', True, (255, 255, 255))
        # self.title_pos_rect = self.title_text.get_rect()
        # self.title_pos_rect.center = (400, 50)
        #
        # self.instructions_text = self.instructions_font.render('Press ESC to return to main menu',
        #                                                        True, (255, 255, 255))
        #
        # self.instructions_text_pos_rect = self.instructions_text.get_rect()
        # self.instructions_text_pos_rect.center = (400, 100)

    def stop(self):
        self.running = False
        self.background_surf = None
        self.map = None
        # self.title_text = None
        # self.title_pos_rect = None
        # self.instructions_text = None
        # self.instructions_text_pos_rect = None

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
        # self.map.draw_wall()
        self.player.update(time_delta)
        # stick the title at the top
        # self.window_surface.blit(self.title_text, self.title_pos_rect)
        # stick the instructions below
        # self.window_surface.blit(self.instructions_text, self.instructions_text_pos_rect)
