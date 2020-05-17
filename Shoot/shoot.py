import pygame
import random
pygame.init()




black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
WIDTH=480
HEIGHT=600

fps= 60
clock=pygame.time.Clock()

        
surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Template")
pygame.mixer.init()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(green)
        self.rect = self.image.get_rect()
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

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((30,40))
        self.image.fill(red)
        self.rect=self.image.get_rect()
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

                




all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
mobs=pygame.sprite.Group()
mob=Mob()
for i in range(8):
    m=Mob()
    all_sprites.add(m)
    mobs.add(m)
    
gameLoop=True

while gameLoop:
    
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameLoop=False

    all_sprites.update()
    surface.fill(black)
    all_sprites.draw(surface)
    hits=pygame.sprite.spritecollide(player,mobs,False)
    if hits:
        gameLoop=False
    
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
