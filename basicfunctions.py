import pygame, time, sys, pyganim
from random import randint
import pyganim
pygame.init()
w = 720
h = 640

size = (w, h)
screen = pygame.display.set_mode(size)
c = pygame.time.Clock()
font = pygame.font.Font("fonts/PressStart2p.ttf", 26)


def main():
    menu()
    imagelist = generateList()
    levelnum = 1
    score = 0

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
        while card_count < levelnum+2:
            time.sleep(7)
            second=0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if second==0:
                    card = inputSuit(event)
                    second=1
                else:
                    number = inputCard(event)

            card+=number
            useranswers.append(card)
            print 'Result ' + str(result) + " = "+ str(card)
            result+=1
            card_count+=1

        i = 0
        while i<3:
            if correctlist[i] == useranswers[i]:
                score += 1
            else:
                print correctlist
                print useranswers
                print "Sorry, you lost the game: " + str(score)
                return 0

            i+=1

        print "score for level " + str(levelnum)+ " is " + str(score)

        levelnum += 1
      #  print correctlist
        time.sleep(10)
        imagelist = generateList()
        c.tick(40)



def level(num1, list1):
    time = 3-(0.25*num1)

    count = 0
    while count < num1+2:
        # create the PygAnimation object, selects the images to display.
        animObj = pyganim.PygAnimation([(randomCard(list1), time)], loop=False)
        animObj.play()

        while animObj.isFinished() != True:
            animObj.blit(screen, (100,100))
            pygame.display.update()

        print count
        c.tick(time)
        count += 1

def randomCard(list1):
    randnumber = randint(0, (len(list1)-1))
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


def inputSuit(event):
    user_answers = []
    card = 0
    if event.key == pygame.K_h:
        card=0
    if event.key == pygame.K_c:
        card=13
    if event.key == pygame.K_d:
        card=26
    if event.key == pygame.K_s:
        card=39

    return card

def inputCard(event):
    if event.key == pygame.K_a:
        return 1
    elif event.key == pygame.K_2:
        return 2
    elif event.key == pygame.K_3:
        return 3
    elif event.key == pygame.K_4:
        return 4
    elif event.key == pygame.K_5:
        return 5
    elif event.key == pygame.K_6:
        return 6
    elif event.key == pygame.K_7:
        return 7
    elif event.key == pygame.K_8:
        return 8
    elif event.key == pygame.K_9:
        return 9
    elif event.key == pygame.K_t:
        return 10
    elif event.key == pygame.K_j:
        return 11
    elif event.key == pygame.K_q:
        return 12
    elif event.key == pygame.K_k:
        return 13


def menu():
    pass


main()

