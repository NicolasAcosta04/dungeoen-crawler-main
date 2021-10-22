import pygame
import map_dict


class MapDraw:
    def __init__(self):
        self.world_data = []
        self.rows = 20
        self.cols = 25

    def empty_list(self):
        for row in range(self.rows):
            r = [000] * self.cols
            self.world_data.append(r)
        print(self.world_data)

    @classmethod
    def run(cls):
        pass


if __name__ == "__main__":
    app = MapDraw
    app.run()
