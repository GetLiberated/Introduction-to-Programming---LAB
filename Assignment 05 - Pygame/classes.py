from pygame import *
from pygame.sprite import *


class Jet(Sprite):

    """initialize the jet"""
    def __init__(self, screen):
        Sprite.__init__(self)

        # load jet image
        self.image = image.load("battlejet.png")

        # resize image
        self.image = pygame.transform.scale(self.image, (90, 50))

        # create hit box for jet
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 50
        self.screen = screen

        # create jet speed
        self.move_speed = 6

        #fire rate speed
        self.firerates = 2

    def moveleft(self):
        self.rect.x -= self.move_speed
        display.flip()

    def moveright(self):
        self.rect.x += self.move_speed
        display.flip()

    def moveup(self):
        self.rect.y -= self.move_speed
        display.flip()

    def movedown(self):
        self.rect.y += self.move_speed
        display.flip()


class Star_bg:

    """initialize background"""
    def __init__(self,background):

        # load bg image for game
        self.background=image.load(background)

        # resize bg image
        self.background=pygame.transform.scale(self.background,(800,600))
        self.background_size=self.background.get_size()
        self.background_rect=self.background.get_rect()
        self.width,self.height=self.background_size

    """print bg"""
    def draw(self,screen,x,y):
        screen.blit(self.background,(x,y))


class Bullet(Sprite):

    """initialize bullet"""
    def __init__(self,screen, startx, starty):
        Sprite. __init__(self)
        self.startx = startx
        self.starty = starty

        # bullet speed
        self.speedx = 20

        # load bullet image
        self.image = pygame.image.load("bullets.png")

        # resize image
        self.image = pygame.transform.scale(self.image,(40,40))

        # create bullet hit box
        self.rect=self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty
        self.rect.center = (startx,starty)
        self.screen = screen

    """move bullet to right"""
    def movement(self):
        self.rect.left += self.speedx


class Asteroid(Sprite):

    """initialize the Asteroid"""
    def __init__(self, screen, width, height, speedx, startx, starty):
        Sprite.__init__(self)
        self.startx = startx
        self.starty = starty

        # create meteor speed
        self.speedx = speedx

        # load meteor image
        self.image = pygame.image.load("meteor.png")

        # resize image
        self.image = pygame.transform.scale(self.image, (width, height))

        # create hitbox for meteor
        self.rect = self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty
        self.screen = screen

    """move the Asteroid to the right"""
    def movement(self):
        self.rect.left -= self.speedx


class Button(Sprite):

    """initialize the start and quit button"""
    def __init__(self,image):
        Sprite. __init__(self)

        # load start or quit image
        self.button=pygame.image.load(image)

        # resize image
        self.button=pygame.transform.scale(self.button,(300,150))
