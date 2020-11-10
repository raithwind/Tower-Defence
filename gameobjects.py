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
    drag = 0.1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.moves = None
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.velx = 0
        self.vely = 0
        self.vel = vect(0, 0)
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.acc = 3
        self.maxvel = 5
        self.game = None
        self.count = 0
        self.target = vect()

    def move(self, target):
        pass

    def update(self):
        move = vect(self.target) - vect(self.rect.center)
        move_length = move.length()
        if move_length < 10:  # speed
            self.rect.center = self.target
            # print(f"#### I am at {self.rect.center}")
        elif move_length != 0:
            move.normalize_ip()
            move = move * 10  # speed
            self.rect.center += move
        if self.count >= settings.FPS * 1:
            print(f"The FPS is: {self.game.clock.get_fps()} with {len(self.game.render_sprites)}")
            self.count = 0
        self.count += 1
        # print(dir(self.game.camera))

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
        self.game.all_sprites.add(Particle(self.rect.x, self.rect.y, 40, 40, self.game))

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


