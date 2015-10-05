import pygame, time, sys, pyganim
from random import randint
import pyganim
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.display.set_caption("Card Switch")
w = 720
h = 640
pygame.mixer.music.load("Song\keygensong.wav")
pygame.mixer.music.play()

infoObject = pygame.display.Info()
pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

w = infoObject.current_w
h = infoObject.current_h

menuPicture = pygame.image.load('Background/Main Screen.jpg')
menuPicture = pygame.transform.scale(menuPicture, (w, h))
rules1Picture = pygame.image.load('Background/How to play page 1.jpg')
rules1Picture = pygame.transform.scale(rules1Picture, (720, 640))
rules2Picture = pygame.image.load('Background/How to play page 2.jpg')
rules2Picture = pygame.transform.scale(rules2Picture, (720, 640))
readyPicture = pygame.image.load('Background/Final page before game.jpg')
readyPicture = pygame.transform.scale(readyPicture, (720, 640))
gamePicture = pygame.image.load('Background/Background for in-Game.png')
gamePicture = pygame.transform.scale(gamePicture, (720, 640))

rect = gamePicture.get_rect()
rect = rect.move((0, 0))

size = (w, h)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
w, h = screen.get_size()
print w, h
c = pygame.time.Clock()
font = pygame.font.Font("fonts/PressStart2p.ttf", 26)



def main():
    menu(rect, menuPicture)
    menu(rect, rules1Picture)
    menu(rect, rules2Picture)

    screen.fill((250, 250, 250))
    screen.blit(gamePicture, rect)
    pygame.display.flip()

    imagelist = generateList()
    levelnum = 0
    score = 0

    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont=pygame.font.SysFont("Courier New", 72)
    font.set_bold(True)

    # set up high score
    hisc=open("high_score.txt","r+")
    highscore=hisc.read()
    highscoreint=int(highscore)
    print highscoreint

    # render text
    label2= myfont.render("High Score= " +str(highscore), 1, (255,215,0))
    screen.blit(label2,(40,50))
    label = myfont.render("Score = " + str(score), 1, (255,215,0))
    screen.blit(label, (40, 100))
    renderText(25, 515)
    
	
   
	

    while levelnum<2:
        global chosen_card
        chosen_card = []

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        global correctlist
        useranswers = []
        correctlist = []

        level(levelnum, imagelist)

        card_count = 0
        result = 1
        w = 10
        h = 550
        while card_count < 3 + levelnum:
            card = inputSuit()
            number = inputCard()

            renderText(25, 515)
            card+=number
            useranswers.append(card)
            print 'Result ' + str(result) + " = "+ str(card)
            result+=1
            card_count+=1

        i = 0
        while i < 3+levelnum:
            if correctlist[i] == useranswers[i]:
                score += 1
            else:
                print correctlist
                print useranswers
                print "Sorry, you lost the game: " + str(score)
				
                #high score implemented into the game
                if score>highscoreint:
                        hisc2=open("high_score.txt","w")
                        highscoreint=score
                        hisc2.write(str(highscoreint))
                        print"new high score is: "+str(highscoreint)
                
                #even if the high score hasn't been broken
                print "high score is: "+str(highscoreint)
                label = font.render("Sorry, you lost the game/nScore = " + str(score), 1, (255,215,0))
                screen.blit(label, (100, 100))
                time.sleep(3)
                pygame.quit()
                sys.exit()

            i+=1

        print "score for level " + str(levelnum)+ " is " + str(score)
        screen.fill((250, 250, 250))
        screen.blit(gamePicture, rect)
        label = font.render("Score = " + str(score), 1, (255,215,0))
        screen.blit(label, (100, 100))
        pygame.display.flip()

        levelnum += 1
      #  print correctlist
        time.sleep(10)
        imagelist = generateList()
        c.tick(40)



def level(num1, list1):
    time = 3-(0.25*num1)

    count = 0
    while count < num1+3:
        # create the PygAnimation object, selects the images to display.
        animObj = pyganim.PygAnimation([(randomCard(list1), time)], loop=False)
        animObj.play()

        while animObj.isFinished() != True:
            animObj.blit(screen, (100,100))
            pygame.display.update()

        animObj = pyganim.PygAnimation([(pygame.image.load("Background/back_card.gif"), 0.5)], loop=False)
        animObj.play()
        animObj.blit(screen, (100,100))
        pygame.display.update()


        print count
        c.tick(time)
        count += 1

def randomCard(list1):
    randnumber = randint(1, (len(list1)-1))
    if randnumber not in chosen_card:
        correctlist.append(randnumber)
        chosen_card.append(randnumber)
    else:
        return randomCard(list1)

    return pygame.image.load("Cards/"+str(randnumber)+".gif")


def generateList():
    count = 1
    imagelist = []
    while count <= 52:
        imagelist.append(pygame.image.load("Cards/"+str(count)+".gif"))
        count+=1
    return imagelist


def inputSuit():
    user_answers = []
    while 1:
        event = pygame.event.wait()
        if event.type in (pygame.K_h, pygame.KEYDOWN):
            card=0
            return card
        elif event.type in (pygame.K_c, pygame.KEYDOWN):
            card=13
            return card
        elif event.type in (pygame.K_d, pygame.KEYDOWN):
            card=26
            return card
        elif event.type in (pygame.K_s, pygame.KEYDOWN):
            card=39
            return card


def inputCard():
    while 1:
        event = pygame.event.wait()
        if event.type in (pygame.K_a, pygame.KEYDOWN):
            return 1
        elif event.type in (pygame.K_2, pygame.KEYDOWN):
            return 2
        elif event.type in (pygame.K_3, pygame.KEYDOWN):
            return 3
        elif event.type in (pygame.K_4, pygame.KEYDOWN):
            return 4
        elif event.type in (pygame.K_5, pygame.KEYDOWN):
            return 5
        elif event.type in (pygame.K_6, pygame.KEYDOWN):
            return 6
        elif event.type in (pygame.K_7, pygame.KEYDOWN):
            return 7
        elif event.type in (pygame.K_8, pygame.KEYDOWN):
            return 8
        elif event.type in (pygame.K_9, pygame.KEYDOWN):
            return 9
        elif event.type in (pygame.K_t, pygame.KEYDOWN):
            return 10
        elif event.type in (pygame.K_j, pygame.KEYDOWN):
            return 11
        elif event.type in (pygame.K_q, pygame.KEYDOWN):
            return 12
        elif event.type in (pygame.K_k, pygame.KEYDOWN):
            return 13

def renderText(w, h):
    font.set_bold(True)
    label = font.render("Answer now", 1, (255,215,0))
    screen.blit(label, (w, h))
    pygame.display.flip()

def renderDash(w, h):
    font.set_bold(True)
    label = font.render("_", 1, (255,215,0))
    screen.blit(label, (w, h))
    pygame.display.flip()



def menu(rect, first):
    screen.fill((250, 250, 250))
    screen.blit(first, rect)
    pygame.display.flip()
    while 1:
        input = pygame.event.wait()
        if input.type in (pygame.K_SPACE, pygame.KEYDOWN):
            return 0



main()

