import pygame
import random
import time
pygame.init()




black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
yellow=(255,255,0)
WIDTH=480
HEIGHT=600

fps= 60
clock=pygame.time.Clock()
spaceship=pygame.image.load("playerShip3_orange.png")
#background=pygame.image.load("blue.png")
#background_image=background.get_rect()
laser=pygame.image.load("laserGreen10.png")
meteor=pygame.image.load("meteorBrown_big4.png")

surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Template")
pygame.mixer.init()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(spaceship,(50,38))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius=20
        #pygame.draw.circle(self.image,red,self.rect.center,self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0


    def update(self):
        self.speedx=0
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx=-8
        if keys[pygame.K_RIGHT]:
            self.speedx=8
        self.rect.x+=self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bull=bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bull)
        bullets.add(bull)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(meteor,(30,40))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius= int(self.rect.width * .85 / 2)
        #pygame.draw.circle(self.image,red,self.rect.center,self.radius)
        self.rect.x=random.randrange(WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(1,8)
        self.speedx=random.randrange(-3,3)

    def update(self):
            self.rect.y+=self.speedy
            self.rect.x+=self.speedx
            if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
                self.rect.x=random.randrange(WIDTH-self.rect.width)
                self.rect.y=random.randrange(-100,-40)
                self.speedy=random.randrange(1,8)

                
class bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.transform.scale(laser,(10,20))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10



    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
mobs=pygame.sprite.Group()
mob=Mob()
for i in range(8):
    m=Mob()
    all_sprites.add(m)
    mobs.add(m)

bullets=pygame.sprite.Group()   
gameLoop=True



while gameLoop:
    
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameLoop=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    player.shoot()
                elif event.type==pygame.K_UP:
                    pygame.time.delay(3000)
                    

    all_sprites.update()
    surface.fill(black)
    #surface.blit(background,(0,0,WIDTH,HEIGHT))
    
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    all_sprites.draw(surface)
    hits=pygame.sprite.spritecollide(player,mobs,False,pygame.sprite.collide_circle)
    if hits:
        gameLoop=False
    
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
