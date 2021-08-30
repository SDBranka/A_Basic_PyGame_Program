#Import and initialize Pygame library
import pygame
pygame.init()

#set up your display window
screen = pygame.display.set_mode((500,500))

#set up a game loop
running = True

while running:
    # did user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the screen with white
    white_for_screenfill = (255,255,255)
    screen.fill(white_for_screenfill)

    # draw a solid blue circle
    blue_for_circle = (0,0,255)
    location_of_circle_center = (250,250)
    pygame.draw.circle(screen, blue_for_circle, location_of_circle_center, 75)

    #flip the display
    pygame.display.flip()

#exit pygame
pygame.quit()