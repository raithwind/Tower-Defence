from KeyHandler import *
import Menus

# initialize pygame
pygame.init()
pygame.mixer.init()
pygame.font.init()

# set some images
bg = pygame.image.load("view_topdown.png")
dts = bg.get_rect().size
bg = pygame.transform.scale(bg, (dts[0] * 5, dts[1] * 5))
bg2 = pygame.transform.scale(bg, (dts[0] * 5, dts[1] * 5))
# vector math shortening
vect = pygame.math.Vector2


class Menu:
    def __init__(self, game):
        self.game = game


class Game:
    def __init__(self, player):
        self.player = player
        self.camhandler = Camera(self)

        self.font = pygame.font.SysFont("Comic Sans MS", 30)

        self.camera = self.camhandler.get_camera()
        self.bg = bg
        self.gamestate = {"paused":False, "playing":False, "menu":True, "cutscene":False}
        self.world = self.bg
        self.clock = pygame.time.Clock()  # For syncing the FPS
        # group all the sprites together for ease of update
        self.all_sprites = pygame.sprite.Group()
        self.render_sprites = pygame.sprite.Group()
        self.count = 0
        self.buttons = []
        self.mouseoffset = (0,0)
    # Game loop
    def Render(self):
        self.camera.fill(settings.BLACK)
        self.world.blit(bg2, (0, 0))
        self.render_sprites.draw(self.world)
        self.camera.blit(self.world, (0, 0), self.camhandler.get_pos())
        self.camhandler.x = self.player.rect.centerx - settings.WIDTH / 2
        self.camhandler.y = self.player.rect.centery - settings.HEIGHT / 2
        pygame.display.update()

    def run(self, keyhandler):
        self.keyhandler = keyhandler
        self.running = True

        while self.running:
            self.keyhandler.get_events()
            if not self.gamestate["playing"]:
                Menus.Start(self)
            if not self.gamestate["paused"] and self.gamestate["playing"]:
            #if not self.paused and self.playing:
                # 1 Process input/events
                self.clock.tick(settings.FPS)  # will make the loop run at the same speed all the time
                # 2 Update
                self.all_sprites.update()

                # 3 Draw/render
                self.Render()
                #pygame.display.flip()
                # Done after drawing everything to the screen
                #
            if self.gamestate["paused"]:
                Menus.Pause(self)


        pygame.quit()


class Camera:
    def __init__(self,game):
        self.game = game
        self.camera = self.game.player.disp #pygame.display.set_mode((settings.WIDTH, settings.HEIGHT),pygame.SRCALPHA)#, pygame.FULLSCREEN)
        pygame.display.set_caption("Tower Defense")

        self.x = 0
        self.y = 0

    def get_pos(self):
        return (self.x, self.y, settings.WIDTH, settings.HEIGHT)

    def get_camera(self):
        return self.camera

