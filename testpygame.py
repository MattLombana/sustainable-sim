import os
import sys
import pygame as pg


class Control(object):
    def __init__(self,screen_size):
        pg.init()
        os.environ["SDL_VIDEO_CENTERED"] = "TRUE"
        self.screen = pg.display.set_mode(screen_size)
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def update(self):
        pass

    def draw(self):
        pass

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = Control((500,500))
    app.main_loop()
    pg.quit()
    sys.exit()