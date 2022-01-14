import pygame

from pygame_gui.elements import UIButton  # imports modules from the libraries used for buttons and ui
from pygame_gui import UI_BUTTON_PRESSED


class SettingsState:  # class is initialized
    def __init__(self, window_surface, ui_manager):
        self.transition_target = None
        self.window_surface = window_surface  # variable has window_surface parameter that is used
        self.ui_manager = ui_manager  # takes the ui_manager variable from the parameter for use in main program
        self.title_font = pygame.font.Font(None, 64)  # sets font for the title text

        self.background_surf = None  # creates all the ui attributes that are used in the settings
        self.title_text = None
        self.title_pos_rect = None

        self.back_button = None

    def start(self):
        self.transition_target = None
        self.background_surf = pygame.Surface((1200, 800))  # 800 640, creates background
        self.background_surf.fill((0, 0, 0))  # fills the background in the colour black
        self.title_text = self.title_font.render('Settings', True, (255, 255, 255))  # renders the text
        self.title_pos_rect = self.title_text.get_rect()  # positions the text in the desired position
        self.title_pos_rect.center = (400, 50)

        self.back_button = UIButton(pygame.Rect((550, 550), (200, 30)),
                                    'Back to main menu', self.ui_manager)  # creates back to main menu button and
        # puts it in the desired position

    def stop(self):  # when this state is no longer being ran, all the ui are killed and set to none
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None

        self.back_button.kill()
        self.back_button = None

    def handle_events(self, event):
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            if event.ui_element == self.back_button:
                self.transition_target = 'main_menu'  # if the user presses the back to main menu button, it should
                # take them to the main menu
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition_target = 'main_menu'  # if the user presses the esc key, the player goes to the main menu

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # stick the title at the top
        self.window_surface.blit(self.title_text, self.title_pos_rect)

        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI Bits


