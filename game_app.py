import pygame
import pygame_gui

from main_menu_state import MainMenuState
from settings_state import SettingsState
from game_state import GameState

ICON = pygame.image.load('Troll Face.ico')  # assigns icon image to a variable
pygame.display.set_caption('dungeoen')  # changes the caption
pygame.display.set_icon(ICON)  # changes the icon


class GameApp:

    def __init__(self):
        pygame.init()

        self.window_surface = pygame.display.set_mode((800, 640))  # creates the window
        self.ui_manager = pygame_gui.UIManager((800, 640), 'theme.json')  # creates UI and includes any themes inside
        # a json file as one of the arguments
        self.clock = pygame.time.Clock()
        self.running = True  # Boolean condition for the while loop running the program.

        self.states = {'main_menu': MainMenuState(self.window_surface, self.ui_manager),
                       'settings': SettingsState(self.window_surface, self.ui_manager),
                       'game': GameState(self.window_surface)}  # creates the states dictionary so that different
        # states are selected

        self.active_state = self.states['main_menu']  # start the app in the main menu
        self.active_state.start()  # starts running the current active state.

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # if a user closes the window, the program will stop running
                    self.running = False
                # elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    # self.running = False  # user can close window with the esc key

                self.ui_manager.process_events(event)

                self.active_state.handle_events(event)

            self.ui_manager.update(time_delta)  # updates all the ui such as text and buttons

            self.active_state.update(time_delta)  # updates the current state that is running

            if self.active_state.transition_target is not None:  # these following if statements control state switching
                if self.active_state.transition_target in self.states:
                    self.active_state.stop()  # stops the active state from running if a transition target is found
                    self.active_state = self.states[
                        self.active_state.transition_target]  # selects the target from the states dictionary
                    self.active_state.start()  # starts running the targeted state.
                elif self.active_state.transition_target == 'quit':  # in main menu, when the quit button is
                    # pressed, the target is 'quit' then the loop will break and the program will end
                    self.running = False

            pygame.display.update()  # updates the display at the end of every pass


if __name__ == '__main__':  # runs the program on startup
    app = GameApp()
    app.run()
