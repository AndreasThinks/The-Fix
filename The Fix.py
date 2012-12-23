import pygame, random, math, sys
from pygame.locals import *


#globals
WINWIDTH = 800
WINHEIGHT = 600

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

TEXTCOLOR = BLACK

#my first start, starscreen
#state = "Start"

#start in fight for debug
state = "Title"

gameSurface = pygame.display.set_mode((WINWIDTH, WINHEIGHT), 0, 32)
pygame.display.set_caption("The Fix")
gameSurface.fill(WHITE)

#set game clock
pygame.init()
mainClock = pygame.time.Clock()
FPS = 60

activate = False

#import music files
pygame.mixer.music.load('title.wav')
bananasound = pygame.mixer.Sound('c-banana.wav')
bananasound2 = pygame.mixer.Sound('c-banana2.wav')
bananasound3 = pygame.mixer.Sound('c-banana3.wav')
bottlesound = pygame.mixer.Sound('c-bottle.wav')
bottlesound2 = pygame.mixer.Sound('c-bottle2.wav')
bottlesound3 = pygame.mixer.Sound('c-bottle3.wav')
fightsound = pygame.mixer.Sound('c-fight.wav')
goatsound = pygame.mixer.Sound('c-goat.wav')
goatsound2 = pygame.mixer.Sound('c-goat2.wav')
goatsound3 = pygame.mixer.Sound('c-goat3.wav')
papersound = pygame.mixer.Sound('c-paper.wav')
papersound2 = pygame.mixer.Sound('c-paper2.wav')
winsound = pygame.mixer.Sound('win.wav')
losesound = pygame.mixer.Sound('lose.wav')
hit = pygame.mixer.Sound('smash.wav')
kicks = pygame.mixer.Sound('kick.wav')
elbows = pygame.mixer.Sound('elbows.wav')

#define starting cash value and weapon unlocks
cash = 100
throw = True
weapons = []

papercoords = [860, 300]
throwpaper = False

bananacoords = [860, 520]
throwbanana = False

bottlecoords = [860, 300]
throwbottle = False

goatcoords = [860, 520]
throwgoat = False

#weapon unlock stages
bananalock = True
bottlelock = True
goatlock = True



#define inventory surface
inventory = pygame.Surface ((800,40))
inventory.fill(BLACK)

#define ring surface
ring = pygame.image.load("ring.png")
title = pygame.image.load("title.png")

#define enemy advantage
enemyboost = 10

# define font and draw text function
pygame.font.init()
defaultfont = "arialblack"
font = pygame.font.SysFont(defaultfont, 35)
def drawText(text, font, surface, x, y, colour = TEXTCOLOR):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)




class Fighter(pygame.sprite.Sprite):
    """ a class that defines our boxers and their sprites"""

    def __init__(self, side):
        # initialize the pygame sprite part
        pygame.sprite.Sprite.__init__(self)
        self.side = side
        self.name = "Boxer " + str(side)
        if side == "left":
            self.surface = pygame.image.load("boxer-left-default.png")
        if side == "right":
            self.surface = pygame.image.load("boxer-right-default.png")
        self.morale = random.randint(1, 3)
        self.hp = 80 + random.randint(0, 20)
        if side == "right":
            self.hp = self.hp + enemyboost
        self.strength = random.randint(0, 5)
        self.speed = 7 + random.randint(0, 3)
        self.rect = self.surface.get_rect()
        if side == "left":
            self.hprect = pygame.Rect(20,25,self.hp,15)
        if side == "right":
            self.hprect = pygame.Rect(700,25,self.hp,15)
        if side == "left":
            self.x = 100
            self.y = 210
        if side == "right":
            self.x = 577
            self.y = 210
        if side == "left":
            self.startx = 100
            self.startyy = 210
        if side == "right":
            self.startx = 577
            self.starty = 210

    def onring(self):
        gameSurface.blit(ring, (0, 0))
        gameSurface.blit(self.surface, (self.x, self.y))

    def movein(self):
        if right.x - left.x > 15:
            if self.side == "left" and right.x > 400:
                self.x += self.speed
            elif self.side == "right" and left.x < 400:
                self.x -= self.speed

    def retreat(self):
        print str(self.x - self.startx)
        if self.side == "left":
            if self.x >= self.startx + 11:
                self.x -= self.speed
            if 50 > left.x - right.x > 30:
                if self.side == "left":
                    left.surface = pygame.image.load("boxer-left-default.png")
                if self.side == "right":
                    right.surface = pygame.image.load("boxer-right-default.png")
            if left.x > left.startx + 10 or right.x < right.startx + 10:
                print "back to start"
                turn = "start"
        if self.side == "right":
            if self.x <= self.startx + 11:
                self.x += self.speed
            if 50 > left.rect.right - right.rect.left > 30:
                if self.side == "left":
                    left.surface = pygame.image.load("boxer-left-default.png")
                if self.side == "right":
                    right.surface = pygame.image.load("boxer-right-default.png")
            if left.x > left.startx + 10 or right.x < right.startx + 10:
                print "back to start"
                turn = "start"



left = Fighter("left")
right = Fighter("right")
turn = "start"

#import weapon assets
paper = pygame.image.load("paper.png")
bottle = pygame.image.load("bottle.png")
banana = pygame.image.load("banana.png")
goat = pygame.image.load("goat.png")
firstlines = ["The wife just left with all the money",
"There's nothing left in the safe",
"The scoundrel took your last dime",
"You haven't got a penny to your name",
"He took everything you had"]

secondlines = ["and the mob don't like delays",
"Bad news is you owe the Yakuza",
"Shame Big Vinny wants his money",
"But you need to get out of town"]

line1 = random.randint(1,5)
line2 = random.randint(1,4)

pygame.mixer.music.play(-1, 0.0)

activate = False
state = "Title"
while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == ord('p'):
                    throwpaper = True
                if event.key == ord('a'):
                    throwbanana = True
                if event.key == ord('b'):
                    throwbottle = True
                if event.key == ord('g'):
                    throwgoat = True
                if event.key == K_SPACE:
                    activate = True
                    print "activate"
    gameSurface.fill(WHITE)

    if state == "Title":
        gameSurface.fill(WHITE)
        gameSurface.blit(title, (0, 0))
        drawText(firstlines[line1 - 1] , font, gameSurface, 50 , 350)
        drawText(secondlines[line2 - 1] , font, gameSurface, 75 , 400)
        drawText("Guess you've got a game to fix..." , font, gameSurface, 75 , 500)
        if activate == True:
            state = "Store"
            activate = False
            pygame.mixer.music.load('crowd.wav')
            pygame.mixer.music.play(-1, 0.0)
        pygame.display.update()

    if state == "matchlose":
        gameSurface.fill(WHITE)
        gameSurface.blit(ring, (0, 0))
        gameSurface.blit(inventory, (0, 560))
        drawText("You Lose" , font, gameSurface, 300 , 100)
        if cash >= 0:
            drawText("Hit Space for next match" , font, gameSurface, 200 , 300)
            if activate == True:
                left = Fighter("left")
                right = Fighter("right")
                state = "Store"
                activate = False
                turn = "start"
        if cash < 0:
            drawText("It's all over" , font, gameSurface, 200 , 450)

        #check FPS
        mainClock.tick(FPS)
        pygame.display.update()

    if state == "matchwin":
        gameSurface.fill(WHITE)
        gameSurface.blit(ring, (0, 0))
        gameSurface.blit(inventory, (0, 560))
        drawText("You Win" , font, gameSurface, 300 , 100)
        if cash >= 200:
            drawText("You've got the cash!" , font, gameSurface, 200 , 450)
        if cash < 200:
            drawText("Hit Space for next match" , font, gameSurface, 200 , 300)
            if activate == True:
                state = "Store"
                left = Fighter("left")
                right = Fighter("right")
                activate = False
                turn = "start"

        #check FPS
        mainClock.tick(FPS)
        pygame.display.update()



    if state == "Store":


        gameSurface.fill(WHITE)
        gameSurface.blit(ring, (0, 40))
        drawText("The Store, press Space to start" , font, gameSurface, 100 ,5, BLACK)
        drawText("You've got $" + str(cash) + ", you need $"+  str(200 - cash) + " more", font, gameSurface, 50 ,40, BLACK)
        
        if left.hp <= 85:
            drawText("Your fighter is looking a little weak today", font, gameSurface, 20 ,75, BLACK)
            if left.morale >= 2:
                drawText("but is in good spirits", font, gameSurface, 150 ,120, BLACK)
        elif left.hp <= 94:
            drawText("Your fighter is well prepared for  today", font, gameSurface, 20 ,75, BLACK)
            if left.morale >= 2:
                drawText("and is feeling on top of the world", font, gameSurface, 150 ,120, BLACK)
        elif left.hp >= 95:
            drawText("Your fighter looks in great form today", font, gameSurface, 20 ,75, BLACK)
            if left.morale >= 2:
                drawText("and is feeling on top of the world", font, gameSurface, 150 ,120, BLACK)

        drawText("Newpaper: Interrupts" , font, gameSurface, 5 ,220, BLACK)
        gameSurface.blit(paper, (375 - 150, 280))

        drawText("Bottle: Damages" , font, gameSurface, 5 + 500 ,220, BLACK)
        gameSurface.blit(bottle, (375 - 150 + 400, 280))

        drawText("Banana: Distract" , font, gameSurface, 5 ,220 + 180, BLACK)
        gameSurface.blit(banana, (375 - 150, 280 + 180))

        drawText("The Hell Goat" , font, gameSurface, 5 + 500 ,220 + 180, RED)
        gameSurface.blit(goat, (320 + 400 - 150, 280 + 180))

        #bananalock = True
        if bottlelock == True:
            drawText("$60 - B to Unlock" , font, gameSurface, 5 + 450 , 350, BLACK)
        else:
            drawText("Unlocked" , font, gameSurface, 5 + 450 , 350, BLACK)

        if bananalock == True:
            drawText("$60 - A to Unlock" , font, gameSurface, 5 ,220 + 180 + 130, BLACK)
        else:
            drawText("Unlocked" , font, gameSurface, 5 ,220 + 180 + 130, BLACK)

        if goatlock == True:
            drawText("$120 - G to Unlock" , font, gameSurface, 5 + 450 , 220 + 180 + 130, BLACK)
        else:
            drawText("Unlocked" , font, gameSurface, 5 + 400 , 220 + 180 + 130, BLACK)

        if throwbottle == True and bottlelock == True:
            if cash >= 60:
                cash -= 60
                bottlelock = False
            throwbottle == False

        if throwbanana == True and bananalock == True:
            if cash >= 60:
                cash -= 60
                bananalock = False
            throwbanana == False

        if throwgoat == True and goatlock == True:
            if cash >= 120:
                cash -= 120
                goatlock = False
            throwgoat == False

        if activate == True:
            throwgoat = False
            throwbanana = False
            throwbottle = False
            state = "Fight"
            attacks = 3


        #check FPS
        mainClock.tick(FPS)
        pygame.display.update()


    if state == "Fight":

        gameSurface.fill(WHITE)
        gameSurface.blit(ring, (0, 0))
        gameSurface.blit(inventory, (0, 560))

        #blit weapons
        drawText("P" , font, gameSurface, 60 ,555, WHITE)
        gameSurface.blit(paper, (140, 565))

        if bottlelock == False:
            drawText("B" , font, gameSurface, 60 + 200 ,555, WHITE)
            gameSurface.blit(bottle, (140 + 200, 565))

        if bananalock == False:
            drawText("A" , font, gameSurface, 60 + 200*2 ,555, WHITE)
            gameSurface.blit(banana, (140 + 200*2, 565))

        if goatlock == False:
            drawText("G" , font, gameSurface, 60 + 200*3 ,555, WHITE)
            gameSurface.blit(goat, (140 + 200*3, 565))

        #blit weapons to right of screen
        papers = pygame.image.load("w-paper.png")
        paperrect = papers.get_rect()
        gameSurface.blit(papers, papercoords)

        bananas = pygame.image.load("w-banana.png")
        bananarect = banana.get_rect()
        gameSurface.blit(bananas, bananacoords)

        bottles = pygame.image.load("w-bottle.png")
        bottlerect = bottles.get_rect()
        gameSurface.blit(bottles, bottlecoords)

        goats = pygame.image.load("w-goat.png")
        goatrect = goats.get_rect()
        gameSurface.blit(goats, goatcoords)

        pygame.draw.rect(gameSurface, RED, left.hprect)
        pygame.draw.rect(gameSurface, GREEN, right.hprect)
        drawText(str(left.hp) , font, gameSurface, 20 ,35)
        drawText(str(right.hp) , font, gameSurface, 700 ,35)

        drawText("Attacks: " + str(attacks) , font, gameSurface, 300 , 100)

        left.onring()
        right.onring()
        if turn == "start":
            turnno = random.randint(1, 10)
            if turnno <= 5:
                turn = "left"
            if turnno > 5:
                turn = "right"
        elif turn == "left":
            leftroll = random.randint(1,6) + left.morale
            if leftroll >= 6:
                turn = "left-elbow"
                attacked = False
            elif left.morale >= 5:
                turn = "left-kick"
                attacked = False
            else:
                turn = "left-punch"
                attacked = False

        elif turn == "left-punch":
            if attacked == False:
                left.movein()
                if right.x - left.x <= 15:
                    hit.play()
                    left.surface = pygame.image.load("boxer-left-punch.png")
                    right.hp -= 8
                    turn = "left-retreat"

        elif turn == "left-kick":
            if attacked == False:
                left.movein()
                if right.x - left.x <= 15:
                    kicks.play()
                    left.surface = pygame.image.load("boxer-left-kick.png")
                    right.hp -= 10
                    attacked = True
                    turn = "left-retreat"

        elif turn == "left-elbow":
            if attacked == False:
                left.movein()
                if right.x - left.x <= 15:
                    elbows.play()
                    left.surface = pygame.image.load("boxer-left-elbow.png")
                    right.hp -= 13
                    attacked = True
                    turn = "left-retreat"

        elif turn == "left-retreat":
            left.x = left.x - left.speed
            if right.x - left.x > 120:
                left.surface = pygame.image.load("boxer-left-default.png")
            if left.x <= left.startx + 10:
                turn = "start"

        elif turn == "right":
            rightroll = random.randint(1,6) + right.morale
            if rightroll >= 6:
                turn = "right-elbow"
                attacked = False
            elif rightroll >= 5:
                turn = "right-kick"
                attacked = False
            else:
                turn = "right-punch"
                attacked = False

        elif turn == "right-punch":
            drawText("Incoming Punch!" , font, gameSurface, 220 , 50)
            if attacked == False:
                right.movein()
                if right.x - left.x <= 15:
                    hit.play()
                    right.surface = pygame.image.load("boxer-right-punch.png")
                    left.hp -= 8
                    turn = "right-retreat"

        elif turn == "right-kick":
            drawText("Incoming Kick!" , font, gameSurface, 220 , 50)
            if attacked == False:
                right.movein()
                if right.x - left.x <= 15:
                    kicks.play()
                    right.surface = pygame.image.load("boxer-right-kick.png")
                    left.hp -= 10
                    turn = "right-retreat"

        elif turn == "right-elbow":
            drawText("Incoming Jump Kick!" , font, gameSurface, 220 , 50)
            if attacked == False:
                right.movein()
                if right.x - left.x <= 15:
                    elbows.play()
                    right.surface = pygame.image.load("boxer-right-elbow.png")
                    left.hp -= 13
                    turn = "right-retreat"

        elif turn == "right-retreat":
            right.x = right.x + right.speed
            if right.x - left.x > 120:
                right.surface = pygame.image.load("boxer-right-default.png")
            if right.x >= right.startx - 10:
                turn = "start"

        if throwpaper == True and attacks > 0:
            papercoords = papercoords
            if papercoords[0] >= right.x and throwpaper == True:
                papers = pygame.transform.rotate(papers, -10)
                papercoords[0] -= 35
            if papercoords[0] - right.x <= 5:
                soundno = random.randint(1, 2)
                if soundno == 1:
                    papersound.play()
                else:
                    papersound2.play()
                turn = "right-retreat"
                throwpaper = False
                attacks -= 1
                papercoords = [860, 300]

        if throwbottle == True and bottlelock == False and attacks > 0:
            bottlecoords = bottlecoords
            if bottlecoords[0] >= right.x and throwbottle == True:
                bottles = pygame.transform.rotate(bottles, -10)
                bottlecoords[0] -= 35
            if bottlecoords[0] - right.x <= 5:
                soundno = random.randint(1, 3)
                if soundno == 1:
                    bottlesound.play()
                elif soundno == 2:
                    bottlesound2.play()
                else:
                    bottlesound3.play()
                right.hp -= 10
                throwbottle = False
                attacks -= 1
                bottlecoords = [860, 300]

        if throwbanana == True and bananalock == False and attacks > 0:
            bananacoords = bananacoords
            if bananacoords[0] >= right.x and throwbanana == True:
                bananas = pygame.transform.rotate(bananas, -10)
                bananacoords[0] -= 35
            if bananacoords[0] - right.x <= 5:
                soundno = random.randint(1, 3)
                if soundno == 1:
                    bananasound.play()
                elif soundno == 2:
                    bananasound2.play()
                else:
                    bananasound3.play()
                right.morale -= 1
                throwbanana = False
                attacks -=1
                bananacoords = [860, 530]

        if throwgoat == True and goatlock == False and attacks > 0:
            goatcoords = goatcoords
            if goatcoords[0] >= right.x and throwgoat == True:
                goats = pygame.transform.rotate(goats, -10)
                goatcoords[0] -= 35
            if goatcoords[0] - right.x <= 5:
                soundno = random.randint(1, 3)
                if soundno == 1:
                    goatsound.play()
                elif soundno == 2:
                    goatsound2.play()
                else:
                    goatsound3.play()
                right.hp -= 20
                throwgoat = False
                attacks -=1
                goatcoords = [860, 530]






        #check FPS
        mainClock.tick(FPS)
        pygame.display.update()

        if left.hp <= 0:
            activate = False
            cash -= 40
            enemyboost -= 5
            losesound.play()
            state = "matchlose"

        if right.hp <= 0:
            activate = False
            cash += 60
            enemyboost += 5
            winsound.play()
            state = "matchwin"
