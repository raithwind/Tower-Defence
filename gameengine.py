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
        self.camhandler = Camera()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.player = player
        self.camera = self.camhandler.get_camera()
        # self.world = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.bg = bg
        self.world = self.bg
        self.clock = pygame.time.Clock()  # For syncing the FPS
        # group all the sprites together for ease of update
        self.all_sprites = pygame.sprite.Group()
        self.render_sprites = pygame.sprite.Group()
        self.count = 0
        self.buttons = []

    # Game loop
    def run(self, keyhandler):
        self.keyhandler = keyhandler
        self.running = True
        self.paused = False
        while self.running:
            self.keyhandler.get_events()

            if not self.paused:
                # 1 Process input/events
                self.clock.tick(settings.FPS)  # will make the loop run at the same speed all the time
                # 2 Update
                self.all_sprites.update()

                # 3 Draw/render
                self.camera.fill(settings.BLACK)
                self.world.blit(bg2, (0, 0))
                self.render_sprites.draw(self.world)
                # self.all_sprites.draw(self.world)
                self.camera.blit(self.world, (0, 0), self.camhandler.get_pos())
                self.camhandler.x = self.player.rect.x - settings.WIDTH / 2
                self.camhandler.y = self.player.rect.y - settings.HEIGHT/2
                print(f"{self.player.rect.y} {self.camhandler.y}")
                pygame.display.flip()
                # Done after drawing everything to the screen
                # pygame.display.update()
            else:
                Menus.Pause(self)
                # pauseimage = pygame.Surface((settings.WIDTH,settings.HEIGHT))
                # pauseimage.fill(settings.WHITE)
                # self.camera.blit(pauseimage,(0,0))
                # pygame.display.flip()
        pygame.quit()


class Camera:
    def __init__(self):
        self.camera = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))  # ,pygame.FULLSCREEN)
        pygame.display.set_caption("Tower Defense")

        self.x = 0
        self.y = 0

    def get_pos(self):
        return (self.x, self.y, settings.WIDTH, settings.HEIGHT)

    def get_camera(self):
        return self.camera

# def Renderer:
#     def __init__(self,game,sprte):
#         self.game = game
#         self.sprte = sprte
#
#     def run(self):
#         distance =  vect(self.game.player.rect.center) - vect(self.sprte.rect.center)
#         distance = distance.length()
#         if distance < settings.envelope:
#             if self.sprte not in self.game.render_sprites:
#                 self.game.render_sprites.add(self.sprte)
#         if distance > settings.envelope:
#             if self.sprte in self.game.render_sprites:
#                 self.game.render_sprites.remove(self.sprte)
#