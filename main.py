import pygame
import random
import settings
from gameobjects import Particle
from gameobjects import Player
import gameengine

player = Player()
game = gameengine.Game(player)
player.game = game

keyhandler = gameengine.KeyHandler(game)

for i in range(1,50):
    game.all_sprites.add(Particle(random.randint(10,settings.WIDTH-10),random.randint(10,settings.HEIGHT-10),10,10,game))


game.all_sprites.add(player)
## Game loop
game.run(keyhandler)


