import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the window
size = (1400, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Animation Example")

# Parameters for Animation buttons
button_width = 100
button_height = 30
button_color = (255, 0, 0)
button_LSA_1_pos = (20, 20)

# Router and Switch
box_size = 80
switch_size = 50
padding = 20
border_width = 5
box_pos = (padding, padding)
router_radius = 30

# POsition of Area 1 routers
router_1_pos = (195, 250)
router_2_pos = (355, 375)
router_3_pos = (350, 510)
router_4_pos = (65, 375)

# Position of Area 1 Swicthes
switch_1_pos = (170, 350)
switch_2_pos = (40, 485)

# Position of all the area boundaries
area_1_pos = (20, 200)
area_2_pos = (550, 100) # backbone area
area_3_pos = (1010, 100) # area 3
area_4_pos = (1010, 420) # area 4

# Position of all Area 2 Routers (There would be 3 routers (I am thinking))
router_5_pos = (610, 150)
router_6_pos = (610, 290)
router_7_pos = (610,430)
router_8_pos = (740, 290)

# Position of all Area 3 Routers and switches
router_9_pos = (1070, 150)
router_10_pos = (1070, 300)
router_11_pos = (1270, 150)

switch_3_pos = (1245, 275)

# Position of all Area 4 Routers and switches
router_12_pos = (1070, 600)
router_13_pos = (1070, 470)
router_14_pos = (1200, 600)
router_15_pos = (1200, 470)
router_16_pos = (1320, 600)

switch_4_pos = (1295, 445)

# List of all LSAs here (as of now I am planning to represent it by a triangle)
area_1_LSA_1 = []

screen.fill((255, 255, 255))

def AreaBoundaryDrawer():
    # Making Area 1 boundary
    pygame.draw.rect(screen, (231, 230, 240), (area_1_pos[0], area_1_pos[1], box_size * 4.8, box_size * 4.8))

    # Making the backbone area boundary: I will be calling this area 2
    pygame.draw.rect(screen, (231, 240, 230), (area_2_pos[0], area_2_pos[1], box_size * 3, box_size * 4.8))

    # Making a third area: Area 3 
    pygame.draw.rect(screen, (240, 240, 230), (area_3_pos[0], area_3_pos[1], box_size * 4.5, box_size * 3))

    # Making a 4th area: Area 4
    pygame.draw.rect(screen, (240, 230, 238), (area_4_pos[0], area_4_pos[1], box_size * 4.5, box_size * 3))

def RouterSwitchArea1():
    # Mkaing routers for area 1: All routers will be circles
    pygame.draw.circle(screen, (159, 173, 191), (router_1_pos[0], router_1_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_2_pos[0], router_2_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_3_pos[0], router_3_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_4_pos[0], router_4_pos[1]), router_radius)

    # Making the switches for area 1: Rectangles
    pygame.draw.rect(screen, (222, 146, 146), (switch_1_pos[0], switch_1_pos[1], switch_size, switch_size))
    pygame.draw.rect(screen, (222, 146, 146), (switch_2_pos[0], switch_2_pos[1], switch_size, switch_size))

    # Render text to display inside each box
    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Router 1', True, (0, 0, 0))
    text_2 = font.render('Router 2', True, (0, 0, 0))
    text_3 = font.render('Router 3', True, (0, 0, 0))
    text_4 = font.render('Router 4', True, (0, 0, 0))
    text_5 = font.render('Switch 1', True, (0, 0, 0))
    text_6 = font.render('Switch 2', True, (0, 0, 0))

    # Calculate the position to display the text in the center of each box
    text_pos = ((box_size - font.size('Router 1')[0]) // 2, (box_size - font.size('Router 1')[1]) // 2)
    text_pos_switch = ((switch_size - font.size('Switch 1')[0]) // 2, (switch_size - font.size('Switch 1')[1]) // 2)

    screen.blit(text_1, text_1.get_rect(center=router_1_pos))
    screen.blit(text_2, text_1.get_rect(center=router_2_pos))
    screen.blit(text_3, text_1.get_rect(center=router_3_pos))
    screen.blit(text_4, text_1.get_rect(center=router_4_pos))

    # Display the text inside each box
    screen.blit(text_5, (switch_1_pos[0] + text_pos_switch[0], switch_1_pos[1] + text_pos_switch[1]))
    screen.blit(text_6, (switch_2_pos[0] + text_pos_switch[0], switch_2_pos[1] + text_pos_switch[1]))

def Area1Connections():
    # switch 1 --> router 1
    center_box = (switch_1_pos[0] + switch_size // 2, switch_1_pos[1])
    # finding the closest point
    x = center_box[0] - router_1_pos[0]
    y = center_box[1] - router_1_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_1_pos[0] + router_radius * math.cos(a)), int(router_1_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # switch 1 --> router 4
    center_box = (switch_1_pos[0], switch_1_pos[1] + switch_size // 2)
    x = center_box[0] - router_4_pos[0]
    y = center_box[1] - router_4_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_4_pos[0] + router_radius * math.cos(a)), int(router_4_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # router 4 --> switch 2
    center_box = (switch_2_pos[0] + switch_size // 2, switch_2_pos[1])
    x = center_box[0] - router_4_pos[0]
    y = center_box[1] - router_4_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_4_pos[0] + router_radius * math.cos(a)), int(router_4_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)


    # switch 2 --> router 3
    center_box = (switch_2_pos[0] + switch_size, switch_2_pos[1] + switch_size // 2)
    x = center_box[0] - router_3_pos[0]
    y = center_box[1] - router_3_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_3_pos[0] + router_radius * math.cos(a)), int(router_3_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # switch 1 --> router 2
    center_box = (switch_1_pos[0] + switch_size, switch_1_pos[1] + switch_size // 2)
    x = center_box[0] - router_2_pos[0]
    y = center_box[1] - router_2_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_2_pos[0] + router_radius * math.cos(a)), int(router_2_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

def RouterSwitchArea2():
    pygame.draw.circle(screen, (159, 173, 191), (router_5_pos[0], router_5_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_6_pos[0], router_6_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_7_pos[0], router_7_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_8_pos[0], router_8_pos[1]), router_radius)

     # Render text to display inside each box
    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Router 5', True, (0, 0, 0))
    text_2 = font.render('Router 6', True, (0, 0, 0))
    text_3 = font.render('Router 7', True, (0, 0, 0))
    text_4 = font.render('Router 8', True, (0, 0, 0))

    # Calculate the position to display the text in the center of each box
    text_pos = ((box_size - font.size('Router 1')[0]) // 2, (box_size - font.size('Router 1')[1]) // 2)

    screen.blit(text_1, text_1.get_rect(center=router_5_pos))
    screen.blit(text_2, text_2.get_rect(center=router_6_pos))
    screen.blit(text_3, text_3.get_rect(center=router_7_pos))
    screen.blit(text_4, text_4.get_rect(center=router_8_pos))

def Area2Connections():
    # router 5 --> router 6
    center_box = (router_5_pos[0], router_5_pos[1] + router_radius)
    x = center_box[0] - router_6_pos[0]
    y = center_box[1] - router_6_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_6_pos[0] + router_radius * math.cos(a)), int(router_6_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # router 6 --> router 7
    center_box = (router_6_pos[0], router_6_pos[1] + router_radius)
    x = center_box[0] - router_7_pos[0]
    y = center_box[1] - router_7_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_7_pos[0] + router_radius * math.cos(a)), int(router_7_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # router 5 --> router 8
    center_box = (router_5_pos[0] + router_radius, router_5_pos[1])
    x = center_box[0] - router_8_pos[0]
    y = center_box[1] - router_8_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_8_pos[0] + router_radius * math.cos(a)), int(router_8_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # router 7 --> router 8
    center_box = (router_7_pos[0] + router_radius, router_7_pos[1])
    x = center_box[0] - router_8_pos[0]
    y = center_box[1] - router_8_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_8_pos[0] + router_radius * math.cos(a)), int(router_8_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

def RouterSwitchArea3():
    pygame.draw.circle(screen, (159, 173, 191), (router_9_pos[0], router_9_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_10_pos[0], router_10_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_11_pos[0], router_11_pos[1]), router_radius)

    pygame.draw.rect(screen, (222, 146, 146), (switch_3_pos[0], switch_3_pos[1], switch_size, switch_size))
    
     # Render text to display inside each box
    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Router 9', True, (0, 0, 0))
    text_2 = font.render('Router 10', True, (0, 0, 0))
    text_3 = font.render('Router 11', True, (0, 0, 0))
    text_4 = font.render('Switch 3', True, (0, 0, 0))

    # Calculate the position to display the text in the center of each box
    text_pos = ((box_size - font.size('Router 1')[0]) // 2, (box_size - font.size('Router 1')[1]) // 2)

    text_pos_switch = ((switch_size - font.size('Switch 3')[0]) // 2, (switch_size - font.size('Switch 3')[1]) // 2)

    screen.blit(text_1, text_1.get_rect(center=router_9_pos))
    screen.blit(text_2, text_2.get_rect(center=router_10_pos))
    screen.blit(text_3, text_3.get_rect(center=router_11_pos))
    screen.blit(text_4, (switch_3_pos[0] + text_pos_switch[0], switch_3_pos[1] + text_pos_switch[1]))

def Area3Connections():
    # Router 9 --> Router 11
    center_box = (router_9_pos[0] + router_radius, router_9_pos[1])
    x = center_box[0] - router_11_pos[0]
    y = center_box[1] - router_11_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_11_pos[0] + router_radius * math.cos(a)), int(router_11_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 11 --> Switch 3
    center_box = (switch_3_pos[0] + switch_size // 2, switch_3_pos[1])
    x = center_box[0] - router_11_pos[0]
    y = center_box[1] - router_11_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_11_pos[0] + router_radius * math.cos(a)), int(router_11_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Switch 3 --> Router 10
    center_box = (switch_3_pos[0], switch_3_pos[1]  + switch_size // 2)
    x = center_box[0] - router_10_pos[0]
    y = center_box[1] - router_10_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_10_pos[0] + router_radius * math.cos(a)), int(router_10_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

def RouterSwitchArea4():
    pygame.draw.circle(screen, (159, 173, 191), (router_12_pos[0], router_12_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_13_pos[0], router_13_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_14_pos[0], router_14_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_15_pos[0], router_15_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_16_pos[0], router_16_pos[1]), router_radius)

    pygame.draw.rect(screen, (222, 146, 146), (switch_4_pos[0], switch_4_pos[1], switch_size, switch_size))
    
     # Render text to display inside each box
    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Router 12', True, (0, 0, 0))
    text_2 = font.render('Router 13', True, (0, 0, 0))
    text_3 = font.render('Router 14', True, (0, 0, 0))
    text_4 = font.render('Router 15', True, (0, 0, 0))
    text_5 = font.render('Router 16', True, (0, 0, 0))
    text_6 = font.render('Switch 4', True, (0, 0, 0))

    # Calculate the position to display the text in the center of each box
    text_pos = ((box_size - font.size('Router 12')[0]) // 2, (box_size - font.size('Router 12')[1]) // 2)

    text_pos_switch = ((switch_size - font.size('Switch 4')[0]) // 2, (switch_size - font.size('Switch 4')[1]) // 2)

    screen.blit(text_1, text_1.get_rect(center=router_12_pos))
    screen.blit(text_2, text_2.get_rect(center=router_13_pos))
    screen.blit(text_3, text_3.get_rect(center=router_14_pos))
    screen.blit(text_4, text_4.get_rect(center=router_15_pos))
    screen.blit(text_5, text_5.get_rect(center=router_16_pos))
    screen.blit(text_6, (switch_4_pos[0] + text_pos_switch[0], switch_4_pos[1] + text_pos_switch[1]))

def Area4Connections():
    # Router 13 --> Router 12
    center_box = (router_13_pos[0], router_13_pos[1] + router_radius)
    x = center_box[0] - router_12_pos[0]
    y = center_box[1] - router_12_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_12_pos[0] + router_radius * math.cos(a)), int(router_12_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 13 --> Router 15
    center_box = (router_13_pos[0] + router_radius, router_13_pos[1])
    x = center_box[0] - router_15_pos[0]
    y = center_box[1] - router_15_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_15_pos[0] + router_radius * math.cos(a)), int(router_15_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 12 --> Router 14
    center_box = (router_12_pos[0] + router_radius, router_12_pos[1])
    x = center_box[0] - router_14_pos[0]
    y = center_box[1] - router_14_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_14_pos[0] + router_radius * math.cos(a)), int(router_14_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 14 --> Router 15
    center_box = (router_14_pos[0], router_14_pos[1] - router_radius)
    x = center_box[0] - router_15_pos[0]
    y = center_box[1] - router_15_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_15_pos[0] + router_radius * math.cos(a)), int(router_15_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 15 --> Switch 4
    center_box = (switch_4_pos[0], switch_4_pos[1] + switch_size // 2)
    x = center_box[0] - router_15_pos[0]
    y = center_box[1] - router_15_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_15_pos[0] + router_radius * math.cos(a)), int(router_15_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Switch 4 --> Router 16
    center_box = (switch_4_pos[0] + switch_size // 2, switch_4_pos[1] + switch_size)
    x = center_box[0] - router_16_pos[0]
    y = center_box[1] - router_16_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_16_pos[0] + router_radius * math.cos(a)), int(router_16_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

def InterAreaConnections():
    # Router 2 (Area 1) --> Router 5 (Area 2)
    center_box = (router_5_pos[0] - router_radius, router_5_pos[1])
    x = center_box[0] - router_2_pos[0]
    y = center_box[1] - router_2_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_2_pos[0] + router_radius * math.cos(a)), int(router_2_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 9 (Area 3) --> Router 8 (Area 2)
    center_box = (router_8_pos[0] + router_radius, router_8_pos[1])
    x = center_box[0] - router_9_pos[0]
    y = center_box[1] - router_9_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_9_pos[0] + router_radius * math.cos(a)), int(router_9_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 8 (Area 2) --> Router 13 (Area 4)
    center_box = (router_8_pos[0] + router_radius, router_8_pos[1])
    x = center_box[0] - router_13_pos[0]
    y = center_box[1] - router_13_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_13_pos[0] + router_radius * math.cos(a)), int(router_13_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

def AddAnimationButtons():
    # Button for sending LSA 1s
    pygame.draw.rect(screen, (31, 128, 48), (button_LSA_1_pos[0], button_LSA_1_pos[1], button_width, button_height))

    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Send LSA 1', True, (0, 0, 0))
    text_pos_switch = ((button_width - font.size('Send LSA 1')[0]) // 2, (button_height - font.size('Send LSA 1')[1]) // 2)
    screen.blit(text_1, (button_LSA_1_pos[0] + text_pos_switch[0], button_LSA_1_pos[1] + text_pos_switch[1]))

def Send_LSA_1():
    pass

# Making the boundaries
AreaBoundaryDrawer()

# Doing all Area 1 Work
RouterSwitchArea1()
Area1Connections()

# Doing all Area 2 Work
RouterSwitchArea2()
Area2Connections()

# Doing All Area 3 Work
RouterSwitchArea3()
Area3Connections()

# Doing All Area 4 work
RouterSwitchArea4()
Area4Connections()

# Making connections between different areas
InterAreaConnections()

# Adding the animation buttons
AddAnimationButtons()

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

