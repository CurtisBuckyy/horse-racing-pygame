#Horse Racing Game created by Curtis Buckingham (https://github.com/CurtisBuckyy)

import random
import sys, pygame
from pygame import *
pygame.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Horse Racing Game")
clock = pygame.time.Clock()

#Loading Icon
icon = pygame.image.load('horse_racing_icon.ico')
pygame.display.set_icon(icon)

#Loading Fonts
font = pygame.font.Font('Louis George Cafe Bold.ttf', 40)
info_font = pygame.font.Font('Louis George Cafe Bold.ttf', 35)
horse_name_font = pygame.font.Font('Louis George Cafe Bold.ttf', 30)

#Loading Images for Background
bg_images = []

bg_image_start = pygame.image.load('bg_stadium_start.png').convert_alpha()
bg_images.append(bg_image_start)

for i in range (4):
    bg_image_mid = pygame.image.load('bg_stadium_mid.png').convert_alpha()
    bg_images.append(bg_image_mid)
    bg_width = bg_images[i].get_width()

bg_image_finish = pygame.image.load('bg_stadium_finish.png').convert_alpha()
bg_images.append(bg_image_finish)

#Horse Image List
horse_image_list = ['horse.png', 'horse2.png', 'horse3.png', 'horse4.png']
horse_icon_list = ['horse1_icon.png','horse2_icon.png','horse3_icon.png', 'horse4_icon.png']

class Horse():
    def __init__(self, horse_image, position_y, colour, name):
        self.postion_x = 0
        self.image = pygame.image.load(horse_image).convert_alpha()
        self.speed = ((1,4))
        self.colour = colour
        self.name = name
        self.rect = self.image.get_rect(midbottom = (self.postion_x, position_y))
        self.movement_count = 0

    def draw(self):
        screen.blit(self.image, self.rect)

    def move_forward(self, range_1, range_2):
        self.rect.x += random.randrange(range_1, range_2)
        self.movement_count += 1


#Creating horse objects of Class Horse

horse1 = Horse(horse_image_list[0], 880, "red", "Storm Blossom") 
horse2 = Horse(horse_image_list[1], 790, "purple", "Darkheart")
horse3 = Horse(horse_image_list[2], 710, "yellow", "Trinity")
horse4 = Horse(horse_image_list[3], 630, "green", "Clover")

def displayEarnings():

    #Display earnings on start screen, if file which money is stored doesn't exist then
        # a file is created.

    try:
        with open('earnings.txt') as f:
            current_earnings = f.readline()

        total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "Black")
        screen.blit(total_earnings, (870,30))

    except:
        total_earnings = info_font.render('Total Earnings: $0', False , "Black")
        screen.blit(total_earnings, (870,30))

        with open('earnings.txt', 'w') as f:
            f.write(str(50))
    
def decreaseEarnings():

    #Decreasing amount of game money using text file methods

    with open('earnings.txt') as f:
        current_earnings = f.readline()
        current_earnings = int(current_earnings)

    if current_earnings > 50:
        with open('earnings.txt', 'w') as f:
            new_earnings = int(current_earnings) - 50
            f.write(str(new_earnings))

def increaseEarnings():

    #Increasing amount of game money using text file methods

     with open('earnings.txt') as f:
        current_earnings = f.readline()
        current_earnings = int(current_earnings)

     if current_earnings > 0 and current_earnings < 100000:

        with open('earnings.txt', 'w') as f:
            new_earnings = int(current_earnings) + 200
            f.write(str(new_earnings))

def displayDistanceLeft():
    display_distance = info_font.render('Metres left: ' + str(610 - selected_horse.movement_count), False , "white")
    screen.blit(display_distance, (1000,27.5))

def playMusic():
    if music_playing:
        pygame.mixer.music.load('game_music.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

def drawBg():
    for x in range (6):
        screen.blit(bg_images[x], ((x * bg_width) - scroll, 0))

def grabResults():

    #Setting position of horses and storing into dictionary with relevant names

    results_dict = {}

    red_horse = horse1.rect.x
    purple_horse = horse2.rect.x
    yellow_horse = horse3.rect.x
    green_horse = horse4.rect.x

    results_dict["Storm Blossom"] = red_horse
    results_dict["Darkheart"] = purple_horse
    results_dict["Trinity"] = yellow_horse
    results_dict["Clover"] = green_horse

    sortedDict = sorted(results_dict.items(), key=lambda x:x[1], reverse=True)

    return sortedDict

def checkWinner():

    #Conditional statements to check which horse is in first place during the race

    if horse1.rect.x > horse2.rect.x and horse1.rect.x > horse3.rect.x and horse1.rect.x > horse4.rect.x:
        return "Red"

    elif horse2.rect.x > horse1.rect.x and horse2.rect.x > horse3.rect.x and horse2.rect.x > horse4.rect.x:
        return "Purple"

    elif horse3.rect.x > horse1.rect.x and horse3.rect.x  > horse2.rect.x and horse3.rect.x > horse4.rect.x:
        return "Yellow"

    elif horse4.rect.x > horse1.rect.x and horse4.rect.x > horse2.rect.x and horse4.rect.x > horse3.rect.x:
        return "Green"

    else:
        return "Black"

def displayResults():

    sortedDict = grabResults()

    text = font.render('Results:' , False , "white")
    screen.blit(text, (300,250))

    if selected_horse.name == sortedDict[0][0]:
        text2 = font.render('1st Place (Winner): ' + str(sortedDict[0][0]), False , "green")
        screen.blit(text2, (300,300))

    else:
        text_winner = font.render('1st Place (Winner): ' + str(sortedDict[0][0]), False , "yellow")
        screen.blit(text_winner, (300,300))

    text3 = font.render('2nd Place: ' + str(sortedDict[1][0]), False , "white")
    screen.blit(text3, (300,350))

    text4 = font.render('3rd Place: ' + str(sortedDict[2][0]) , False , "white")
    screen.blit(text4, (300,400))

    text5 = font.render('4th Place: ' + str(sortedDict[3][0]) , False , "white")
    screen.blit(text5, (300,450))

    if selected_horse.name == sortedDict[0][0]:
        text6= horse_name_font.render('Bet won with: ' + selected_horse.name + " and earned $200", False , "green")
        screen.blit(text6, (300,600))
        increaseEarnings()

    else:
        text7= horse_name_font.render('Your have lost your bet with: ' + selected_horse.name , False , "red")
        screen.blit(text7, (300,600))
        decreaseEarnings()

#Initalising Variables
game_active = True
start_check = False
music_playing = True
scroll = 0

while True:

    for event in pygame.event.get():
        global selected_horse
        if event.type == pygame.QUIT: sys.exit() 
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1 and start_check == False:
            start_check = True
            selected_horse = horse1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and start_check == False:
            start_check = True
            selected_horse = horse2

        if event.type == pygame.KEYDOWN and event.key == pygame.K_3 and start_check == False:
            start_check = True
            selected_horse = horse3

        if event.type == pygame.KEYDOWN and event.key == pygame.K_4 and start_check == False:
            start_check = True
            selected_horse = horse4

        if event.type == MOUSEBUTTONDOWN:
            if horse1_rect.collidepoint(event.pos):
                start_check = True
                selected_horse = horse1

            if horse2_rect.collidepoint(event.pos):
                start_check = True
                selected_horse = horse2

            if horse3_rect.collidepoint(event.pos):
                start_check = True
                selected_horse = horse3

            if horse4_rect.collidepoint(event.pos):
                start_check = True
                selected_horse = horse4

        #Event check to pause and unpause game music
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:

            if music_playing == True:
                music_playing = False
                pygame.mixer.music.pause()

            else:
                pygame.mixer.music.unpause()
                music_playing = True
             
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_active == False:
            
            #Resetting Variables for Game Restart
            horse1.movement_count = 0
            horse2.movement_count = 0
            horse3.movement_count = 0
            horse4.movement_count = 0
            horse1.rect.x = 0
            horse2.rect.x = 0
            horse3.rect.x = 0
            horse4.rect.x = 0
            scroll = 0
            game_active = True

    if game_active: 
        
        bg_image = pygame.image.load('bg_stadium_start.png').convert_alpha()
        screen.blit(bg_image, (0,0))

        #Grabbing total earnings and outputting to horse selection screen
        displayEarnings()

        if start_check:
            
            #Displaying moving background function with multiple images
            drawBg()

            info_bar_image = pygame.image.load('info_bar.png').convert_alpha()
            screen.blit(info_bar_image, (0,0))
            
            horse4.draw(), horse3.draw(), horse2.draw(), horse1.draw()

            winner = checkWinner()

            default_range = ((1, 4))

            #Calling Horse class move_forward function to start the race

            horse1.move_forward(default_range[0], default_range[1]), horse2.move_forward(default_range[0], default_range[1])
            horse3.move_forward(default_range[0], default_range[1]), horse4.move_forward(default_range[0], default_range[1])

            scroll += 12 #Incrementing scroll variable by 12 for moving background function

            displayDistanceLeft() # Calling function to display metres left in horse race

            #Ending game if each horse has finished the race and calling the subsequent functions
            if horse1.movement_count == 610 and horse2.movement_count == 610 and horse3.movement_count == 610 and horse4.movement_count == 610:
                game_active = False
                start_check = False
                results_board_image = pygame.image.load('results_board.png').convert_alpha()
                screen.blit(results_board_image, (185,80))
                displayResults()
                grabResults()   

            trophy_image = pygame.image.load('trophy.png').convert_alpha()

            screen.blit(trophy_image, (10,10))
            
            winner_text = info_font.render('1st Place: ', False , "White")
            screen.blit(winner_text, (100,27.5))

            winner_text_colour = info_font.render(str(winner), False , str(winner))
            screen.blit(winner_text_colour, (260,27.5))

            current_horse_text = horse_name_font.render('Chosen Horse:', False , "White")
            screen.blit(current_horse_text, (450,27.5))

            current_horse_colour = horse_name_font.render(selected_horse.name, False , str(selected_horse.colour))
            screen.blit(current_horse_colour, (660,27.5))

        else:
            playMusic()
            horse_selection_image = pygame.image.load('select_horse.png').convert_alpha()
            screen.blit(horse_selection_image, (185,65))

            horse1_icon = pygame.image.load(horse_icon_list[0]).convert_alpha()
            horse1_rect = horse1_icon.get_rect(midbottom = (1050, 350))
            screen.blit(horse1_icon, horse1_rect)

            horse2_icon = pygame.image.load(horse_icon_list[1]).convert_alpha()
            horse2_rect = horse2_icon.get_rect(midbottom = (1050, 470))
            screen.blit(horse2_icon, horse2_rect)

            horse3_icon = pygame.image.load(horse_icon_list[2]).convert_alpha()
            horse3_rect = horse3_icon.get_rect(midbottom = (1050, 590))
            screen.blit(horse3_icon, horse3_rect)

            horse4_icon = pygame.image.load(horse_icon_list[3]).convert_alpha()
            horse4_rect = horse4_icon.get_rect(midbottom = (1050, 710))
            screen.blit(horse4_icon, horse4_rect)

    pygame.display.update()
    clock.tick(60)
 