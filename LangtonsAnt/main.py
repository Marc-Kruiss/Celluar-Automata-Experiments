import pygame as pg


class App:
    def __init__(self, WIDTH=1600, HEIGHT=900, CELL_SIZE=12):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()

        self.CELL_SIZE = CELL_SIZE
        self.ROWS, self.COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
        self.grid = [[0 for col in range(self.COLS)] for row in range(self.ROWS)]

    def run(self):
        while True:
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    app = App()
    app.run()
