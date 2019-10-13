import pygame
import time
import random

pygame.init()
pygame.font.init()

display_width = 900
display_height = 650

black = (0,0,0)
gray1 = (15,15,15)
gray2 = (30,30,30)
gray3 = (45,45,45)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Lost Savance')
icon = pygame.image.load('Assets/Art/icon.png')
pygame.display.set_icon(icon)

Night = pygame.image.load("Assets/Art/Menu/NightSky.png")
Landscape = pygame.image.load("Assets/Art/Menu/Landscape.png")
option1 = pygame.image.load("Assets/Art/Menu/SelectionStart.png")
option2 = pygame.image.load("Assets/Art/Menu/SelectionOptions.png")
option3 = pygame.image.load("Assets/Art/Menu/SelectionExit.png")
logo = pygame.image.load("Assets/Art/logo.png")

gameDisplay.blit(logo, (0, 0))
pygame.display.update()
time.sleep(2)






#=================================VAR================================#

chunk = 25

#People#

heroX = 0
heroY = 0
heroHP = 8
balance = 10
potions = 3
view = 2
frame = 0
Herobusy = False
heroHit = False

shopX = (chunk*29)
shopY = (chunk*2)

#Mobs#

mob1X = (chunk*12)
mob1Y = (chunk*12)
mob1HP = 5
mob1 = True
MobAttack1 = False

mob2X = (chunk*12)
mob2Y = (chunk*2)
mob2HP = 3
mob2 = True
MobAttack2 = False

mob3X = (chunk*0)
mob3Y = (chunk*0)
mob3HP = 0
mob3 = False
MobAttack3 = False

mob4X = (chunk*0)
mob4Y = (chunk*0)
mob4HP = 0
mob4 = False
MobAttack4 = False

mob5X = (chunk*0)
mob5Y = (chunk*0)
mob5HP = 0
mob5 = False
MobAttack5 = False

def loop():
    pass
    
mob6X = (chunk*0)
mob6Y = (chunk*0)
mob6HP = 0
mob6 = False
MobAttack6 = False

mob7X = (chunk*0)
mob7Y = (chunk*0)
mob7HP = 0
mob7 = False
MobAttack7 = False

mob8X = (chunk*0)
mob8Y = (chunk*0)
mob8HP = 0
mob8 = False
MobAttack8 = False

mob9X = (chunk*0)
mob9Y = (chunk*0)
mob9HP = 0
mob9 = False
MobAttack9 = False

mob10X = (chunk*0)
mob10Y = (chunk*0)
mob10HP = 0
mob10 = False
MobAttack2 = False

blocked = False
blocked2 = False
#Merchandise#

sale1 = "potion"
unique1 = False
sold1 = False

sale2 = ""
unique2 = False
sold2 = False

sale3 = ""
unique3 = False
sold3 = False

sale4 = ""
unique4 = False
sold4 = False

sale5 = ""
unique5 = False
sold5 = False

sale6 = ""
unique6 = False
sold6 = False

#Objects#

coin1 = True
coin1X = (chunk*8)
coin1Y = (chunk*3)

coin2 = True
coin2X = (chunk*11)
coin2Y = (chunk*3)

coin3 = True
coin3X = (chunk*14)
coin3Y = (chunk*3)

coin4 = True
coin4X = (chunk*17)
coin4Y = (chunk*3)

coin5 = True
coin5X = (chunk*20)
coin5Y = (chunk*3)

coin6 = True
coin6X = (chunk*23)
coin6Y = (chunk*3)

coin7 = True
coin7X = (chunk*26)
coin7Y = (chunk*3)

coin8 = True
coin8X = (chunk*6)
coin8Y = (chunk*5)

coin9 = True
coin9X = (chunk*5)
coin9Y = (chunk*8)

coin10 = True
coin10X = (chunk*2)
coin10Y = (chunk*9)

#Potions
potion1 = True
potion1X = (chunk*12)
potion1Y = (chunk*1)

potion2 = False
potion2X = (chunk*0)
potion2Y = (chunk*0)

potion3 = False
potion3X = (chunk*0)
potion3Y = (chunk*0)

potion4 = False
potion4X = (chunk*0)
potion4Y = (chunk*0)

potion5 = False
potion5X = (chunk*0)
potion5Y = (chunk*0)


#rocks
rock1 = True
rock1X = (chunk*34)
rock1Y = (chunk*12)

rock2 = True
rock2X = (chunk*34)
rock2Y = (chunk*13)

rock3 = False
rock3X = (chunk*12)
rock3Y = (chunk*6)

rock4 = False
rock4X = (chunk*12)
rock4Y = (chunk*6)

rock5 = False
rock5X = (chunk*12)
rock5Y = (chunk*6)

rock6 = False
rock6X = (chunk*12)
rock6Y = (chunk*6)

rock7 = False
rock7X = (chunk*12)
rock7Y = (chunk*6)

rock8 = False
rock8X = (chunk*12)
rock8Y = (chunk*6)

rock9 = False
rock9X = (chunk*12)
rock9Y = (chunk*6)

#============OTHER============#

line1 = ""
line1X = 430
line2 = ""
line2X = 430
line3 = ""
line3X = 430
line4 = ""
line4X = 430
line5 = ""
line5X = 430
line6 = ""
line6X = 430
line7 = ""
line7X = 430

random10 = [1,2,3,4,5,6,7,8,9,10]
random8 = [1,2,3,4,5,6,7,8]
randomChoice = 0

select = 1
selectEsc = 1
selectShop = 1

counter = 0
counter2 = 0

clock = 0
aniclock = 0
movclock = 0
chatclock = 0
hitclock = 0
atkClockM1 = 0
atkClockM2 = 0
    
reset = True
Time = (clock/350)

#sprites

L0S1 = pygame.image.load("Assets/Level/L0S1.png")
L0S2 = pygame.image.load("Assets/Level/L0S2.png")
#L0S3 = pygame.image.load("Assets/Level/L0S3.png")

level = "menu"


heroIMG = pygame.image.load("Assets/Entities/Hero/heroFH.png")

#PROFILES
talk = pygame.image.load("Assets/Art/Speech/SpeechBubbleThink.png")

merchantProfile = pygame.image.load("Assets/Profiles/test.png")

profile = ""


merchant = pygame.image.load("Assets/Entities/Merchant/MerchantF.png")

store = pygame.image.load("Assets/Art/Shop/shop.png")
shopSelection = pygame.image.load("Assets/Art/Shop/shopSelect.png")

bush = pygame.image.load("Assets/Tiles/Terrain/bush.png")
rock = pygame.image.load("Assets/Tiles/Terrain/rock.png")
house1 = pygame.image.load("Assets/Tiles/Buildings/house.png")
fence = pygame.image.load("Assets/Tiles/Buildings/fence.png")

coin = pygame.image.load("Assets/Tiles/Items/coin.png")
potion = pygame.image.load("Assets/Tiles/Items/potion.png")


escScreen = pygame.image.load("Assets/Art/EscapeMenu.png")
escSelect1 = pygame.image.load("Assets/Art/EscapeResume.png")
escSelect2 = pygame.image.load("Assets/Art/EscapeOptions.png")
escSelect3 = pygame.image.load("Assets/Art/EscapeExit.png")
selection = pygame.image.load("Assets/Toolbar/selection.png")
heart = pygame.image.load("Assets/Toolbar/heart.png")

slime = pygame.image.load("Assets/Entities/Mob/slime.png")
slimeHurt = pygame.image.load("Assets/Entities/Mob/slimeHurt.png")

skeleton = pygame.image.load("Assets/Entities/Mob/skeleton.png")
skeletonHurt = pygame.image.load("Assets/Entities/Mob/skeletonHurt.png")


#
#============================= Main Game Loop =============================#
#
def transition():
    global heroMotion
    global movclock
    heroMotion = False
    movclock = 0
    Tran = True
    counterT = 0
    while Tran:
        counterT += 1
        if counterT >= 1 and counterT <= 5:
            gameDisplay.fill(gray3)
            
        if counterT >= 6 and counterT <= 10:
            gameDisplay.fill(gray2)
            
        if counterT >= 11 and counterT <= 15:
            gameDisplay.fill(gray1)
            
        if counterT >= 16 and counterT <= 130:
            gameDisplay.fill(black)
            
        if counterT >= 131 and counterT <= 145:
            gameDisplay.fill(gray1)
            
        if counterT >= 146 and counterT <= 150:
            gameDisplay.fill(gray2)
            
        if counterT >= 151 and counterT <= 165:
            gameDisplay.fill(gray3)
            Tran = False
            
        pygame.display.update()

def Menu():
    global level
    global heroX
    global heroY
    global heroHP
    global balance
    global potions
    global view
    slide = 0
    MenuSelect = 1

    while level == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if MenuSelect == 1:
                        heroX = (chunk*0)
                        heroY = (chunk*9)
                        heroHP = 8
                        balance = 10
                        potions = 3
                        view = 3
                        level = L0S1
                    if MenuSelect == 2:
                        pass
                    if MenuSelect == 3:
                        quit()
                        
                if event.key == pygame.K_UP and MenuSelect != 1:
                    MenuSelect -= 1
                if event.key == pygame.K_DOWN and MenuSelect != 3:
                    MenuSelect += 1
        
        gameDisplay.blit(Night, (slide, 0))
        gameDisplay.blit(Landscape, (0, 0))
        if MenuSelect == 1:
            gameDisplay.blit(option1, (0, 0))
        if MenuSelect == 2:
            gameDisplay.blit(option2, (0, 0))
        if MenuSelect == 3:
            gameDisplay.blit(option3, (0, 0))
            
        pygame.display.update()

        slide -= 1
        if slide == -1800:
            slide = 0


def heal():
    global potions
    global heroHP
    if potions > 0 and heroHP != 8:
        potions -= 1
        heroHP += 2
        if heroHP > 8:
            heroHP = 8

def heroHurt():
    global heroHit
    heroHit = True
    

def mob1hurt():
    gameDisplay.blit(slimeHurt, (mob1X, (mob1Y - 7)))
    randomChoice = (random.choice(random10))
    pygame.display.update()
    time.sleep(0.3)

def mob2hurt():
    gameDisplay.blit(skeletonHurt, (mob2X, (mob2Y - 9)))
    randomChoice = (random.choice(random10))
    pygame.display.update()
    time.sleep(0.3)


def text_objects(text,font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

def balance_display(text):
    largeText = pygame.font.SysFont('Arial.ttf',22)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (93,620)
    gameDisplay.blit(TextSurf, TextRect)

def balance_dis():
    balance_display(str(balance))

def potionCount_display(text):
    largeText = pygame.font.SysFont('Arial.ttf',18)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (218,583)
    gameDisplay.blit(TextSurf, TextRect)

def potionCount_dis():
    potionCount_display(str(potions))

#============chat============#

def chat1_display(text):
    largeText = pygame.font.SysFont('Arial.ttf',19)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (line1X,530)
    gameDisplay.blit(TextSurf, TextRect)

def chat1_dis():
    chat1_display(str(line1))

def chat2_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (line2X,550)
    gameDisplay.blit(TextSurf, TextRect)

def chat2_dis():
    chat2_display(str(line2))

def chat3_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (line3X,565)
    gameDisplay.blit(TextSurf, TextRect)

def chat3_dis():
    chat3_display(str(line3))

def chat4_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (line4X,580)
    gameDisplay.blit(TextSurf, TextRect)

def chat4_dis():
    chat4_display(str(line4))

def chat5_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (line5X,595)
    gameDisplay.blit(TextSurf, TextRect)

def chat5_dis():
    chat5_display(str(line5))

def chat6_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (line6X,610)
    gameDisplay.blit(TextSurf, TextRect)

def chat6_dis():
    chat6_display(str(line6))
    
def chat7_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (line7X,625)
    gameDisplay.blit(TextSurf, TextRect)

def chat7_dis():
    chat7_display(str(line7))

def chat():
    chat1_dis()
    chat2_dis()
    chat3_dis()
    chat4_dis()
    chat5_dis()
    chat6_dis()
    chat7_dis()
#=================================#

    
    
def lives():
    if heroHP >= 1:
        gameDisplay.blit(heart, (20, 577))
    if heroHP >= 2:
        gameDisplay.blit(heart, (38, 577))
    if heroHP >= 3:
        gameDisplay.blit(heart, (56, 577))
    if heroHP >= 4:
        gameDisplay.blit(heart, (74, 577))
    if heroHP >= 5:
        gameDisplay.blit(heart, (92, 577))
    if heroHP >= 6:
        gameDisplay.blit(heart, (110, 577))
    if heroHP >= 7:
        gameDisplay.blit(heart, (128, 577))
    if heroHP >= 8:
        gameDisplay.blit(heart, (146, 577))

def resetEntities():
    global coin1
    global coin2
    global coin3
    global coin4
    global coin5
    global coin6
    global coin7
    global coin8
    global coin9
    global coin10
    
    global rock1
    global rock2
    global rock3
    global rock4
    global rock5
    global rock6
    global rock7
    global rock8
    global rock9
    global rock10
    
    global mob1
    global mob2
    global mob3
    global mob4
    global mob5
    global mob6
    global mob7
    global mob8
    global mob9
    global mob10

    global potion1
    global potion2
    global potion3
    global potion4
    global potion5

    global mob1X
    global mob1Y
    global mob1HP
    global mob1
    global MobAttack1
    
    global mob2X
    global mob2Y
    global mob2HP
    global mob2
    global MobAttack2

    global mob3X
    global mob3Y
    global mob3HP
    global mob3
    global MobAttack3

    global mob4X
    global mob4Y
    global mob4HP
    global mob4
    global MobAttack4

    global mob5X
    global mob5Y
    global mob5HP
    global mob5
    global MobAttack5

    global mob6X
    global mob6Y
    global mob6HP
    global mob6
    global MobAttack6

    global mob7X
    global mob7Y
    global mob7HP
    global mob7
    global MobAttack7

    global mob8X
    global mob8Y
    global mob8HP
    global mob8
    global MobAttack8

    global mob9X
    global mob9Y
    global mob9HP
    global mob9
    global MobAttack9

    global mob10X
    global mob10Y
    global mob10HP
    global mob10
    global MobAttack10
    
    coin1 = False
    coin2 = False
    coin3 = False
    coin4 = False
    coin5 = False
    coin6 = False
    coin7 = False
    coin8 = False
    coin9 = False
    coin10 = False
    
    rock1 = False
    rock2 = False
    rock3 = False
    rock4 = False
    rock5 = False
    rock6 = False
    rock7 = False
    rock8 = False
    rock9 = False
    rock10 = False

    potion1 = False
    potion2 = False
    potion3 = False
    potion4 = False
    potion5 = False

    mob1X = 0
    mob1Y = 0
    mob1HP = 0
    mob1 = False
    MobAttack1 = 0
    
    mob2X = 0
    mob2Y = 0
    mob2HP = 0
    mob2 = False
    MobAttack2 = 0

    mob3X = 0
    mob3Y = 0
    mob3HP = 0
    mob3 = False
    MobAttack3 = 0

    mob4X = 0
    mob4Y = 0
    mob4HP = 0
    mob4 = False
    MobAttack4 = 0

    mob5X = 0
    mob5Y = 0
    mob5HP = 0
    mob5 = False
    MobAttack5 = 0

    mob6X = 0
    mob6Y = 0
    mob6HP = 0
    mob6 = False
    MobAttack6 = 0

    mob7X = 0
    mob7Y = 0
    mob7HP = 0
    mob7 = False
    MobAttack7 = 0

    mob8X = 0
    mob8Y = 0
    mob8HP = 0
    mob8 = False
    MobAttack8 = 0

    mob9X = 0
    mob9Y = 0
    mob9HP = 0
    mob9 = False
    MobAttack9 = 0

    mob10X = 0
    mob10Y = 0
    mob10HP = 0
    mob10 = False
    MobAttack10 = 0
    
    shopX = 0
    shopY = 0
    
def displayL0S1():
    #bushs
    gameDisplay.blit(bush, ((chunk*6), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*7), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*9), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*10), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*12), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*13), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*15), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*16), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*18), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*19), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*21), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*22), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*24), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*25), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*27), (chunk*1 - 8)))
    gameDisplay.blit(bush, ((chunk*28), (chunk*1 - 8)))
    
    gameDisplay.blit(bush, ((chunk*3), (chunk*2 - 8)))
    gameDisplay.blit(bush, ((chunk*4), (chunk*2 - 8)))

    gameDisplay.blit(bush, ((chunk*29), (chunk*3 - 8)))
    gameDisplay.blit(bush, ((chunk*31), (chunk*3 - 8)))
    
    gameDisplay.blit(bush, ((chunk*3), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*4), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*7), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*9), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*11), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*17), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*18), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*24), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*26), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*29), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*31), (chunk*4 - 8)))
    gameDisplay.blit(bush, ((chunk*33), (chunk*4 - 8)))


    gameDisplay.blit(bush, ((chunk*8), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*10), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*12), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*15), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*16), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*19), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*20), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*23), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*25), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*29), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*31), (chunk*5 - 8)))
    gameDisplay.blit(bush, ((chunk*33), (chunk*5 - 8)))
    
    gameDisplay.blit(bush, ((chunk*3), (chunk*6 - 8)))
    gameDisplay.blit(bush, ((chunk*4), (chunk*6 - 8)))
    gameDisplay.blit(bush, ((chunk*7), (chunk*6 - 8)))
    gameDisplay.blit(bush, ((chunk*9), (chunk*6 - 8)))
    gameDisplay.blit(bush, ((chunk*11), (chunk*6 - 8)))
    gameDisplay.blit(bush, ((chunk*24), (chunk*6 - 8)))
    gameDisplay.blit(bush, ((chunk*26), (chunk*6 - 8)))
    gameDisplay.blit(bush, ((chunk*29), (chunk*6 - 8)))
    gameDisplay.blit(bush, ((chunk*31), (chunk*6 - 8)))
    gameDisplay.blit(bush, ((chunk*33), (chunk*6 - 8)))

    gameDisplay.blit(bush, ((chunk*8), (chunk*7 - 8)))
    gameDisplay.blit(bush, ((chunk*25), (chunk*7 - 8)))
    
    gameDisplay.blit(bush, ((chunk*7), (chunk*8 - 8)))
    gameDisplay.blit(bush, ((chunk*26), (chunk*8 - 8)))
    
    gameDisplay.blit(bush, ((chunk*8), (chunk*9 - 8)))
    gameDisplay.blit(bush, ((chunk*29), (chunk*9 - 8)))

    gameDisplay.blit(bush, ((chunk*28), (chunk*10 - 8)))

    gameDisplay.blit(bush, ((chunk*29), (chunk*11 - 8)))
    
    gameDisplay.blit(merchant, (shopX, (shopY - 9)))

    gameDisplay.blit(house1, ((chunk*14), (chunk*9)))
    gameDisplay.blit(fence, ((chunk*13), (chunk*11)))
    gameDisplay.blit(fence, ((chunk*12), (chunk*11)))
    gameDisplay.blit(fence, ((chunk*11), (chunk*11)))
    gameDisplay.blit(fence, ((chunk*10), (chunk*11)))
    gameDisplay.blit(fence, ((chunk*9), (chunk*12)))
    gameDisplay.blit(fence, ((chunk*14), (chunk*16)))
    gameDisplay.blit(fence, ((chunk*13), (chunk*16)))
    gameDisplay.blit(fence, ((chunk*12), (chunk*16)))
    gameDisplay.blit(fence, ((chunk*11), (chunk*16)))
    gameDisplay.blit(fence, ((chunk*10), (chunk*16)))
    gameDisplay.blit(fence, ((chunk*9), (chunk*16)))

def display():
    global level
    global heroX
    global heroY
    global frame
    #Background]
    if level != "menu":
        gameDisplay.blit(level, (0, 0))
    
	#items
    if coin1 == True:
        gameDisplay.blit(coin, ((coin1X), (coin1Y  - 8)))
	
    if coin2 == True:
        gameDisplay.blit(coin, ((coin2X), (coin2Y - 8)))
	
    if coin3 == True:
        gameDisplay.blit(coin, ((coin3X), (coin3Y - 8)))
	
    if coin4 == True:
        gameDisplay.blit(coin, ((coin4X), (coin4Y - 8)))
	
    if coin5 == True:
        gameDisplay.blit(coin, ((coin5X), (coin5Y - 8)))
	
    if coin6 == True:
        gameDisplay.blit(coin, ((coin6X), (coin6Y - 8)))
	
    if coin7 == True:
        gameDisplay.blit(coin, ((coin7X), (coin7Y - 8)))
	
    if coin8 == True:
        gameDisplay.blit(coin, ((coin8X), (coin8Y - 8)))
	
    if coin9 == True:
        gameDisplay.blit(coin, ((coin9X), (coin9Y - 8)))
	
    if coin10 == True:
        gameDisplay.blit(coin, ((coin10X), (coin10Y - 8)))

    if potion1 == True:
        gameDisplay.blit(potion, ((potion1X), (potion1Y)))

    if potion2 == True:
        gameDisplay.blit(potion, ((potion2X), (potion2Y)))
        
    if potion3 == True:
        gameDisplay.blit(potion, ((potion3X), (potion3Y)))
        
    if potion4 == True:
        gameDisplay.blit(potion, ((potion4X), (potion4Y)))
        
    if potion5 == True:
        gameDisplay.blit(potion, ((potion5X), (potion5Y)))
    
    #rock
    if rock1 == True:
        gameDisplay.blit(rock, ((rock1X), (rock1Y)))
    if rock2 == True:
        gameDisplay.blit(rock, ((rock2X), (rock2Y)))
    if rock3 == True:
        gameDisplay.blit(rock, ((rock3X), (rock3Y)))
    if rock4 == True:
        gameDisplay.blit(rock, ((rock4X), (rock4Y)))
    if rock5 == True:
        gameDisplay.blit(rock, ((rock5X), (rock5Y)))
    if rock6 == True:
        gameDisplay.blit(rock, ((rock6X), (rock6Y)))
    if rock7 == True:
        gameDisplay.blit(rock, ((rock7X), (rock7Y)))
    if rock8 == True:
        gameDisplay.blit(rock, ((rock8X), (rock8Y)))

    #Profile

    if profile == "merchantProfile":
        gameDisplay.blit(merchantProfile, (764, 529))
    
    #Hero

    if view == 1:
        if select == 1:
            gameDisplay.blit(selection, (20, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroLHHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroLH.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroLH1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroLH2.png")
        if select == 2:
            gameDisplay.blit(selection, (73, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroLSHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroLS.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroLS1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroLS2.png")
        if select == 3:
            gameDisplay.blit(selection, (126, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroLPHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroLP.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroLP1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroLP2.png")
                
    if view == 2:
        if select == 1:
            gameDisplay.blit(selection, (20, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroFHHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroFH.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroFH1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroFH2.png")
        if select == 2:
            gameDisplay.blit(selection, (73, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroFSHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroFS.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroFS1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroFS2.png")
        if select == 3:
            gameDisplay.blit(selection, (126, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroFPHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroFP.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroFP1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroFP2.png")
                
    if view == 3:
        if select == 1:
            gameDisplay.blit(selection, (20, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroRHHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroRH.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroRH1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroRH2.png")
        if select == 2:
            gameDisplay.blit(selection, (73, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroRSHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroRS.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroRS1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroRS2.png")
        if select == 3:
            gameDisplay.blit(selection, (126, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroRPHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroRP.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroRP1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroRP2.png")
                
    if view == 4:
        if select == 1:
            gameDisplay.blit(selection, (20, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroBHHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroBH.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroBH1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroBH2.png")
        if select == 2:
            gameDisplay.blit(selection, (73, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroBSHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroBS.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroBS1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroBS2.png")
        if select == 3:
            gameDisplay.blit(selection, (126, 528))
            if heroHit:
                heroIMG = pygame.image.load("Assets/Entities/Hero/heroBPHurt.png")
            else:
                if frame == 0:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/heroBP.png")
                if frame == 1:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroBP1.png")
                if frame == 2:
                    heroIMG = pygame.image.load("Assets/Entities/Hero/Animations/heroBP2.png")
        
    gameDisplay.blit(heroIMG, (heroX, (heroY - 9)))    
    
    #mob1 1
    if mob1HP > 0 and mob1 == True:
        gameDisplay.blit(slime, (mob1X, (mob1Y - 8)))
    
    if mob2HP > 0 and mob2 == True:
        gameDisplay.blit(skeleton, (mob2X, (mob2Y - 8)))

    if mob3HP > 0 and mob3 == True:
        gameDisplay.blit(skeleton, (mob3X, (mob3Y - 8)))

    if mob4HP > 0 and mob4 == True:
        gameDisplay.blit(skeleton, (mob4X, (mob4Y - 8)))

    if mob5HP > 0 and mob5 == True:
        gameDisplay.blit(skeleton, (mob5X, (mob5Y - 8)))

    if mob6HP > 0 and mob6 == True:
        gameDisplay.blit(skeleton, (mob6X, (mob6Y - 8)))

    if mob7HP > 0 and mob7 == True:
        gameDisplay.blit(skeleton, (mob7X, (mob7Y - 8)))

    if mob8HP > 0 and mob8 == True:
        gameDisplay.blit(skeleton, (mob8X, (mob8Y - 8)))

    if mob9HP > 0 and mob9 == True:
        gameDisplay.blit(skeleton, (mob9X, (mob9Y - 8)))

    if mob10HP > 0 and mob10 == True:
        gameDisplay.blit(skeleton, (mob10X, (mob10Y - 8)))

    
    balance_dis()
    potionCount_dis()
    chat()




#===============================IN GAME MENUS==============================#


def shopOpen():
    global shop
    global selectShop
    global balance
    global potions
    global heroX
    global heroY
    
    global sale1
    global unique1
    global sold1
    
    global sale2
    global unique2
    global sold2
    
    global sale3
    global unique3
    global sold3
    
    global sale4
    global unique4
    global sold4
    
    global sale5
    global unique5
    global sold5

    global sale6
    global unique6
    global sold6
    
    shop = True
    selectShop = 1

    potionM = pygame.image.load("Assets/Art/Shop/shopItemPotion.png")
    
    while shop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shop = False
                if event.key == pygame.K_UP:
                    if selectShop == 3:
                        selectShop = 1
                    if selectShop == 4:
                        selectShop = 2
                    if selectShop == 5:
                        selectShop = 3
                    if selectShop == 6:
                        selectShop = 4
                if event.key == pygame.K_DOWN:
                    if selectShop == 3:
                        selectShop = 5
                    if selectShop == 1:
                        selectShop = 3
                    if selectShop == 4:
                        selectShop = 6
                    if selectShop == 2:
                        selectShop = 4
                if event.key == pygame.K_LEFT:
                    if selectShop == 2:
                        selectShop = 1
                    if selectShop == 4:
                        selectShop = 3
                    if selectShop == 6:
                        selectShop = 5
                if event.key == pygame.K_RIGHT:
                    if selectShop == 1:
                        selectShop = 2
                    if selectShop == 3:
                        selectShop = 4
                    if selectShop == 5:
                        selectShop = 6

                if event.key == pygame.K_RETURN and sold1 == False and selectShop == 1 and sale1 == "potion" and balance > 4:
                    potions += 1
                    balance -= 5

                if event.key == pygame.K_RETURN and sold2 == False and selectShop == 2 and sale2 == "potion" and balance > 4:
                    potions += 1
                    balance -= 5

                if event.key == pygame.K_RETURN and sold3 == False and selectShop == 3 and sale3 == "potion" and balance > 4:
                    potions += 1
                    balance -= 5

                if event.key == pygame.K_RETURN and sold4 == False and selectShop == 4 and sale4 == "potion" and balance > 4:
                    potions += 1
                    balance -= 5

                if event.key == pygame.K_RETURN and sold5 == False and selectShop == 5 and sale5 == "potion" and balance > 4:
                    potions += 1
                    balance -= 5

                if event.key == pygame.K_RETURN and sold6 == False and selectShop == 6 and sale6 == "potion" and balance > 4:
                    potions += 1
                    balance -= 5

                

        
        
        display()
        if level == L0S1:
            displayL0S1()
        lives()
        chat()
        
        gameDisplay.blit(talk, ((heroX), (heroY - 30)))
        gameDisplay.blit(talk, (shopX, (shopY - 30)))
        
        gameDisplay.blit(store, (0, 0))

        if sale1 == "potion":
            gameDisplay.blit(potionM, (318, 208))

        if sale2 == "potion":
            gameDisplay.blit(potionM, (456, 208))

        if sale3 == "potion":
            gameDisplay.blit(potionM, (318, 254))

        if sale4 == "potion":
            gameDisplay.blit(potionM, (456, 254))

        if sale5 == "potion":
            gameDisplay.blit(potionM, (318, 300))

        if sale6 == "potion":
            gameDisplay.blit(potionM, (456, 300))
        
        if selectShop == 1:            
            gameDisplay.blit(shopSelection, (318, 208))
        if selectShop == 2:
            gameDisplay.blit(shopSelection, (456, 208))
        if selectShop == 3:
            gameDisplay.blit(shopSelection, (318, 254))
        if selectShop == 4:
            gameDisplay.blit(shopSelection, (456, 254))
        if selectShop == 5:
            gameDisplay.blit(shopSelection, (318, 300))
        if selectShop == 6:
            gameDisplay.blit(shopSelection, (456, 300))

        
        pygame.display.update()
		
		
		
def esc():
    global level
    escape = True
    selectEsc = 1
    while escape:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and selectEsc == 3:
                    escape = False
                    level = "menu"
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN and selectEsc == 1:
                    escape = False
                if event.key == pygame.K_UP and selectEsc != 1:
                    selectEsc -= 1
                if event.key == pygame.K_DOWN and selectEsc != 3:
                    selectEsc += 1
        display()
        if level == L0S1:
            displayL0S1()
        lives()
        gameDisplay.blit(escScreen, (0, 0))            
        if selectEsc == 1:
            gameDisplay.blit(escSelect1, (0, 0))
        if selectEsc == 2:
            gameDisplay.blit(escSelect2, (0, 0))
        if selectEsc == 3:
            gameDisplay.blit(escSelect3, (0, 0))
        
        pygame.display.update()
        
stage = 1             

def motionStop():
    global heroMotion
    global heroMoveL
    global heroMoveD
    global heroMoveR
    global heroMoveU
    motionQue = False
    heroMotion = False
    heroMoveL = False
    heroMoveD = False
    heroMoveR = False
    heroMoveU = False

def LCol(X,Y):
    global blocked2
    blocked2 = False
    if mob1Y == Y and mob1X == (X - 25) or Y == mob2Y and X == (mob2X + 25) or Y == mob3Y and X == (mob3X + 25) or Y == mob4Y and X == (mob4X + 25) or Y == mob5Y and X == (mob5X + 25) or Y == mob6Y and X == (mob6X + 25) or Y == mob7Y and X == (mob7X + 25) or Y == mob8Y and X == (mob8X + 25) or Y == mob9Y and X == (mob9X + 25) or Y == mob10Y and X == (mob10X + 25):
        blocked2 = True
    else:
        if shopY == Y and shopX == (X - 25) or X == 0:
            blocked2 = True
        else:
            if Y == rock1Y and X == (rock1X + 25)and rock1 or Y == rock2Y and X == (rock2X + 25)and rock2 or Y == rock3Y and X == (rock3X + 25)and rock3 or Y == rock4Y and X == (rock4X + 25)and rock4 or Y == rock5Y and X == (rock5X + 25)and rock5 or Y == rock6Y and X == (rock6X + 25)and rock6 or Y == rock7Y and X == (rock7X + 25)and rock7 or Y == rock8Y and X == (rock8X + 25)and rock8 or Y == rock9Y and X == (rock9X + 25)and rock9:
                blocked2 = True
            else:
                pass

def RCol(X,Y):
    global blocked2
    blocked2 = False
    if mob1Y == Y and mob1X == (X + 25) or Y == mob2Y and X == (mob2X - 25) or Y == mob3Y and X == (mob3X - 25) or Y == mob4Y and X == (mob4X - 25) or Y == mob5Y and X == (mob5X - 25) or Y == mob6Y and X == (mob6X - 25) or Y == mob7Y and X == (mob7X - 25) or Y == mob8Y and X == (mob8X - 25) or Y == mob9Y and X == (mob9X - 25) or Y == mob10Y and X == (mob10X - 25):
        blocked2 = True
    else:
        if shopY == Y and shopX == (X + 25) or X == 875:
            blocked2 = True
        else:
            if Y == rock1Y and X == (rock1X - 25)and rock1 or Y == rock2Y and X == (rock2X - 25)and rock2 or Y == rock3Y and X == (rock3X - 25)and rock3 or Y == rock4Y and X == (rock4X - 25)and rock4 or Y == rock5Y and X == (rock5X - 25)and rock5 or Y == rock6Y and X == (rock6X - 25)and rock6 or Y == rock7Y and X == (rock7X - 25)and rock7 or Y == rock8Y and X == (rock8X - 25)and rock8 or Y == rock9Y and X == (rock9X - 25)and rock9:
                blocked2 = True
            else:
                pass
def UCol(X,Y):
    global blocked2
    blocked2 = False
    if mob1X == X and mob1Y == (Y - 25) or X == mob2X and Y == (mob2Y + 25) or X == mob3X and Y == (mob3Y + 25) or X == mob4X and Y == (mob4Y + 25) or X == mob5X and Y == (mob5Y + 25) or X == mob6X and Y == (mob6Y + 25) or X == mob7X and Y == (mob7Y + 25) or X == mob8X and Y == (mob8Y + 25) or X == mob9X and Y == (mob9Y + 25) or X == mob10X and Y == (mob10Y + 25):
        blocked2 = True
    else:
        if shopX == X and shopY == (Y - 25) or Y == 0:
            blocked2 = True
        else:
            if X == rock1X and Y == (rock1Y + 25)and rock1 or X == rock2X and Y == (rock2Y + 25)and rock2 or X == rock3X and Y == (rock3Y + 25)and rock3 or X == rock4X and Y == (rock4Y + 25)and rock4 or X == rock5X and Y == (rock5Y + 25)and rock5 or X == rock6X and Y == (rock6Y + 25)and rock6 or X == rock7X and Y == (rock7Y + 25)and rock7 or X == rock8X and Y == (rock8Y + 25)and rock8 or X == rock9X and Y == (rock9Y + 25)and rock9:
                blocked2 = True
            else:
                pass
            
def DCol(X,Y):
    global blocked2
    blocked2 = False
    if mob1X == X and mob1Y == (Y + 25) or X == mob2X and Y == (mob2Y - 25) or X == mob3X and Y == (mob3Y - 25) or X == mob4X and Y == (mob4Y - 25) or X == mob5X and Y == (mob5Y - 25) or X == mob6X and Y == (mob6Y - 25) or X == mob7X and Y == (mob7Y - 25) or X == mob8X and Y == (mob8Y - 25) or X == mob9X and Y == (mob9Y - 25) or X == mob10X and Y == (mob10Y - 25):
        blocked2 = True
    else:
        if shopX == X and shopY == (Y + 25) or Y == 475:
            blocked2 = True
        else:
            if X == rock1X and Y == (rock1Y - 25)and rock1 or X == rock2X and Y == (rock2Y - 25)and rock2 or X == rock3X and Y == (rock3Y - 25)and rock3 or X == rock4X and Y == (rock4Y - 25)and rock4 or X == rock5X and Y == (rock5Y - 25)and rock5 or X == rock6X and Y == (rock6Y - 25)and rock6 or X == rock7X and Y == (rock7Y - 25)and rock7 or X == rock8X and Y == (rock8Y - 25)and rock8 or X == rock9X and Y == (rock9Y - 25)and rock9 :
                blocked2 = True
            else:
                pass

def L0S1_L(X,Y):
    global blocked
    blocked = False
    if X == 125 and Y < 225 and Y > 175 or X == 100 and Y < 200 and Y > 150:
        blocked = True
    else:
        if X == 75 and Y < 175 and Y > 0 or X == 125 and Y < 325 and Y > 275:
            blocked = True
        else:
            if X == 100 and Y < 300 and Y > 250 or X == 75 and Y < 500 and Y > 300:
                blocked = True
            else:
                if X == 100 and Y < 500 and Y > 425 or X == 125 and Y < 450 and Y > 375:
                    blocked = True
                else:
                    if X == 150 and Y < 400 and Y > 325 or X == 175 and Y < 350 and Y > 275:
                        blocked = True
                    else:
                        if X == 200 and Y < 300 and Y > 250 or X == 250 and Y < 275 and Y > 200:
                            blocked = True
                        else:
                            if X == 275 and Y < 225 and Y > 175 or X == 350 and Y < 200 and Y > 150:
                                blocked = True
                            else:
                                if X == 550 and Y < 175 and Y > 125 or X == 600 and Y < 225 and Y > 150:
                                    blocked = True
                                else:
                                    if X == 625 and Y < 250 and Y > 200 or X == 675 and Y < 300 and Y > 225:
                                        blocked = True
                                    else:
                                        if X == 700 and Y < 325 and Y > 275 or X == 725 and Y < 375 and Y > 300:
                                            blocked = True
                                        else:
                                            if X == 750 and Y < 450 and Y > 400 or X == 450 and Y < 325 and Y > 225:
                                                blocked = True
                                            else:
                                                if X == 375 and Y < 375 and Y > 300 or X == 375 and Y < 425 and Y > 375:
                                                    blocked = True
                                                else:
                                                    if X == 225 and Y < 425 and Y > 300 or X == 250 and Y < 325 and Y > 275:
                                                        blocked = True
                                                    else:
                                                        pass

def L0S1_R(X,Y):
    global blocked
    blocked = False
    if X == 100 and Y < 425 and Y > 350 or X == 125 and Y < 375 and Y > 300:
        blocked = True
    else:
        if X == 150 and Y < 325 and Y > 250 or X == 175 and Y < 275 and Y > 225:
            blocked = True
        else:
            if X == 225 and Y < 250 and Y > 175 or X == 250 and Y < 200 and Y > 150:
                blocked = True
            else:
                if X == 325 and Y < 175 and Y > 125 or X == 525 and Y < 200 and Y > 150:
                    blocked = True
                else:
                    if X == 575 and Y < 250 and Y > 175 or X == 600 and Y < 275 and Y > 225:
                        blocked = True
                    else:
                        if X == 650 and Y < 325 and Y > 250 or X == 675 and Y < 350 and Y > 300:
                            blocked = True
                        else:
                            if X == 700 and Y < 375 and Y > 325 or X == 700 and Y < 450 and Y > 400:
                                pblocked = True
                            else:
                                if X == 675 and Y < 475 and Y > 425 or X == 650 and Y < 500 and Y > 450:
                                    blocked = True
                                else:
                                    if X == 775 and Y < 400 and Y > 350 or X == 750 and Y < 450 and Y > 375:
                                        blocked = True
                                    else:
                                        if X == 800 and Y < 375 and Y > 325 or X == 800 and Y < 300 and Y > 250:
                                            blocked = True
                                        else:
                                            if X == 775 and Y < 275 and Y > 225 or X == 800 and Y < 300 and Y > 250:
                                                blocked = True
                                            else:
                                                if X == 800 and Y < 250 and Y > 150 or X == 825 and Y < 200 and Y > 75:
                                                    blocked = True
                                                else:
                                                    if X == 800 and Y < 100 and Y > 50 or X == 750 and Y < 75 and Y > 25:
                                                        blocked = True
                                                    else:
                                                        if X == 725 and Y < 50 and Y > 0 or X == 200 and Y < 425 and Y > 300:
                                                            blocked = True
                                                        else:
                                                            if X == 225 and Y < 325 and Y > 275 or X == 325 and Y < 325 and Y > 225:
                                                                blocked = True
                                                            else:
                                                                if X == 350 and Y < 375 and Y > 300 or X == 350 and Y < 425 and Y > 375:
                                                                    blocked = True
                                                                else:
                                                                    pass
def L0S1_U(X,Y):
    global blocked
    global level
    global heroX
    global heroY
    blocked = False
    if heroX == (chunk*16) and heroY == (chunk*13):
        level = L0S2
        heroX = (chunk*15)
        heroY = (chunk*13)
        blocked = True
    else:
        if Y == 225 and X < 125 or Y == 325 and X < 125 and X > 50 or Y == 25:
            blocked = True
        else:
            if Y == 450 and X < 125 and X > 75 or Y == 400 and X < 150 and X > 100:
                blocked = True
            else:
                if Y == 350 and X < 175 and X > 125 or Y == 300 and X < 200 and X > 150:
                    blocked = True
                else:
                    if Y == 275 and X < 250 and X > 175 or Y == 225 and X < 275 and X > 225:
                        blocked = True
                    else:
                        if Y == 200 and X < 350 and X > 250 or Y == 175 and X < 550 and X > 325:
                            blocked = True
                        else:
                            if Y == 200 and X < 600 and X > 525 or Y == 250 and X < 625 and X > 575:
                                blocked = True
                            else:
                                if Y == 275 and X < 675 and X > 600 or Y == 325 and X < 700 and X > 650:
                                    blocked = True
                                else:
                                    if Y == 350 and X < 725 and X > 675 or Y == 425 and X < 725 and X > 675:
                                        blocked = True
                                    else:
                                        if Y == 300 and X < 900 and X > 800 or Y == 275 and X < 825 and X > 775:
                                            blocked = True
                                        else:
                                            if Y == 100 and X < 850 and X > 800 or Y == 75 and X < 825 and X > 750:
                                                blocked = True
                                            else:
                                                if Y == 50 and X < 775 and X > 725 or Y == 375 and X < 725 and X > 675:
                                                    blocked = True
                                                else:
                                                    if Y == 425 and X < 375 and X > 200 or Y == 300 and X < 350 and X > 225:
                                                        blocked = True
                                                    else:
                                                        if Y == 375 and X < 375 and X > 325 or Y == 325 and X < 250 and X > 200:
                                                            blocked = True
                                                        else:
                                                            if Y == 325 and X < 450 and X > 325:
                                                                blocked = True
                                                            else:
                                                                pass

def L0S1_D(X,Y):
    global blocked
    blocked = False
    if Y == 250 and X < 100 or Y == 275 and X < 125 and X > 75:
        blocked = True
    else:
        if Y == 400 and X < 125 and X > 50 or Y == 350 and X < 150 and X > 100:
            blocked = True
        else:
            if Y == 300 and X < 175 and X > 125 or Y == 250 and X < 200 and X > 150:
                blocked = True
            else:
                if Y == 225 and X < 250 and X > 175 or Y == 175 and X < 275 and X > 225:
                    blocked = True
                else:
                    if Y == 150 and X < 350 and X > 250 or Y == 125 and X < 550 and X > 325:
                        blocked = True
                    else:
                        if Y == 150 and X < 600 and X > 525 or Y == 200 and X < 625 and X > 575:
                            blocked = True
                        else:
                            if Y == 225 and X < 675 and X > 600 or Y == 275 and X < 700 and X > 650:
                                blocked = True
                            else:
                                if Y == 300 and X < 725 and X > 675 or Y == 400 and X < 750 and X > 675:
                                    blocked = True
                                else:
                                    if Y == 350 and X < 725 and X > 675 or Y == 425 and X < 775 and X > 725:
                                        blocked = True
                                    else:
                                        if Y == 375 and X < 800 and X > 750 or Y == 350 and X < 825 and X > 775:
                                            blocked = True
                                        else:
                                            if Y == 325 and X < 900 and X > 800 or Y == 225 and X < 825 and X > 775:
                                                blocked = True
                                            else:
                                                if Y == 150 and X < 850 and X > 800 or Y == 150 and X < 100 and X > 50:
                                                    blocked = True
                                                else:
                                                    if Y == 400 and X < 375 and X > 200 or Y == 275 and X < 350 and X > 225:
                                                        blocked = True
                                                    else:
                                                        if Y == 350 and X < 375 and X > 325 or Y == 300 and X < 250 and X > 200:
                                                            blocked = True
                                                        else:
                                                            if Y == 175 and X < 125 and X > 75 or Y == 225 and X < 450 and X > 325:
                                                                blocked = True
                                                            else:
                                                                pass
    

def runL0S1():
    #=========================L0S1 LOOP===========================#
    #----------Global---------#

    global chunk

    #People#

    global heroX
    global heroY
    global heroHP
    global balance
    global potions
    global view
    global frame
    global Herobusy

    global shop
    global shopX
    global shopY

    #Mobs#

    global mob1X
    global mob1Y
    global mob1HP
    global mob1
    global MobAttack1
    
    global mob2X
    global mob2Y
    global mob2HP
    global mob2
    global MobAttack2

    global mob3X
    global mob3Y
    global mob3HP
    global mob3
    global MobAttack3

    global mob4X
    global mob4Y
    global mob4HP
    global mob4
    global MobAttack4

    global mob5X
    global mob5Y
    global mob5HP
    global mob5
    global MobAttack5

    global mob6X
    global mob6Y
    global mob6HP
    global mob6
    global MobAttack6

    global mob7X
    global mob7Y
    global mob7HP
    global mob7
    global MobAttack7

    global mob8X
    global mob8Y
    global mob8HP
    global mob8
    global MobAttack8

    global mob9X
    global mob9Y
    global mob9HP
    global mob9
    global MobAttack9

    global mob10X
    global mob10Y
    global mob10HP
    global mob10
    global MobAttack10

    global blocked
    global blocked2

    #Objects#

    global coin1
    global coin1X
    global coin1Y

    global coin2
    global coin2X
    global coin2Y

    global coin3
    global coin3X
    global coin3Y

    global coin4
    global coin4X
    global coin4Y

    global coin5
    global coin5X
    global coin5Y

    global coin6
    global coin6X
    global coin6Y

    global coin7
    global coin7X
    global coin7Y

    global coin8
    global coin8X
    global coin8Y

    global coin9
    global coin9X
    global coin9Y

    global coin10
    global coin10X
    global coin10Y

    #Potions
    global potion1
    global potion1X
    global potion1Y

    global potion2
    global potion2X
    global potion2Y

    global potion3
    global potion3X
    global potion3Y

    global potion4
    global potion4X
    global potion4Y

    global potion5
    global potion5X
    global potion5Y


    #rocks
    global rock1
    global rock1X
    global rock1Y

    global rock2
    global rock2X
    global rock2Y

    global rock3
    global rock3X
    global rock3Y

    global rock4
    global rock4X 
    global rock4Y

    global rock5
    global rock5X
    global rock5Y

    global rock6
    global rock6X
    global rock6Y

    global rock7
    global rock7X
    global rock7Y

    global rock8
    global rock8X
    global rock8Y

    global rock9
    global rock9X
    global rock9Y

    #============OTHER============#

    global random10
    global random8
    global randomChoice

    global select

    global counter
    global counter2
    
    global clock
    global aniclock
    global movclock
    global chatclock
    global hitclock
    global atkClockM1
    global atkClockM2
    
    global reset
    global Time

    #sprites

    global L0S1
    #global L1S2
    #global L1S3

    global level


    global heroIMG
    global heroHit

    #PROFILES
    global talk

    global line1
    global line1X
    global line2
    global line2X
    global line3
    global line3X
    global line4
    global line4X
    global line5
    global line5X
    global line6
    global line6X
    global line7
    global line7X
    
    global merchantProfile

    global profile


    global merchant

    global store
    global shopSelection

    global bush
    global rock

    global coin
    global potion

    global logo
    global escScreen
    global escSelect1
    global escSelect2
    global escSelect3
    global selection
    global heart

    global mob1
    global mob1Hurt

    global mob2
    global mob2Hurt


    

    
    #============ CLOCKS ===========#
    heroMoving = False
    heroMotion = False
    heroMoveL = False
    heroMoveD = False
    heroMoveR = False
    heroMoveU = False
    while level == L0S1:
        clock += 1
        Time = (clock/500000)
        if Time%1 == 0:
            pass
        #This^ may need to change if resource becomes too demanding.

        aniclock += 1
        if aniclock == 600000:
            pass
        if aniclock == 1200000:
            aniclock = 0

        if heroHit:
            hitclock += 1
            if hitclock == 15:
                heroHit = False
                hitclock = 0

        chatclock += 1
        if chatclock == 300:
            chatclock = 0
            line1 = ""
            line2 = ""
            line3 = ""
            line4 = ""
            line5 = ""
            line6 = ""
            line7 = ""
            profile = ""

        
                
        if heroMotion:
            movclock += 1
            if heroMoveL == True:
                L0S1_L(heroX,heroY)
                LCol(heroX,heroY)
                if blocked == False and blocked2 == False:
                    if movclock == 3:
                        heroX -= 5
                        frame = 1
                    if movclock == 6:
                        heroX -= 5
                        frame = 2
                    if movclock == 9:
                        heroX -= 5
                        frame = 1
                    if movclock == 12:
                        heroX -= 5
                        frame = 1
                    if movclock == 15:
                        heroX -= 5
                        frame = 0

                                                                            

            if heroMoveR == True:
                L0S1_R(heroX,heroY)
                RCol(heroX,heroY)
                if blocked == False and blocked2 == False:
                    if movclock == 3:
                        heroX += 5
                        frame = 1
                    if movclock == 6:
                        heroX += 5
                        frame = 2
                    if movclock == 9:
                        heroX += 5
                        frame = 1
                    if movclock == 12:
                        heroX += 5
                        frame = 1
                    if movclock == 15:
                        heroX += 5
                        frame = 0

            if heroMoveU == True:
                L0S1_U(heroX,heroY)
                UCol(heroX,heroY)
                if blocked == False and blocked2 == False:
                    if movclock == 3:
                        heroY -= 5
                        frame = 1
                    if movclock == 6:
                        heroY -= 5
                        frame = 2
                    if movclock == 9:
                        heroY -= 5
                        frame = 1
                    if movclock == 12:
                        heroY -= 5
                        frame = 1
                    if movclock == 15:
                        heroY -= 5
                        frame = 0

            if heroMoveD == True:
                L0S1_D(heroX,heroY)
                DCol(heroX,heroY)
                if blocked == False and blocked2 == False:
                    if movclock == 3:
                        heroY += 5
                        frame = 1
                    if movclock == 6:
                        heroY += 5
                        frame = 2
                    if movclock == 9:
                        heroY += 5
                        frame = 1
                    if movclock == 12:
                        heroY += 5
                        frame = 1
                    if movclock == 15:
                        heroY += 5
                        frame = 0
            
            
            if movclock == 15:
                movclock = 0
                if not heroMoving:
                    heroMotion = False
                    heroMoveL = False
                    heroMoveD = False
                    heroMoveR = False
                    heroMoveU = False
                    
            
            #============Messages===========#
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                    select = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP2 or event.key == pygame.K_2:
                    select = 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP3 or event.key == pygame.K_3:
                    select = 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    heal()
            #====================RESPAWN====================#
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if mob1HP < 1:
                        mob1X = (chunk*12)
                        mob1Y = (chunk*12)
                        mob1HP = 5
                        counter = 0
                            
                    if mob2HP < 1:
                        mob2X= (chunk*12)
                        mob2Y = (chunk*2)
                        mob2HP = 3
                        counter = 0
            #==================INTERACT====================#
            #--------------mob1--------------#
            if event.type == pygame.KEYDOWN and select == 2: 
                if event.key == pygame.K_UP and heroX == mob1X and heroY == (mob1Y + 25):
                    mob1HP = (mob1HP - 1)
                    view = 4
                    if randomChoice < 4:
                        heroHurt()
                        heroHP -= 1
                    mob1hurt()
                    
            if event.type == pygame.KEYDOWN and select == 2: 
                if event.key == pygame.K_DOWN and heroX == mob1X and heroY == (mob1Y - 25):
                    mob1HP = (mob1HP - 1)
                    view = 2
                    if randomChoice < 4:
                        heroHurt()
                        heroHP -= 1
                    mob1hurt()

            if event.type == pygame.KEYDOWN and select == 2: 
                if event.key == pygame.K_LEFT and heroY == mob1Y and heroX == (mob1X + 25):
                    mob1HP = (mob1HP - 1)
                    view = 1
                    if randomChoice < 4:
                        heroHurt()
                        heroHP -= 1
                    mob1hurt()
            
            if event.type == pygame.KEYDOWN and select == 2: 
                if event.key == pygame.K_RIGHT and heroY == mob1Y and heroX == (mob1X - 25):
                    mob1HP = (mob1HP - 1)
                    view = 3
                    if randomChoice < 4:
                        heroHurt()
                        heroHP -= 1
                    mob1hurt()
                    
            #------------mob2------------#

            if event.type == pygame.KEYDOWN and select == 2: 
                if event.key == pygame.K_UP and heroX == mob2X and heroY == (mob2Y + 25):
                    mob2HP = (mob2HP - 1)
                    view = 4
                    if randomChoice < 4:
                        heroHurt()
                        heroHP -= 2
                    mob2hurt()
                    
            if event.type == pygame.KEYDOWN and select == 2: 
                if event.key == pygame.K_DOWN and heroX == mob2X and heroY == (mob2Y - 25):
                    mob2HP = (mob2HP - 1)
                    view =2
                    if randomChoice < 4:
                        heroHurt()
                        heroHP -= 2
                    mob2hurt()

            if event.type == pygame.KEYDOWN and select == 2: 
                if event.key == pygame.K_LEFT and heroY == mob2Y and heroX == (mob2X + 25):
                    mob2HP = (mob2HP - 1)
                    view = 1
                    if randomChoice < 4:
                        heroHurt()
                        heroHP -= 2
                    mob2hurt()
            
            if event.type == pygame.KEYDOWN and select == 2: 
                if event.key == pygame.K_RIGHT and heroY == mob2Y and heroX == (mob2X - 25):
                    mob2HP = (mob2HP - 1)
                    view = 3
                    if randomChoice < 4:
                        heroHurt()
                        heroHP -= 2
                    mob2hurt()  
                                         
            #------------SHOP------------#

            if event.type == pygame.KEYDOWN and select == 1: 
                if event.key == pygame.K_UP and heroX == shopX and heroY == (shopY + 25):
                    view = 4
                    merchant = pygame.image.load("Assets/Entities/Merchant/MerchantF.png")
                    line1 = "Merchant: "
                    line1X = 433
                    line2 = "Hello there, what can I do for you today?"
                    line2X = 513
                    profile = "merchantProfile"
                    shopOpen()
                    line1 = "Merchant: "
                    line2 = "Come again!"
                    line2X = 435
                    heroMotion
            if event.type == pygame.KEYDOWN and select == 1: 
                if event.key == pygame.K_DOWN and heroX == shopX and heroY == (shopY - 25):
                    view = 2
                    merchant = pygame.image.load("Assets/Entities/Merchant/MerchantB.png")
                    line1 = "Merchant: "
                    line1X = 433
                    line2 = "Hello there, what can I do for you today?"
                    line2X = 513
                    profile = "merchantProfile"
                    shopOpen()
                    line1 = "Merchant: "
                    line2 = "Come again!"
                    line2X = 435

            if event.type == pygame.KEYDOWN and select == 1: 
                if event.key == pygame.K_LEFT and heroY == shopY and heroX == (shopX + 25):
                    view = 1
                    merchant = pygame.image.load("Assets/Entities/Merchant/MerchantL.png")
                    line1 = "Merchant: "
                    line1X = 433
                    line2 = "Hello there, what can I do for you today?"
                    line2X = 513
                    profile = "merchantProfile"
                    shopOpen()
                    line1 = "Merchant: "
                    line2 = "Come again!"
                    line2X = 435
            
            if event.type == pygame.KEYDOWN and select == 1: 
                if event.key == pygame.K_RIGHT and heroY == shopY and heroX == (shopX - 25):
                    view = 3
                    merchant = pygame.image.load("Assets/Entities/Merchant/MerchantR.png")
                    line1 = "Merchant: "
                    line1X = 430
                    line2 = "Hello there, what can I do for you today?"
                    line2X = 513
                    profile = "merchantProfile"
                    shopOpen()
                    line1 = "Merchant: "
                    line2 = "Come again!"
                    line2X = 435

            #------------ROCK------------#
            if event.type == pygame.KEYDOWN and select == 3:
                
                if event.key == pygame.K_LEFT:
                    view = 1
                    if heroX == (rock1X + 25) and heroY == rock1Y and rock1:
                        rock1 = False
                    if heroX == (rock2X + 25) and heroY == rock2Y and rock2:
                        rock2 = False
                    if heroX == (rock3X + 25) and heroY == rock3Y and rock3:
                        rock3 = False
                    if heroX == (rock4X + 25) and heroY == rock4Y and rock4:
                        rock4 = False
                    if heroX == (rock5X + 25) and heroY == rock5Y and rock5:
                        rock5 = False
                    if heroX == (rock6X + 25) and heroY == rock6Y and rock6:
                        rock6 = False
                    if heroX == (rock7X + 25) and heroY == rock7Y and rock7:
                        rock7 = False
                    if heroX == (rock8X + 25) and heroY == rock8Y and rock8:
                        rock8 = False
                    if heroX == (rock9X + 25) and heroY == rock9Y and rock9:
                        rock9 = False
                        
                if event.key == pygame.K_DOWN:
                    view =  2
                    if heroY == (rock1Y - 25) and heroX == rock1X and rock1:
                        rock1 = False
                    if heroY == (rock2Y - 25) and heroX == rock2X and rock2:
                        rock2 = False
                    if heroY == (rock3Y - 25) and heroX == rock3X and rock3:
                        rock3 = False
                    if heroY == (rock4Y - 25) and heroX == rock4X and rock4:
                        rock4 = False
                    if heroY == (rock5Y - 25) and heroX == rock5X and rock5:
                        rock5 = False
                    if heroY == (rock6Y - 25) and heroX == rock6X and rock6:
                        rock6 = False
                    if heroY == (rock7Y - 25) and heroX == rock7X and rock7:
                        rock7 = False
                    if heroY == (rock8Y - 25) and heroX == rock8X and rock8:
                        rock8 = False
                    if heroY == (rock9Y - 25) and heroX == rock9X and rock9:
                        rock9 = False
                    

                if event.key == pygame.K_RIGHT:
                    view = 3
                    if heroX == (rock1X - 25) and heroY == rock1Y and rock1:
                        rock1 = False
                    if heroX == (rock2X - 25) and heroY == rock2Y and rock2:
                        rock2 = False
                    if heroX == (rock3X - 25) and heroY == rock3Y and rock3:
                        rock3 = False
                    if heroX == (rock4X - 25) and heroY == rock4Y and rock4:
                        rock4 = False
                    if heroX == (rock5X - 25) and heroY == rock5Y and rock5:
                        rock5 = False
                    if heroX == (rock6X - 25) and heroY == rock6Y and rock6:
                        rock6 = False
                    if heroX == (rock7X - 25) and heroY == rock7Y and rock7:
                        rock7 = False
                    if heroX == (rock8X - 25) and heroY == rock8Y and rock8:
                        rock8 = False
                    if heroX == (rock9X - 25) and heroY == rock9Y and rock9:
                        rock9 = False
                    
                        
                if event.key == pygame.K_UP:
                    view = 4
                    if heroY == (rock1Y + 25) and heroX == rock1X and rock1:
                        rock1 = False
                    if heroY == (rock2Y + 25) and heroX == rock2X and rock2:
                        rock2 = False
                    if heroY == (rock3Y + 25) and heroX == rock3X and rock3:
                        rock3 = False
                    if heroY == (rock4Y + 25) and heroX == rock4X and rock4:
                        rock4 = False
                    if heroY == (rock5Y + 25) and heroX == rock5X and rock5:
                        rock5 = False
                    if heroY == (rock6Y + 25) and heroX == rock6X and rock6:
                        rock6 = False
                    if heroY == (rock7Y + 25) and heroX == rock7X and rock7:
                        rock7 = False
                    if heroY == (rock8Y + 25) and heroX == rock8X and rock8:
                        rock8 = False
                    if heroY == (rock9Y + 25) and heroX == rock9X and rock9:
                        rock9 = False
                    
                    
                        
            #==========ESC===========#
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    esc()
            #==========HERO MOVEMENT===========#

            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_a and heroMotion == False: #LEFT
                    view = 1
                    heroMotion = True
                    heroMoving = True
                    heroMoveL = True
                    
         
                if event.key == pygame.K_d and heroMotion == False: #RIGHT
                    view = 3
                    heroMotion = True
                    heroMoving = True
                    heroMoveR = True

                        
                if event.key == pygame.K_w and heroMotion == False: # UP
                    view = 4
                    heroMotion = True
                    heroMoving = True
                    heroMoveU = True

                    
                if event.key == pygame.K_s and heroMotion == False: #DOWN
                    view = 2
                    heroMotion = True
                    heroMoving = True
                    heroMoveD = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_w:
                    heroMoving = False

            
        
            
        if mob1HP < 1:
            mob1X = 0
            mob1Y = 0

        if mob2HP < 1:
            mob2X = 0
            mob2Y = 0

        if heroHP < 1:
            heroX = (chunk*0)
            heroY = (chunk*9)
            heroHP = 8
            balance = 0

        #-----------------PICK UP----------------#
        if heroX == coin1X and heroY == coin1Y and coin1 == True:
            coin1 = False
            coin1X = 0
            coin1Y = 0
            balance += 1

        if heroX == coin2X and heroY == coin2Y and coin2 == True:
            coin2 = False
            coin2X = 0
            coin2Y = 0
            balance += 1

        if heroX == coin3X and heroY == coin3Y and coin3 == True:
            coin3 = False
            coin3X = 0
            coin3Y = 0
            balance += 1

        if heroX == coin4X and heroY == coin4Y and coin4 == True:
            coin4 = False
            coin4X = 0
            coin4Y = 0
            balance += 1

        if heroX == coin5X and heroY == coin5Y and coin5 == True:
            coin5 = False
            coin5X = 0
            coin5Y = 0
            balance += 1

        if heroX == coin6X and heroY == coin6Y and coin6 == True:
            coin6 = False
            coin6X = 0
            coin6Y = 0
            balance += 1

        if heroX == coin7X and heroY == coin7Y and coin7 == True:
            coin7 = False
            coin7X = 0
            coin7Y = 0
            balance += 1

        if heroX == coin8X and heroY == coin8Y and coin8 == True:
            coin8 = False
            coin8X = 0
            coin8Y = 0
            balance += 1

        if heroX == coin9X and heroY == coin9Y and coin9 == True:
            coin9 = False
            coin9X = 0
            coin9Y = 0
            balance += 1

        if heroX == coin10X and heroY == coin10Y and coin10 == True:
            coin10 = False
            coin10X = 0
            coin10Y = 0
            balance += 1

        if heroX == potion1X and heroY == potion1Y and potion1 == True:
            potion1 = False
            potion1X = 0
            potion1Y = 0
            potions += 1
            
        if heroX == potion2X and heroY == potion2Y and potion2 == True:
            potion2 = False
            potion2X = 0
            potion2Y = 0
            potions += 1
                
        if heroX == potion3X and heroY == potion3Y and potion3 == True:
            potion3 = False
            potion3X = 0
            potion3Y = 0
            potions += 1
                
        if heroX == potion4X and heroY == potion4Y and potion4 == True:
            potion4 = False
            potion4X = 0
            potion4Y = 0
            potions += 1
                
        if heroX == potion5X and heroY == potion5Y and potion5 == True:
            potion5 = False
            potion5X = 0
            potion5Y = 0
            potions += 1
            
        #======================= START MOB 1 AI ======================#

        if MobAttack1:
            atkClockM1 += 1
            if atkClockM1 == 100:
                heroHurt()
                heroHP -= 1
                MobAttack1 = False
                atkClockM1 = 0
                
        counter = (counter + 1)
        
        if heroX == (mob1X + 25) and heroY == mob1Y  or heroX == (mob1X - 25) and heroY == mob1Y  or heroY == (mob1Y + 25) and heroX == mob1X  or heroY == (mob1Y - 25) and heroX == mob1X:
            MobAttack1 = True
        else:
            MobAttack1 = False
            if counter == 60 and mob1HP != 0 or heroX == mob1X and heroY == mob1Y:
                randomChoice = (random.choice(random8))
                
                if randomChoice == 1 or randomChoice == 5 and heroX < mob1X or randomChoice == 6 and heroX < mob1X or heroX == mob1X and heroY == mob1Y: #LEFT
                    L0S1_L(mob1X,mob1Y)
                    LCol(mob1X,mob1Y)
                    if blocked == False and blocked2 == False:
                        mob1X = (mob1X - 25)
                        if mob1X == heroX and mob1Y == heroY:
                            mob1X = (mob1X + 25)
                                                        


                if randomChoice == 2 or randomChoice == 5 and heroX > mob1X or randomChoice == 6 and heroX > mob1X or heroX == mob1X and heroY == mob1Y: #RIGHT
                    L0S1_R(mob1X,mob1Y)
                    RCol(mob1X,mob1Y)
                    if blocked == False and blocked2 == False:
                        mob1X = (mob1X + 25)
                        if mob1X == heroX and mob1Y == heroY:
                            mob1X = (mob1X - 25)
                                                            


                if randomChoice == 3 or randomChoice == 7 and heroY < mob1Y or randomChoice == 8 and heroY < mob1Y or heroX == mob1X and heroY == mob1Y: # UP
                    L0S1_U(mob1X,mob1Y)
                    UCol(mob1X,mob1Y)
                    if blocked == False and blocked2 == False:
                        mob1Y = (mob1Y - 25)
                        if mob1Y == heroY and mob1X == heroX:
                            mob1Y = (mob1Y + 25)
                                            
                if randomChoice == 4 or randomChoice == 7 and heroY > mob1Y or randomChoice == 8 and heroY > mob1Y or heroX == mob1X and heroY == mob1Y: #DOWN
                    L0S1_D(mob1X,mob1Y)
                    DCol(mob1X,mob1Y)
                    if blocked == False and blocked2 == False:
                        mob1Y = (mob1Y + 25)
                        if mob1Y == heroY and mob1X == heroX:
                            mob1Y = (mob1Y - 25)

                                                                                        
                

        #====================== END mob1 AI =====================#
                                                
        #======================= START mob2 AI ======================#

        if MobAttack2:
            atkClockM2 += 1
            if atkClockM2 == 100:
                heroHurt()
                heroHP -= 2
                atkClockM2 = 0
                MobAttack2 = False
                                                                                        
        if heroX == (mob2X + 25) and heroY == mob2Y  or heroX == (mob2X - 25) and heroY == mob2Y  or heroY == (mob2Y + 25) and heroX == mob2X  or heroY == (mob2Y - 25) and heroX == mob2X:
            MobAttack1 = True
        else:
            MobAttack1 = False
            if counter == 60 and mob2HP != 0 or heroX == mob2X and heroY == mob2Y:
                randomChoice = (random.choice(random8))
                
                if randomChoice == 1 or randomChoice == 5 and heroX < mob2X or randomChoice == 6 and heroX < mob2X or heroX == mob2X and heroY == mob2Y: #LEFT
                    L0S1_L(mob2X,mob2Y)
                    LCol(mob2X,mob2Y)
                    if blocked == False and blocked2 == False:
                        mob2X = (mob2X - 25)
                        if mob2X == heroX and mob2Y == heroY:
                            mob2X = (mob2X + 25)
                                                        


                if randomChoice == 2 or randomChoice == 5 and heroX > mob2X or randomChoice == 6 and heroX > mob2X or heroX == mob2X and heroY == mob2Y: #RIGHT
                    L0S1_R(mob2X,mob2Y)
                    RCol(mob2X,mob2Y)
                    if blocked == False and blocked2 == False:
                        mob2X = (mob2X + 25)
                        if mob2X == heroX and mob2Y == heroY:
                            mob2X = (mob2X - 25)
                                                            


                if randomChoice == 3 or randomChoice == 7 and heroY < mob2Y or randomChoice == 8 and heroY < mob2Y or heroX == mob2X and heroY == mob2Y: # UP
                    L0S1_U(mob2X,mob2Y)
                    UCol(mob2X,mob2Y)
                    if blocked == False and blocked2 == False:
                        mob2Y = (mob2Y - 25)
                        if mob2Y == heroY and mob2X == heroX:
                            mob2Y = (mob2Y + 25)
                                            
                if randomChoice == 4 or randomChoice == 7 and heroY > mob2Y or randomChoice == 8 and heroY > mob2Y or heroX == mob2X and heroY == mob2Y: #DOWN
                    L0S1_D(mob2X,mob2Y)
                    DCol(mob2X,mob2Y)
                    if blocked == False and blocked2 == False:
                        mob2Y = (mob2Y + 25)
                        if mob2Y == heroY and mob2X == heroX:
                            mob2Y = (mob2Y - 25)

                #====================== END mob2 AI =====================#
        if counter == 30 or counter == 60:
            randomChoice = (random.choice(random10))
            if randomChoice == 8 or randomChoice == 9 or randomChoice == 10:
                randomChoice = (random.choice(random10))
                if randomChoice > 8:
                    merchant = pygame.image.load("Assets/Entities/Merchant/MerchantF.png")
            if randomChoice == 5 or randomChoice == 6 or randomChoice == 7:
                randomChoice = (random.choice(random10))
                if randomChoice > 9:
                    merchant = pygame.image.load("Assets/Entities/Merchant/MerchantL.png")
            if randomChoice == 2 or randomChoice == 3 or randomChoice == 4:
                randomChoice = (random.choice(random10))
                if randomChoice > 9:
                    merchant = pygame.image.load("Assets/Entities/Merchant/MerchantR.png")
            if randomChoice == 1:
                randomChoice = (random.choice(random10))
                if randomChoice > 8:
                    merchant = pygame.image.load("Assets/Entities/Merchant/MerchantB.png")
                    
        
        if counter == 60:
            counter = 0
            

            #============= Display ==============#
        gameDisplay.fill(white)
        display()
        if level == L0S1:
            displayL0S1()
        lives()
        pygame.display.update()
#====================== END L0S1 =====================#

def L0S2_L(X,Y):
    global blocked
    blocked = False
    if X == 300:
        blocked = True
    else:
        pass
def L0S2_R(X,Y):
    global blocked
    blocked = False
    if X == 575:
        blocked = True
    else:
        pass
def L0S2_U(X,Y):
    global blocked
    blocked = False
    if Y == 175:
        blocked = True
    else:
        pass
def L0S2_D(X,Y):
    global level
    global heroX
    global heroY
    global blocked
    blocked = False
    if heroX == (chunk*15) and heroY == (chunk*13):
        level = L0S1
        heroX = (chunk*16)
        heroY = (chunk*13)
        blocked = True
    else:
        if Y == 325:
            blocked = True
        else:
            pass
    
def runL0S2():
    global chunk

    #People#

    global heroX
    global heroY
    global heroHP
    global balance
    global potions
    global view
    global frame
    global Herobusy

    global shop
    global shopX
    global shopY

    #Mobs#

    global mob1X
    global mob1Y
    global mob1HP
    global mob1
    global MobAttack1
    
    global mob2X
    global mob2Y
    global mob2HP
    global mob2
    global MobAttack2

    global mob3X
    global mob3Y
    global mob3HP
    global mob3
    global MobAttack3

    global mob4X
    global mob4Y
    global mob4HP
    global mob4
    global MobAttack4

    global mob5X
    global mob5Y
    global mob5HP
    global mob5
    global MobAttack5

    global mob6X
    global mob6Y
    global mob6HP
    global mob6
    global MobAttack6

    global mob7X
    global mob7Y
    global mob7HP
    global mob7
    global MobAttack7

    global mob8X
    global mob8Y
    global mob8HP
    global mob8
    global MobAttack8

    global mob9X
    global mob9Y
    global mob9HP
    global mob9
    global MobAttack9

    global mob10X
    global mob10Y
    global mob10HP
    global mob10
    global MobAttack10

    global blocked
    global blocked2

    #Objects#

    global coin1
    global coin1X
    global coin1Y

    global coin2
    global coin2X
    global coin2Y

    global coin3
    global coin3X
    global coin3Y

    global coin4
    global coin4X
    global coin4Y

    global coin5
    global coin5X
    global coin5Y

    global coin6
    global coin6X
    global coin6Y

    global coin7
    global coin7X
    global coin7Y

    global coin8
    global coin8X
    global coin8Y

    global coin9
    global coin9X
    global coin9Y

    global coin10
    global coin10X
    global coin10Y

    #Potions
    global potion1
    global potion1X
    global potion1Y

    global potion2
    global potion2X
    global potion2Y

    global potion3
    global potion3X
    global potion3Y

    global potion4
    global potion4X
    global potion4Y

    global potion5
    global potion5X
    global potion5Y


    #rocks
    global rock1
    global rock1X
    global rock1Y

    global rock2
    global rock2X
    global rock2Y

    global rock3
    global rock3X
    global rock3Y

    global rock4
    global rock4X 
    global rock4Y

    global rock5
    global rock5X
    global rock5Y

    global rock6
    global rock6X
    global rock6Y

    global rock7
    global rock7X
    global rock7Y

    global rock8
    global rock8X
    global rock8Y

    global rock9
    global rock9X
    global rock9Y

    #============OTHER============#

    global random10
    global random8
    global randomChoice

    global select

    global counter
    global counter2
    
    global clock
    global aniclock
    global movclock
    global chatclock
    global hitclock
    global atkClockM1
    global atkClockM2
    
    global reset
    global Time

    #sprites

    global L0S1
    #global L1S2
    #global L1S3

    global level


    global heroIMG
    global heroHit

    #PROFILES
    global talk

    global line1
    global line1X
    global line2
    global line2X
    global line3
    global line3X
    global line4
    global line4X
    global line5
    global line5X
    global line6
    global line6X
    global line7
    global line7X
    
    global merchantProfile

    global profile


    global merchant

    global store
    global shopSelection

    global bush
    global rock

    global coin
    global potion

    global logo
    global escScreen
    global escSelect1
    global escSelect2
    global escSelect3
    global selection
    global heart

    heroMoving = False
    heroMotion = False
    heroMoveL = False
    heroMoveD = False
    heroMoveR = False
    heroMoveU = False
    while level == L0S2:
        if heroMotion:
            movclock += 1
            if heroMoveL == True:
                L0S2_L(heroX,heroY)
                LCol(heroX,heroY)
                if blocked == False and blocked2 == False:
                    if movclock == 3:
                        heroX -= 5
                        frame = 1
                    if movclock == 6:
                        heroX -= 5
                        frame = 2
                    if movclock == 9:
                        heroX -= 5
                        frame = 1
                    if movclock == 12:
                        heroX -= 5
                        frame = 1
                    if movclock == 15:
                        heroX -= 5
                        frame = 0

                                                                            

            if heroMoveR == True:
                L0S2_R(heroX,heroY)
                RCol(heroX,heroY)
                if blocked == False and blocked2 == False:
                    if movclock == 3:
                        heroX += 5
                        frame = 1
                    if movclock == 6:
                        heroX += 5
                        frame = 2
                    if movclock == 9:
                        heroX += 5
                        frame = 1
                    if movclock == 12:
                        heroX += 5
                        frame = 1
                    if movclock == 15:
                        heroX += 5
                        frame = 0

            if heroMoveU == True:
                L0S2_U(heroX,heroY)
                UCol(heroX,heroY)
                if blocked == False and blocked2 == False:
                    if movclock == 3:
                        heroY -= 5
                        frame = 1
                    if movclock == 6:
                        heroY -= 5
                        frame = 2
                    if movclock == 9:
                        heroY -= 5
                        frame = 1
                    if movclock == 12:
                        heroY -= 5
                        frame = 1
                    if movclock == 15:
                        heroY -= 5
                        frame = 0

            if heroMoveD == True:
                L0S2_D(heroX,heroY)
                DCol(heroX,heroY)
                if blocked == False and blocked2 == False:
                    if movclock == 3:
                        heroY += 5
                        frame = 1
                    if movclock == 6:
                        heroY += 5
                        frame = 2
                    if movclock == 9:
                        heroY += 5
                        frame = 1
                    if movclock == 12:
                        heroY += 5
                        frame = 1
                    if movclock == 15:
                        heroY += 5
                        frame = 0
            
            
            if movclock == 15:
                movclock = 0
                if not heroMoving:
                    heroMotion = False
                    heroMoveL = False
                    heroMoveD = False
                    heroMoveR = False
                    heroMoveU = False
                    
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and heroMotion == False: #LEFT
                    view = 1
                    heroMotion = True
                    heroMoving = True
                    heroMoveL = True
                        
             
                if event.key == pygame.K_d and heroMotion == False: #RIGHT
                    view = 3
                    heroMotion = True
                    heroMoving = True
                    heroMoveR = True

                            
                if event.key == pygame.K_w and heroMotion == False: # UP
                    view = 4
                    heroMotion = True
                    heroMoving = True
                    heroMoveU = True

                        
                if event.key == pygame.K_s and heroMotion == False: #DOWN
                    view = 2
                    heroMotion = True
                    heroMoving = True
                    heroMoveD = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_w:
                    heroMoving = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                    select = 1
                if event.key == pygame.K_KP2 or event.key == pygame.K_2:
                    select = 2
                if event.key == pygame.K_KP3 or event.key == pygame.K_3:
                    select = 3
                if event.key == pygame.K_r:
                    heal()
            
        gameDisplay.fill(white)
        display()
        if level == L0S1:
            displayL0S1()
        lives()
        pygame.display.update()
        
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if level == "menu":
        Menu()

    if level == L0S1:
        transition()
        runL0S1()

    if level == L0S2:
        transition()
        resetEntities()
        runL0S2()
        
pygame.quit()
quit()
