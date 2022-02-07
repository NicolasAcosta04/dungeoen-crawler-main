import pygame

from pygame_gui.elements import UIButton  # imports modules that are needed from the libraries used in the project
from pygame_gui import UI_BUTTON_PRESSED


class MainMenuState:  # class is initialized
    def __init__(self, window_surface, ui_manager):
        self.transition_target = None
        self.window_surface = window_surface  # variable has window_surface parameter that is used
        self.ui_manager = ui_manager  # takes the ui_manager variable from the parameter for use in main program
        self.title_font = pygame.font.Font(None, 64)  # sets title font for the main menu text

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        # creates all the button, background and text variables and sets them to none for use in the main menu
        self.start_game_button = None
        self.settings_button = None
        self.quit_button = None

    def start(self):
        self.transition_target = None
        self.background_surf = pygame.Surface((1200, 800))  # creates the background
        self.background_surf.fill((0, 0, 0))  # fills it in black
        self.title_text = self.title_font.render('Main Menu', True, (255, 255, 255))  # initialises text on the screen
        self.title_pos_rect = self.title_text.get_rect()  # 027 and 028 position the title in the desired location
        self.title_pos_rect.center = (400, 50)

        self.start_game_button = UIButton(pygame.Rect((325, 240), (150, 30)),
                                          'Start Game',
                                          self.ui_manager)  # initialises the start game button with position and size
        self.settings_button = UIButton(pygame.Rect((325, 280), (150, 30)),
                                        'Settings',
                                        self.ui_manager)  # initialises the settings button with position and size
        self.quit_button = UIButton(pygame.Rect((325, 320), (150, 30)),
                                    'Quit',
                                    self.ui_manager)  # initialises the quit button with position and size

    def stop(self):  # when the state is changed, all the elements on the screen are killed and deleted.
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None

        self.start_game_button.kill()
        self.start_game_button = None
        self.settings_button.kill()
        self.settings_button = None
        self.quit_button.kill()
        self.quit_button = None

    def handle_events(self, event):
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            if event.ui_element == self.start_game_button:
                self.transition_target = 'game'  # starts the game when the start game button is pressed
            elif event.ui_element == self.settings_button:
                self.transition_target = 'settings'  # goes to the settings menu when settings button is pressed
            elif event.ui_element == self.quit_button:
                self.transition_target = 'quit'  # quits game and closes window when quit button is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition_target = 'quit'

    def update(self, time_delta):
        self.window_surface.blit(self.background_surf, (0, 0))  # clear the window to the background surface
        self.window_surface.blit(self.title_text, self.title_pos_rect)  # stick the title at the top
        self.ui_manager.draw_ui(self.window_surface)  # draws all the ui on screen including buttons and text
