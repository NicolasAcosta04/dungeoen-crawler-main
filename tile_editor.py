import pygame  # imports the pygame library
import button  # imports the button class from button.py
import csv  # imports the csv library for saving files in the csv format

pygame.init()  # initialises the pygame modules

clock = pygame.time.Clock
FPS = 60  # caps the fps to 60

SCREEN_WIDTH = 800  # these variables set the dimensions for the game window
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')  # changes the caption of the window

# define game variables
ROWS = 20  # sets how many rows will be in the grid
MAX_COLS = 25  # sets the maximum amount of columns that will be displayed in the grid
TILE_SIZE = SCREEN_HEIGHT // ROWS  # calculates the tile size
TILE_TYPES = 6  # sets how many tiles there will be in the editor
level = 0  # sets level to zero for creating the level data
current_tile = 0  # sets the current tile selected to zero by default
# load images
# store tiles in a list
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'Foozle_2DT0002_Lucifer_Tileset_1_Pixel_Art/Png/tile/{x}.png').convert_alpha()
    img = pygame.transform.smoothscale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)  # takes all the images from the folder and adds them to the img_list

save_img = pygame.image.load('save_btn.png').convert_alpha()  # loads the images for the save and load buttons
load_img = pygame.image.load('load_btn.png').convert_alpha()

GREEN = (144, 201, 120)  # sets the RGB values for green, white, and red and assigning them to variables
WHITE = (255, 255, 255)
RED = (200, 25, 25)
BISQUE = "#FFE4C4"  # sets the hexadecimal value for bisque and assigns this to a variable

# define font
font = pygame.font.SysFont('Comic Sans', 30)

# create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * MAX_COLS  # fills the entire empty world data list with -1, which means a tile is empty
    world_data.append(r)

# create ground
for tile in range(0, MAX_COLS):
    world_data[ROWS - 1][tile] = 0  # the bottom row of the list is filled with 0, which is a ground tile


# function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_bg():
    screen.fill(GREEN)  # fills in the background in the colour green


def draw_grid():  # creates the grid for placing tiles
    # vertical lines
    for c in range(MAX_COLS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT))
    # horizontal lines
    for c in range(ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))


# function for drawing world tiles
def draw_world():  # goes through the world_data list and blits each tile onto the screen if tile >= 0, as -1 is empty
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                screen.blit(img_list[tile], (x * TILE_SIZE, y * TILE_SIZE))


# create buttons
# store buttons in a list
save_button = button.Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + LOWER_MARGIN - 50, save_img, 1)  # creates save button
load_button = button.Button(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT + LOWER_MARGIN - 50, load_img, 1)  # creates the load
# button and sets the position
button_list = []  # button list is set and made empty for buttons of all the tiles in the grid in the editor
button_col = 0
button_row = 0
for i in range(len(img_list)):
    tile_button = button.Button(SCREEN_WIDTH + (75 * button_col) + 50, (75 * button_row) + 50, img_list[i], 1)
    button_list.append(tile_button)  # creates a button for every tile in the grid and appends them to a list
    button_col += 1
    if button_col == 3:
        button_row += 1
        button_col = 0

run = True  # condition for the main game loop
while run:

    draw_bg()  # background is drawn
    draw_grid()  # grid is drawn
    draw_world()  # the ground tiles are drawn in the last row of the world_data file
    draw_text(f'level: {level}', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 90)  # displays current level
    draw_text('Press UP or DOWN to change level', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 60)
    #  text that shows how to navigate the editor when changing which level they want to edit

    # save and load data
    if save_button.draw(screen):
        # save level data
        with open(f'level{level}_data.csv', 'w', newline='') as csvfile:  # opens file you want to save data in based
            # on level number
            writer = csv.writer(csvfile, delimiter=',')  # separates all the data with commas
            for row in world_data:  # writes the data into the file, line by line
                writer.writerow(row)

    if load_button.draw(screen):
        # load in level data
        with open(f'level{level}_data.csv',  newline='') as csvfile:  # opens file based on level number
            reader = csv.reader(csvfile, delimiter=',')  # reads the data within the commas
            for x, row in enumerate(reader):  # changes row once all the data in a row is written
                for y, tile in enumerate(row):  # for every tile in a row, the data is read and written and drawn in
                    # the level
                    world_data[x][y] = int(tile)

    # draw tile panel and tiles
    pygame.draw.rect(screen, BISQUE, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))
    # choose a tile
    button_count = 0
    for button_count, i in enumerate(button_list):  # draws all the buttons onto the screen
        if i.draw(screen):
            current_tile = button_count

    # highlight selected tile
    pygame.draw.rect(screen, RED, button_list[current_tile].rect, 3)

    # add new tiles to the screen
    # get mouse position
    pos = pygame.mouse.get_pos()
    x = pos[0] // TILE_SIZE
    y = pos[1] // TILE_SIZE

    # check that the coordinates are in the tile area
    if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
        # update tile value
        if pygame.mouse.get_pressed()[0] == 1:
            if world_data[y][x] != current_tile:
                world_data[y][x] = current_tile  # when you have a tile from the right selected and you left click on a
                # tile in the grid, the tile is placed in that location
        if pygame.mouse.get_pressed()[2] == 1:
            world_data[y][x] = -1  # if you hover over a placed tile and right click it, the value of the tile selected
            # will be set to -1, effectively deleting the tile

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # when the window is closed, the program will stop running
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1  # when the up arrow key is pressed, the level number is increased by one so that the next
                # level up can be edited
            if event.key == pygame.K_DOWN and level > 0:
                level -= 1  # when the down arrow key is pressed, the level number is decreased by one unless the level
                # number is already zero
            if event.key == pygame.K_ESCAPE:
                run = False  # when the escape key on the keyboard is pressed, the program will stop running and the
                # window will close

    pygame.display.update()  # the display.update() method will update all the processes on screen at the end of every
    # pass in the loop

pygame.quit()  # quits the program when the runtime loop ends
