################################################
################################################
################################################
#########*******###*******####**********########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**********########
########**#####**#**#####**###**################
########**#####**#**#####**###**################
########**######***######**###**################
########**###############**###**################
########**###############**###**################
################################################
########Copyright © Maresal Programming#########
################################################

import pygame,random
 
pygame.init()

class SnakeGame:
    def __init__(self):
        self.colors = {"white":(255, 255, 255),"black" : (0, 0, 0),"red":(202, 4, 43),"green":(78, 178, 4),"blue":(4, 104, 178)}
        self.dis_width = 600
        self.dis_height = 400
 
        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Snake Game by Maresal Prm')
 
        self.clock = pygame.time.Clock()

        self.snake_block = 10
        self.snake_speed = 15
        
        self.font_style = pygame.font.SysFont("comicsans", 35)
        self.score_font = pygame.font.SysFont("comicsans", 25)
 
 
    def Your_score(self,score):
        value = self.score_font.render("Your Score: " + str(score), True, self.colors["white"])
        self.dis.blit(value, [0, 0])

    
    def our_snake(self,snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.dis, self.colors["green"], [x[0], x[1], snake_block, snake_block])
    
    
    def message(self,msg,color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 9, self.dis_height / 3])
    
    def gameLoop(self):
        game_over = False
        game_close = False
    
        x1 = self.dis_width / 2
        y1 = self.dis_height / 2
    
        x1_change = 0
        y1_change = 0
    
        snake_List = []
        LengthSnake = 1
    
        foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0

    
        while not game_over:
            while game_close == True:
                self.dis.fill(self.colors["black"])
                self.message("You Lost! Press C - Play Again or Q - Quit",self.colors["red"])
                self.Your_score(LengthSnake - 1)
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.gameLoop()
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        x1_change = -self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        x1_change = self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        y1_change = -self.snake_block
                        x1_change = 0
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        y1_change = self.snake_block
                        x1_change = 0
    
            if x1 >= self.dis_width or x1 < 0 or y1 >= self.dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            self.dis.fill(self.colors["black"])
            pygame.draw.rect(self.dis, self.colors["red"], [foodx, foody, self.snake_block, self.snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > LengthSnake:
                del snake_List[0]
    
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
    
            self.our_snake(self.snake_block, snake_List)
            self.Your_score(LengthSnake - 1)
    
            pygame.display.update()
    
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
                LengthSnake += 1
                
    
            self.clock.tick(self.snake_speed)
    
        pygame.quit()
        quit()
 
 
SnakeGame().gameLoop()