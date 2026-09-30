# This file was created by: Chris Cozort
# Code inspired by game dev Chris Bradfield at Kids Can Code

import pygame as pg
from os import path
from sprites import *
from settings import *
from utils import *

'''
Why are we making game a class?
Why is it capitalized?
What is init?
What is pass?

Data types: boolean, JSON, strings, 

Input (events): Keyboard, mouse, right click, voice, 
power button, eye tracking, camera, gyroscoping, electrostatic, location, volume, 
microphone - zelda game where you blow out a candle with the mic

Process: cursor position, position of the player, score, enemy position, velocity
aim in FPS, 

Output: Graphics - things are drawn, sounds: jump, power up, walking, haptics


'''

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        print("game initialized...")
        pg.display.set_caption(TITLE)
        self.running = True
        self.playing = True
        self.clock = pg.time.Clock()

    def load_data(self, map):
        self.game_dir = path.dirname(__file__)
        self.img_dir = path.join(self.game_dir, 'images')
        self.snd_dir = path.join(self.game_dir, 'audio')
        self.map = Map(path.join(self.game_dir, map))

    def new(self):
        self.load_data('level1.txt')
        print(self.map.data)
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()


        for row, tiles in enumerate(self.map.data):
            for col, tile, in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'M':
                    pass
                # if tile == 'P':
                #     Player(self, col, row)
        for row, tiles in enumerate(self.map.data):
            for col, tile, in enumerate(tiles):
                if tile == 'P':
                    Player(self, col, row)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()
        
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

if __name__ == "__main__":
    g = Game()

while g.running:
    g.new()
    g.run()