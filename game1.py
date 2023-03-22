import pygame
import random

pygame.mixer.init()

pygame.init()


#creating ground for the game
screen_width=900
screen_height=600
gamewindow=pygame.display.set_mode((screen_width,screen_height))

#Background image
backimg=pygame.image.load("startscreen.jpeg")
backimg=pygame.transform.scale(backimg,(screen_width,screen_height)).convert_alpha()

#game title
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()

#colors: these have different RGB values just like ascii values
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
coffee=(111,78,55)
green=(0,255,0)
light_grey=(211,211,211)

#setting frame rate
clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)

def textscreen(text,color,x,y):
    screentext=font.render(text,True,color)
    gamewindow.blit(screentext,[x,y])

def plot_snake(gamewindow,color,snklist,snake_size):
    for x,y in snklist:
        pygame.draw.rect(gamewindow,color,[x,y, snake_size, snake_size])

#Home Screen
def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(backimg,(0,0))
        textscreen("WELCOME TO SNAKES",black,235,190)
        textscreen("PRESS SPACEBAR TO PLAY",black,190,250)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    #pygame.mixer.music.load('background.mp3')
                    pygame.mixer.music.load('background2.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)
        
        
    
#game loop
def gameloop():
    pygame.mixer.music.load('background.mp3')
    #pygame.mixer.music.load('background2.mp3')
    pygame.mixer.music.play()
    with open("hi-score.txt","r") as f:
        hiscore=f.read()
    #game specific variables
    exit_game= False
    game_over= False
    snake_x=45
    snake_y=55
    snake_size=15
    velocity_x=0
    velocity_y=0
    food_x=random.randint(0,screen_width/2)
    food_y=random.randint(0,screen_height/2)
    score=0
    var_vel=5
    fps=60
    
    #snake length
    snklist=[]
    snklength=1
    
    while not exit_game:
       
        if game_over:
            with open("hi-score.txt","w") as f:
                f.write(str(hiscore))
            gamewindow.fill(white)
            textscreen("Game Over!!! Press Enter To Continue",green,100,250)
            pygame.display.update() 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                  
                    
                    if event.key==pygame.K_RIGHT:
                        velocity_x = var_vel
                        velocity_y= 0

                    if event.key==pygame.K_LEFT:
                        velocity_x = -var_vel
                        velocity_y= 0

                    if event.key==pygame.K_UP:
                        velocity_y = -var_vel
                        velocity_x = 0

                    if event.key==pygame.K_DOWN:
                        velocity_y = var_vel
                        velocity_x = 0
                    if event.key==pygame.K_q:
                        score+=10
                    if event.key==pygame.K_e:
                        snklength+=5
            
            snake_x+=velocity_x
            snake_y+=velocity_y   

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score+=10

                food_x=random.randint(0,screen_width/2)
                food_y=random.randint(0,screen_height/2)
                snklength+=5
                if score>int(hiscore):
                    hiscore=score
                
            gamewindow.fill(light_grey)
            
        #display of score on the screen
            textscreen("Score: "+str(score)+"  HISCORE:"+str(hiscore),coffee,5,5) 
        #adding the fruits

            pygame.draw.rect(gamewindow,red,[food_x,food_y, snake_size, snake_size])

        #adding snake head  
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snklist.append(head)

            if len(snklist)>snklength:
                del snklist[0]
            
            if head in snklist[:-1]:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
               

            plot_snake(gamewindow,black,snklist,snake_size)
        pygame.display.update() 

    #for fps
        clock.tick(fps)
    
    pygame.quit()
    quit()
  
#welcome()

