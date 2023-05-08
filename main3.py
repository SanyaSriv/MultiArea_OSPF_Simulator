import pygame

# Initialize Pygame
pygame.init()

# Set up the window
size = (1400, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Animation Example")

# Set up the variables for the animation
box_size = 80
padding = 20
border_width = 5
box_pos = (padding, padding)

# Draw the four routers
box_1_pos = (40, 270)
box_2_pos = (305, 270)
box_3_pos = (305, 450)
box_4_pos = (40, 450)
switch_1_pos = (170, 350)
area_1_pos = (20, 200)

screen.fill((255, 255, 255))
# I want to demarcate what is area 1 by a boundary
pygame.draw.rect(screen, (231, 230, 240), (area_1_pos[0], area_1_pos[1], box_size * 4.8, box_size * 4.8))

pygame.draw.rect(screen, (194, 206, 207), (box_1_pos[0], box_1_pos[1], box_size, box_size))
pygame.draw.rect(screen, (194, 206, 207), (box_2_pos[0], box_2_pos[1], box_size, box_size))
pygame.draw.rect(screen, (194, 206, 207), (box_3_pos[0], box_3_pos[1], box_size, box_size))
pygame.draw.rect(screen, (194, 206, 207), (box_4_pos[0], box_4_pos[1], box_size, box_size))
pygame.draw.rect(screen, (163, 122, 113), (switch_1_pos[0], switch_1_pos[1], box_size, box_size))
# Render text to display inside each box
font = pygame.font.SysFont('Arial', 14)
text_1 = font.render('Router 1', True, (0, 0, 0))
text_2 = font.render('Router 2', True, (0, 0, 0))
text_3 = font.render('Router 3', True, (0, 0, 0))
text_4 = font.render('Router 4', True, (0, 0, 0))
text_5 = font.render('Switch 1', True, (0, 0, 0))

# Calculate the position to display the text in the center of each box
text_pos = ((box_size - font.size('Router 1')[0]) // 2, (box_size - font.size('Router 1')[1]) // 2)

# Display the text inside each box
screen.blit(text_1, (box_1_pos[0] + text_pos[0], box_1_pos[1] + text_pos[1]))
screen.blit(text_2, (box_2_pos[0] + text_pos[0], box_2_pos[1] + text_pos[1]))
screen.blit(text_3, (box_3_pos[0] + text_pos[0], box_3_pos[1] + text_pos[1]))
screen.blit(text_4, (box_4_pos[0] + text_pos[0], box_4_pos[1] + text_pos[1]))
screen.blit(text_5, (switch_1_pos[0] + text_pos[0], switch_1_pos[1] + text_pos[1]))

# trying to connect the routers here
line_width = 3
line_color = (0, 0, 0)
pygame.draw.line(screen, line_color, (box_1_pos[0] + box_size, box_1_pos[1] + box_size // 2), 
                 (box_2_pos[0], box_2_pos[1] + box_size // 2), line_width)

# Update the screen
pygame.display.flip()

# Set up the clock
clock = pygame.time.Clock()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

    # Wait for a short amount of time to control the animation speed
    clock.tick(60)

# Clean up
pygame.quit()

