import pygame
import random
import settings
from gameobjects import Particle
import gameengine

game = gameengine.Game()
keyhandler = gameengine.KeyHandler(game)

for i in range(1,50):
    game.all_sprites.add(Particle(random.randint(10,settings.WIDTH-10),random.randint(10,settings.HEIGHT-10),random.randint(1,20),random.randint(1,20),game))


## Game loop
game.run(keyhandler)


