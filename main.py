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


GOALS: CS2 plant bomb, defuse, eliminate enemies

RULES: CS2 no going off map, no friendly fire, players take damage from stuff, 

FEEDBACK: Rocket league score goes up, boost meter, noise

FREEDOM: Fortnite: go anywhere, build anything, shoot, jump


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
        self.high_score = 0
        self.score = 0

    def load_data(self, map):
        self.game_dir = path.dirname(__file__)
        self.game_save_file = path.join(self.game_dir, "highscore.txt")

        self.img_dir = path.join(self.game_dir, 'images')
        # sound handling
        self.snd_dir = path.join(self.game_dir, 'audio')
        self.pickup_snd = pg.mixer.Sound(path.join(self.snd_dir, "pickup.wav"))
        self.map = Map(path.join(self.game_dir, map))

        try:
            with open(self.game_save_file, 'x', encoding="utf-8") as file:
                file.write("hello world!")
            print("file created successfully!")

        except FileExistsError:
            print("File already exists")

        with open(self.game_save_file, 'r') as file:
            try:
                self.high_score = int(file.read())
            except:
                # self.high_score = 0
                print("high score not read...")

    def new(self):
        self.load_data('level1.txt')
        print(self.map.data)
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_coins = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_particles = pg.sprite.Group()


        for row, tiles in enumerate(self.map.data):
            for col, tile, in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
        for row, tiles in enumerate(self.map.data):
            for col, tile, in enumerate(tiles):
                if tile == 'P':
                    self.player = Player(self, col, row)
        # pg.mixer.music.load(path.join(self.snd_dir, "Juhani Junkala_Stage 1.ogg"))
        # pg.mixer.music.play(loops=-1)
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
                if self.score > self.high_score:
                    with open(path.join(self.game_dir, self.game_save_file), 'w') as f:
                        f.write(str(self.score))
                if self.playing:
                    self.playing = False
                self.running = False
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def update(self):
        self.all_sprites.update()

    def draw(self):
        # this order matters: the first things are on the bottom because they are the first to be drawn
        # the last lines in this method are drawn on top or last
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(f"Frames per second:{1/self.dt}", 24, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text(f"Coins:{self.player.coins}", 24, WHITE, WIDTH/2, HEIGHT/7)
        self.draw_text(f"Score:{self.score}", 24, WHITE, WIDTH/2, HEIGHT/8)
        self.draw_text(f"High Score:{self.high_score}", 24, WHITE, WIDTH/2, HEIGHT/12)
        pg.display.flip()

if __name__ == "__main__":
    g = Game()

while g.running:
    g.new()
    g.run()