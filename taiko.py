#! python3
# pygame_boilerplate.py
# Provides template code on which to build

import pygame, random, time

pygame.init()

# CONSTANTS --------
WIDTH  = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
WINDOW_TITLE = "Taiko!"
BGCOLOUR = (0, 0, 0)
REFRESH_RATE = 60
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (255,0,255)
RED = (255,0,0)
GREEN = (4,214,5)
RED_DRUM_X = [3150, 4464, 4900,7192,7378,7564,7967,8327,9300,9679,11477,12965,13647,15197,17491,18210,19016,19574,22860,23108,24782,25216,25836,27014,27944,28254,28626,28936,28998,29928,30052,30300,30982,31130,32308,33238,33548,33920,34354,34664,35656,35780,36772,37516,38012,38570] 
LEFT_DRUM_X = [3100,4340, 5394,5766,7285,7471,7707,8947,11291,12655,13275,13833,14515,16809,17057,17838,18520,19326,20194,20814,22426,23728,24100,24410,25526,25712,26580,26890,27634,28502,29432,29742,30672,31006,31750,32122,32928,33796,34230,35036,35408,36090,36400,37144,37826,38384]



#classes
#Blue Drums that you much hit with the input keys on the left
class LeftDrum(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        # What the block looks like
        self.image = pygame.Surface([width, height])
        # Mathematical representation of our block
        self.rect = self.image.get_rect() # ->[x,y,width,height]    
        self.image = pygame.transform.scale(
            pygame.image.load("bluedrum.png").convert_alpha(),
            (80, 80)
        )        
        


    def update(self):
        self.rect.x -= 10
        



#Red drums that you must hit with the input keys on the right
class RightDrum(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        # What the block looks like
        self.image = pygame.Surface([width, height])
        # Mathematical representation of our block
        self.rect = self.image.get_rect() # ->[x,y,width,height]    
        self.image = pygame.transform.scale(
            pygame.image.load("reddrum.png").convert_alpha(),
            (80, 80)
        )        

    def update(self):
        self.rect.x -= 10
        

 

# Line that deletes the drum and subtracts points if it collides with one
class EndLine(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25, 200])
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()

class Creeper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale(
            pygame.image.load("awman.jpg"), (75, 150)
        )
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()


# Line that indicates where the drum must be before you tap
class Tapline(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("tapline.png").convert(), 
            (25, 200)
        )
        

        self.rect = self.image.get_rect()

# Object that the drums ride down on
class Runway(pygame.sprite.Sprite):
   def __init__(self):
        super().__init__()
        #what it looks like
        self.image = pygame.Surface([800, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(
            pygame.image.load("runway.jpg").convert_alpha(),
            (800, 100)
        )

class LeftDrummer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25,10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def hit_ldrum(self):
        self.rect.y = 250
    def stop_ldrum(self):
        self.rect.y = 280

class RightDrummer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25,10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def hit_rdrum(self):
        self.rect.y = 250
    def stop_rdrum(self):
        self.rect.y = 280



    

# Functions --------
def main():
    # LOCAL Variables -------
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 25, bold=True)
    num_leftdrum = 46
    num_rightdrum = 46
    bgpicture = pygame.image.load("crowd.jpeg") #.convert(),(800,600)
    losspic = pygame.transform.scale(pygame.image.load("loss.png"), (800, 600))
    done = False # controls our main loop
    failstreak = False
    ldrum_list = pygame.sprite.Group()
    rdrum_list = pygame.sprite.Group()
    tdrum_list = pygame.sprite.Group()
    endline_list = pygame.sprite.Group()
    ldrummer_list = pygame.sprite.Group()
    rdrummer_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    
    score = 0

    #draw left drummer
    ldrummer = LeftDrummer()
    ldrummer.rect.x = 200
    ldrummer.rect.y = 280
    ldrummer_list.add(ldrummer)
    all_sprites_list.add(ldrummer)

    #draw right drummer
    rdrummer = RightDrummer()
    rdrummer.rect.x = 200
    rdrummer.rect.y = 280
    rdrummer_list.add(rdrummer)
    all_sprites_list.add(rdrummer)

    # Draw Endline
    endline = EndLine()
    endline.rect.x = 100
    endline.rect.y = 145
    endline_list.add(endline)


    #Draw runway
    runway = Runway()
    runway.rect.x = 0
    runway.rect.y = 187
    all_sprites_list.add(runway)

    # Draw Tapline
    tapline = Tapline()
    tapline.rect.x = 200
    tapline.rect.y = 145
    all_sprites_list.add(tapline)


    #draw the man himself
    creeper = Creeper()
    creeper.rect.x = 85
    creeper.rect.y = 170
    all_sprites_list.add(creeper)
    


    # Draw all the Right Drums
    for i in range(num_rightdrum):
        rdrum = RightDrum(80, 80)            
        rdrum.rect.x = RED_DRUM_X[i]
        rdrum.rect.y = 200
        rdrum_list.add(rdrum)
        tdrum_list.add(rdrum)
        all_sprites_list.add(rdrum)

    # Draw all the left drums
    for i in range(num_leftdrum):
        ldrum = LeftDrum(80, 80)
        ldrum.rect.x = LEFT_DRUM_X[i]
        ldrum.rect.y = 200
        ldrum_list.add(ldrum)
        tdrum_list.add(ldrum)
        all_sprites_list.add(ldrum)



    endline_list.add(endline)
    pygame.display.set_caption(WINDOW_TITLE)
    
    #music player
    bgmusic = pygame.mixer.Sound("STAL.wav")
    pygame.mixer.Sound.play(bgmusic)

    #mouse visibility
    pygame.mouse.set_visible(True)

    # Main loop
    while not done:
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z or event.key == pygame.K_x:
                    ldrummer.hit_ldrum()

                if event.key == pygame.K_c or event.key == pygame.K_v:
                    rdrummer.hit_rdrum()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z or event.key == pygame.K_x:
                    ldrummer.stop_ldrum()

                if event.key == pygame.K_c or event.key == pygame.K_v:
                    rdrummer.stop_rdrum()

             

        # Game Logic --------
       
        for drum in ldrum_list:
            ldrums_hit = pygame.sprite.spritecollide(
                drum,
                ldrummer_list,
                False
            )

            ldrums_missed = pygame.sprite.spritecollide(
                drum, 
                endline_list, 
                False
            )

            if len(ldrums_hit) > 0:
                drum.kill()
                score += 100
                failstreak = 0

            if len(ldrums_missed) > 0:
                drum.kill()
                score -= 50
                failstreak += 1

        for drum in rdrum_list:
            rdrums_hit = pygame.sprite.spritecollide(
                drum,
                rdrummer_list,
                False
            )

            rdrums_missed = pygame.sprite.spritecollide(
                drum, 
                endline_list, 
                False
            )

            if len(rdrums_hit) > 0:
                drum.kill()
                score += 100
                failstreak = 0


            if len(rdrums_missed) > 0:
                drum.kill()
                score -= 50
                failstreak += 1


        # Drawing --------
        endline_list.draw(screen)
        screen.fill(BGCOLOUR)
        screen.blit
        screen.blit(bgpicture, (0,0))

        all_sprites_list.draw(screen)

        ldrum_list.update()
        rdrum_list.update()

        text = font.render("Score: " + str(score), False, WHITE)
        screen.blit(text, (WIDTH//3, 30))  
        if failstreak >= 3:
            pygame.mixer.music.stop()
            screen.blit(losspic, (0,0))
            all_sprites_list.remove(all_sprites_list)
            
            failure = font.render("You exploded! Dont let the blocks hit the creeper!", False, BGCOLOUR)
            screen.blit(failure,(100,30))
        pygame.display.flip() # update the screen



        # Clock Tick -------
        clock.tick(REFRESH_RATE)

if __name__ == "__main__":
    main()

