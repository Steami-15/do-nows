import pygame

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Valentine's Day Card")
screen = pygame.display.set_mode((800, 800))
font = pygame.font.Font('freesansbold.ttf', 32)
img = pygame.image.load("sigma caca.png")

class Heart:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self, surface):
        left_circle_center = (self.x - 20, self.y)
        right_circle_center = (self.x + 20, self.y)
        triangle_points = [(self.x - 40, self.y + 5),
                           (self.x + 40, self.y + 5),
                           (self.x, self.y + 50)]
        
        pygame.draw.circle(surface, self.color, left_circle_center, 20)
        pygame.draw.circle(surface, self.color, right_circle_center, 20)
        pygame.draw.polygon(surface, self.color, triangle_points)
        
class Flower:
    def __init__(self, x, y, petal_color, center_color):
        self.x = x
        self.y = y
        self.petal_color = petal_color
        self.center_color = center_color

    def draw(self, surface):
        petal_radius = 30
        pygame.draw.circle(surface, self.petal_color, (self.x - 40, self.y), petal_radius)
        pygame.draw.circle(surface, self.petal_color, (self.x + 40, self.y), petal_radius)  
        pygame.draw.circle(surface, self.petal_color, (self.x, self.y - 40), petal_radius)
        pygame.draw.circle(surface, self.petal_color, (self.x, self.y + 40), petal_radius)

        
        pygame.draw.circle(surface, self.center_color, (self.x, self.y), petal_radius // 2)

       
        pygame.draw.line(surface, (0, 255, 0), (self.x, self.y + 40), (self.x, self.y + 100), 5)

flower1 = Flower(100, 500, (255, 0, 0), (255, 255, 0))
flower2 = Flower(300, 500, (0, 255, 255), (255, 0, 255))
flower3 = Flower(500, 500, (255, 0, 0), (255, 255, 0))
flower4 = Flower(700, 500, (0, 255, 255), (255, 0, 255))

        

# Create instances of Heart
heart1 = Heart(100, 200, (250, 0, 0))
heart2 = Heart(300, 200, (250, 0, 0))
heart3 = Heart(500, 200, (250, 0, 0))
heart4 = Heart(700, 200, (250, 0, 0))
heart5 = Heart(200, 300, (250, 0, 0))
heart6 = Heart(400, 300, (250, 0, 0))
heart7 = Heart(600, 300, (250, 0, 0))

# Draw everything
heart1.draw(screen)
heart2.draw(screen)
heart3.draw(screen)
heart4.draw(screen)
heart5.draw(screen)
heart6.draw(screen)
heart7.draw(screen)
flower1.draw(screen)
flower2.draw(screen)
flower3.draw(screen)
flower4.draw(screen)

text1 = font.render('I Love You!', True, (250, 100, 100))
text2 = font.render('Happy Valentines Day', True, (250, 0, 0), (200, 150, 150))
screen.blit(text1, (200, 100))
screen.blit(text2, (400, 300))
screen.blit(img, (0, 600))

pygame.display.flip()
pygame.time.wait(5000)
