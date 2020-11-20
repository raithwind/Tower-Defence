import pygame
import random
import settings

vect = pygame.math.Vector2

pygame.init()


# noinspection PyArgumentList
class Particle(pygame.sprite.Sprite):
    type = "particle"
    drag = 0.05

    # noinspection PyArgumentList
    def __init__(self, x, y, vx, vy, game):
        """
        :param x: int x coord
        :param y: int y coord
        :param vx: int/float x velocity
        :param vy: int/float y velocity
        :param game: Game()
        """
        pygame.sprite.Sprite.__init__(self)
        self.width = 10
        self.game = game
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.rect = self.image.get_rect()
        self.rect.center = vect(x, y)
        self.velx = vx
        self.vely = vy

    def update(self):
        distance = (vect(self.game.player.rect.center) - vect(self.rect.center)).length()
        if distance < settings.envelope:
            self.game.render_sprites.add(self)
        if self in self.game.render_sprites:
            if distance > settings.envelope:
                self.game.render_sprites.remove(self)
        self.rect.x += self.velx
        self.rect.y += self.vely
        if abs(self.velx) > 1.5:
            self.velx *= 1 - self.drag
            # print(f"x: {self.velx}")
        else:
            self.velx = 0
        if abs(self.vely) > 1.5:
            self.vely *= 1 - self.drag
            # print(f"y = {self.vely}")
        else:
            self.vely = 0
        if self.velx == 0 and self.vely == 0:
            if self in self.game.render_sprites:
                self.game.render_sprites.remove(self)
            self.game.all_sprites.remove(self)


# noinspection PyArgumentList
class Player(pygame.sprite.Sprite):
    drag = 1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.moves = None
        self.width = 10
        self.height = 40
        self.disp = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.SRCALPHA)
        self.image = pygame.Surface([self.width, self.height])
        self.image = pygame.image.load("test icon.png")
        self.image = self.image.convert()
        self.image.set_colorkey((0,0,220))
        #self.image.fill((100, 100, 100, 0))

        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.game = None
        self.count = 0
        self.target = vect(50, 50)

    def move(self, target):
        pass

    def update(self):
        # print(f"HHH {event.pos}")
        keys = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        x += self.game.camhandler.x
        y += self.game.camhandler.y
        pos = (x, y)
        radius, angle = (vect(pos)-vect(self.rect.center)).as_polar()
        print(f"Radius: {radius}, Angle: {angle}")
        if radius > 40:
            self.image = pygame.transform.rotate(self.orig_image, -angle+90)
            # Create a new rect with the center of the old rect.
            self.rect = self.image.get_rect(center=self.rect.center)
        if keys[0]:
            # find target position

             # noinspection PyArgumentList
            self.set_target(vect(pos))
        move = vect(self.target) - vect(self.rect.center)
        move_length = move.length()
        if move_length < 10:  # speed
            pass
        elif move_length != 0:
            move.normalize_ip()
            move = move * 10  # speed
            self.rect.center += move
        if self.count >= settings.FPS * 1:
            print(f"The FPS is: {self.game.clock.get_fps()} with {len(self.game.render_sprites)}")
            self.count = 0
        self.count += 1

    def set_target(self, target):
        self.target = vect(target)

    def spawn(self):
        self.game.all_sprites.add(Particle(self.rect.x, self.rect.y, 3, 3, self.game))


# noinspection PyArgumentList
class Tower(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        pygame.sprite.Sprite.__init__(self)
        self.width = 10
        self.game = game
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(settings.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = vect(pos)
        self.count = 0
        self.delay = 1  # random.randint(1, 101) / 10

    def spawn(self):
        self.game.all_sprites.add(Particle(self.rect.x, self.rect.y, 10, 10, self.game))

    def update(self):
        distance = (vect(self.game.player.rect.center) - vect(self.rect.center)).length()
        if self not in self.game.render_sprites:
            if distance < settings.envelope:
                self.game.render_sprites.add(self)
        if self in self.game.render_sprites:
            if distance > settings.envelope:
                self.game.render_sprites.remove(self)
        if self.count >= self.delay * settings.FPS:
            self.spawn()
            self.count = 0
        self.count += 1
