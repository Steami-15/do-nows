import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Flappy Bird") 
clock = pygame.time.Clock() 
font = pygame.font.Font(None, 36) 
font2 = pygame.font.Font(None, 72)
bg_x1 = 0
bg_x2 = 800

bird_img = pygame.image.load('helpme.png').convert_alpha()

score = 0
pygame.mixer.music.load("musicman.mp3")
pygame.mixer.music.set_volume(0.1)

jump = pygame.mixer.Sound("jump 1.mp3")
jump.set_volume(0.2)

dead = pygame.mixer.Sound("death.mp3")
dead.set_volume(0.9)

start = pygame.mixer.Sound("start.mp3")
start.set_volume(0.3)

lost = pygame.mixer.Sound("lost.mp3")
lost.set_volume(0.2)

pipe_img = pygame.image.load('pipe.png').convert_alpha()

background_img = pygame.image.load('background6.png').convert_alpha()

running = True

def check_collision(bx, by, px, py):
    if bx + 30 > px and bx < px + 50 and by < py:
        return True
    if bx + 30 > px and bx < px + 50 and by + 30 > py + 150:
        return True
    return False

class Bird:
    def __init__(self):
        self.y = 200
        self.velocity = 0
    def flap(self):
        self.velocity = -3.5 
       
    def physics(self):
        self.velocity += 0.1 
        self.y += self.velocity
       
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (50, self.y, 30, 30))
bird = Bird()

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, 400)
        self.gap = 150
        self.top_pipe = pygame.transform.flip(pipe_img, False, True)
        self.bottom_pipe = pipe_img
        
    def move(self):
        self.x -= 2 
    def draw(self):
        top_height = self.height
        bottom_height = 800 - (self.height + self.gap)
        
        screen.blit(self.top_pipe, (self.x, top_height -  self.top_pipe.get_height()))
        
        screen.blit(self.bottom_pipe, (self.x, self.height + self.gap))
pipes = []
spawn_pipe = 0
ticker = 0
frameWidth = 50
frameHeight = 51
frameNum = 0
ticker = 0

pygame.mixer.Sound.play(start)
pygame.time.delay(2400)
pygame.mixer.music.play(-1)
while running:
    clock.tick(60)
    ticker+=1 
    if ticker%10 == 0: 
        ticker = 0
        score+=1
        
    bird.physics()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird.flap()
            pygame.mixer.Sound.play(jump)
    spawn_pipe += 1 
    if spawn_pipe >= 150: 
        pipes.append(Pipe(800)) 
        spawn_pipe = 0 
    bg_x1 -= 2
    bg_x2 -= 2
    if bg_x1 <= -800:
        bg_x1 = 800
    if bg_x2 <= -800:
        bg_x2 = 800
    #move pipes!
    for pipe in pipes: #walk through list of pipes
        pipe.move() #move each pipe
        if check_collision(50, bird.y, pipe.x, pipe.height): #check collision with bird
            running = False #kill game if you hit a pipe
    #destroy pipes that have gone off screen
    i = len(pipes) - 1 #start at end of list
    while i >= 0:
        if pipes [i].x <= -50: #check if pipe is off screen
            pipes.pop(i) #remove from list
        i -= 1 #this increments the while loop
    #-end of game loop--------
    # Render section----
    ticker+=1
    if ticker%10 == 0: 
            ticker = 0
            frameNum+=1
            score+=1
    if frameNum>12:
         frameNum = 0
    screen.fill((0, 0, 0))
    
    
    screen.blit(background_img, (bg_x1, 0))
    screen.blit(background_img, (bg_x2, 0))
    screen.blit(bird_img, (50, bird.y), (frameWidth*frameNum, 0, frameWidth, frameHeight))
    for pipe in pipes:
        pipe.draw()
    score_text = font.render("Score:", True, (255, 255, 255))
    screen.blit(score_text, (650, 20)) # Position the score in the top-right corner
    score_text2 = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text2, (750, 20)) # Position the score in the top-right corner

   
    pygame.display.flip()

#---end of game loop-----------
pygame.mixer.music.stop()
pygame.mixer.Sound.play(dead)
pygame.mixer.Sound.play(lost)
text = font2.render("GAME OVER", True, (255, 50, 50))
screen.blit(text, (200, 200))
pygame.display.flip()
pygame.time.delay(2500)
text = font2.render("YOU'RE TRASH", True, (255, 50, 50))
screen.blit(text, (170, 300))
pygame.display.flip()
pygame.time.delay(500)
pygame.quit()
