import pygame

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Skull")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

while(True):

    screen.fill((50, 50, 50))  # Background color

    # Draw skull head (upper part)
    pygame.draw.circle(screen, white, (200, 175), 90)  # Upper skull circle
    
    # Draw skull jaw (lower part)
    pygame.draw.ellipse(screen, white, (150, 250, 100, 50))  # Lower jaw oval

    # Draw eyes (large black circles)
    pygame.draw.circle(screen, black, (170, 160), 25)
    pygame.draw.circle(screen, black, (240, 160), 25)

    pygame.draw.circle(screen, white, (200, 150), 25)

  

    # Draw nose (upside-down triangle)
    pygame.draw.polygon(screen, black, [(230,250), (200,200), (175, 250)])

    #teeth!
    for i in range(2):
        for j in range(5):
            pygame.draw.rect(screen, black, (180+j*10, 265+i*10, 5, 8))

    
    # Update display
    pygame.display.flip()


pygame.quit()
