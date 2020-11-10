from gameobjects import *
import gameengine

player = Player()
game = gameengine.Game(player)
player.game = game
game.render_sprites.add(player)
keyhandler = gameengine.KeyHandler(game)

game.all_sprites.add(player)
# Game loop
game.run(keyhandler)
