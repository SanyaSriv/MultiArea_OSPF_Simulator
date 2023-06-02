import pygame
import math
import global_variables_file
from global_variables_file import *
import Area_1_LSA
import Area_2_LSA
import LSA_Class
# Initialize Pygame
pygame.init()

# Set up the window

screen = pygame.display.set_mode(size)
pygame.display.set_caption("OSPF Simulator")
clock = pygame.time.Clock()

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
    pygame.draw.circle(screen, (159, 173, 191), (router_5_pos_area_1[0], router_5_pos_area_1[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_6_pos_area_1[0], router_6_pos_area_1[1]), router_radius)

    # Render text to display inside each box
    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Router 1', True, (0, 0, 0))
    text_2 = font.render('Router 2', True, (0, 0, 0))
    text_3 = font.render('Router 3', True, (0, 0, 0))
    text_4 = font.render('Router 4', True, (0, 0, 0))
    text_5 = font.render('Router 5', True, (0, 0, 0))
    text_6 = font.render('Router 6', True, (0, 0, 0))

    # Calculate the position to display the text in the center of each box
    text_pos = ((box_size - font.size('Router 1')[0]) // 2, (box_size - font.size('Router 1')[1]) // 2)

    screen.blit(text_1, text_1.get_rect(center=router_1_pos))
    screen.blit(text_2, text_1.get_rect(center=router_2_pos))
    screen.blit(text_3, text_1.get_rect(center=router_3_pos))
    screen.blit(text_4, text_1.get_rect(center=router_4_pos))
    screen.blit(text_5, text_1.get_rect(center=router_5_pos_area_1))
    screen.blit(text_6, text_1.get_rect(center=router_6_pos_area_1))

def Area1Connections():
    global triangle_pos
    # router 5 area 1 --> router 1
    center_box = (router_5_pos_area_1[0], router_5_pos_area_1[1] - router_radius)
    # finding the closest point
    x = center_box[0] - router_1_pos[0]
    y = center_box[1] - router_1_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_1_pos[0] + router_radius * math.cos(a)), int(router_1_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    # making the travel route for this
    area_1_travel_routes["router_5_area_1__TO__router_1"] = [closest_point, center_box]

    # router 5 area 1 --> router 4
    center_box = (router_5_pos_area_1[0] - router_radius, router_5_pos_area_1[1])
    x = center_box[0] - router_4_pos[0]
    y = center_box[1] - router_4_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_4_pos[0] + router_radius * math.cos(a)), int(router_4_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    # making the travel route for this
    area_1_travel_routes["router_5_area_1__TO__router_4"] = [closest_point, center_box]

    # router 4 --> router 3
    center_box = (router_4_pos[0], router_4_pos[1] + router_radius)
    x = center_box[0] - router_3_pos[0]
    y = center_box[1] - router_3_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_3_pos[0] + router_radius * math.cos(a)), int(router_3_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    # making the travel route for this
    area_1_travel_routes["router_4__TO__router_3"] = [closest_point, center_box]

    # router 5 area 1 --> router 2
    center_box = (router_5_pos_area_1[0] + router_radius, router_5_pos_area_1[1])
    x = center_box[0] - router_2_pos[0]
    y = center_box[1] - router_2_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_2_pos[0] + router_radius * math.cos(a)), int(router_2_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    # making the travel route for this
    area_1_travel_routes["router_5_area_1__TO__router_2"] = [closest_point, center_box]

    # router 2 --> router 6
    center_box = (router_6_pos_area_1[0], router_6_pos_area_1[1]  - router_radius)
    x = center_box[0] - router_2_pos[0]
    y = center_box[1] - router_2_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_2_pos[0] + router_radius * math.cos(a)), int(router_2_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    # making the travel route for this
    area_1_travel_routes["router_2__TO__router_6"] = [closest_point, center_box]


def RouterSwitchArea2():
    pygame.draw.circle(screen, (159, 173, 191), (router_7_pos[0], router_7_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_8_pos[0], router_8_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_9_pos[0], router_9_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_10_pos[0], router_10_pos[1]), router_radius)

     # Render text to display inside each box
    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Router 7', True, (0, 0, 0))
    text_2 = font.render('Router 8', True, (0, 0, 0))
    text_3 = font.render('Router 9', True, (0, 0, 0))
    text_4 = font.render('Router 10', True, (0, 0, 0))

    # Calculate the position to display the text in the center of each box
    text_pos = ((box_size - font.size('Router 1')[0]) // 2, (box_size - font.size('Router 1')[1]) // 2)

    screen.blit(text_1, text_1.get_rect(center=router_7_pos))
    screen.blit(text_2, text_2.get_rect(center=router_8_pos))
    screen.blit(text_3, text_3.get_rect(center=router_9_pos))
    screen.blit(text_4, text_4.get_rect(center=router_10_pos))

def Area2Connections():
    # router 7 --> router 8
    center_box = (router_7_pos[0], router_7_pos[1] + router_radius)
    x = center_box[0] - router_8_pos[0]
    y = center_box[1] - router_8_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_8_pos[0] + router_radius * math.cos(a)), int(router_8_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    area_2_travel_routes["router_7__TO__router_8"] = [center_box, closest_point]
    
    # router 8 --> router 9
    center_box = (router_8_pos[0], router_8_pos[1] + router_radius)
    x = center_box[0] - router_9_pos[0]
    y = center_box[1] - router_9_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_9_pos[0] + router_radius * math.cos(a)), int(router_9_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    area_2_travel_routes["router_8__TO__router_9"] = [center_box, closest_point]
    
    # router 7 --> router 10
    center_box = (router_7_pos[0] + router_radius, router_7_pos[1])
    x = center_box[0] - router_10_pos[0]
    y = center_box[1] - router_10_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_10_pos[0] + router_radius * math.cos(a)), int(router_10_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    area_2_travel_routes["router_7__TO__router_10"] = [center_box, closest_point]

    # router 9 --> router 10
    center_box = (router_9_pos[0] + router_radius, router_9_pos[1])
    x = center_box[0] - router_10_pos[0]
    y = center_box[1] - router_10_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_10_pos[0] + router_radius * math.cos(a)), int(router_10_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    area_2_travel_routes["router_9__TO__router_10"] = [center_box, closest_point]

def RouterSwitchArea3():
    # 9, 10, 11 --> 11, 12, 13
    pygame.draw.circle(screen, (159, 173, 191), (router_11_pos[0], router_11_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_12_pos[0], router_12_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_13_pos[0], router_13_pos[1]), router_radius)

    pygame.draw.rect(screen, (222, 146, 146), (switch_3_pos[0], switch_3_pos[1], switch_size, switch_size))
    
     # Render text to display inside each box
    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Router 11', True, (0, 0, 0))
    text_2 = font.render('Router 12', True, (0, 0, 0))
    text_3 = font.render('Router 13', True, (0, 0, 0))
    text_4 = font.render('Switch 3', True, (0, 0, 0))

    # Calculate the position to display the text in the center of each box
    text_pos = ((box_size - font.size('Router 1')[0]) // 2, (box_size - font.size('Router 1')[1]) // 2)

    text_pos_switch = ((switch_size - font.size('Switch 3')[0]) // 2, (switch_size - font.size('Switch 3')[1]) // 2)

    screen.blit(text_1, text_1.get_rect(center=router_11_pos))
    screen.blit(text_2, text_2.get_rect(center=router_12_pos))
    screen.blit(text_3, text_3.get_rect(center=router_13_pos))
    screen.blit(text_4, (switch_3_pos[0] + text_pos_switch[0], switch_3_pos[1] + text_pos_switch[1]))

def Area3Connections():
    # Router 11 --> Router 13
    center_box = (router_11_pos[0] + router_radius, router_11_pos[1])
    x = center_box[0] - router_13_pos[0]
    y = center_box[1] - router_13_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_13_pos[0] + router_radius * math.cos(a)), int(router_13_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 13 --> Switch 3
    center_box = (switch_3_pos[0] + switch_size // 2, switch_3_pos[1])
    x = center_box[0] - router_13_pos[0]
    y = center_box[1] - router_13_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_13_pos[0] + router_radius * math.cos(a)), int(router_13_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Switch 3 --> Router 12
    center_box = (switch_3_pos[0], switch_3_pos[1]  + switch_size // 2)
    x = center_box[0] - router_12_pos[0]
    y = center_box[1] - router_12_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_12_pos[0] + router_radius * math.cos(a)), int(router_12_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

def RouterSwitchArea4():
    # 12, 13, 14, 15, 16 --> 14, 15, 16, 17, 18
    pygame.draw.circle(screen, (159, 173, 191), (router_14_pos[0], router_14_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_15_pos[0], router_15_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_16_pos[0], router_16_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_17_pos[0], router_17_pos[1]), router_radius)
    pygame.draw.circle(screen, (159, 173, 191), (router_18_pos[0], router_18_pos[1]), router_radius)

    pygame.draw.rect(screen, (222, 146, 146), (switch_4_pos[0], switch_4_pos[1], switch_size, switch_size))
    
     # Render text to display inside each box
    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Router 14', True, (0, 0, 0))
    text_2 = font.render('Router 15', True, (0, 0, 0))
    text_3 = font.render('Router 16', True, (0, 0, 0))
    text_4 = font.render('Router 17', True, (0, 0, 0))
    text_5 = font.render('Router 18', True, (0, 0, 0))
    text_6 = font.render('Switch 4', True, (0, 0, 0))

    # Calculate the position to display the text in the center of each box
    text_pos = ((box_size - font.size('Router 12')[0]) // 2, (box_size - font.size('Router 12')[1]) // 2)

    text_pos_switch = ((switch_size - font.size('Switch 4')[0]) // 2, (switch_size - font.size('Switch 4')[1]) // 2)

    screen.blit(text_1, text_1.get_rect(center=router_14_pos))
    screen.blit(text_2, text_2.get_rect(center=router_15_pos))
    screen.blit(text_3, text_3.get_rect(center=router_16_pos))
    screen.blit(text_4, text_4.get_rect(center=router_17_pos))
    screen.blit(text_5, text_5.get_rect(center=router_18_pos))
    screen.blit(text_6, (switch_4_pos[0] + text_pos_switch[0], switch_4_pos[1] + text_pos_switch[1]))

def Area4Connections():
    # Router 15 --> Router 14
    center_box = (router_15_pos[0], router_15_pos[1] + router_radius)
    x = center_box[0] - router_14_pos[0]
    y = center_box[1] - router_14_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_14_pos[0] + router_radius * math.cos(a)), int(router_14_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 15 --> Router 17
    center_box = (router_15_pos[0] + router_radius, router_15_pos[1])
    x = center_box[0] - router_17_pos[0]
    y = center_box[1] - router_17_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_17_pos[0] + router_radius * math.cos(a)), int(router_17_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 14 --> Router 16
    center_box = (router_14_pos[0] + router_radius, router_14_pos[1])
    x = center_box[0] - router_16_pos[0]
    y = center_box[1] - router_16_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_16_pos[0] + router_radius * math.cos(a)), int(router_16_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 17 --> Router 16
    center_box = (router_16_pos[0], router_16_pos[1] - router_radius)
    x = center_box[0] - router_17_pos[0]
    y = center_box[1] - router_17_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_17_pos[0] + router_radius * math.cos(a)), int(router_17_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # TODO: FIX THIS 
    # # Router 15 --> Switch 4
    # center_box = (switch_4_pos[0], switch_4_pos[1] + switch_size // 2)
    # x = center_box[0] - router_15_pos[0]
    # y = center_box[1] - router_15_pos[1]
    # a = math.atan2(y, x)
    # closest_point = (int(router_15_pos[0] + router_radius * math.cos(a)), int(router_15_pos[1] + router_radius * math.sin(a)))
    # pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # # Switch 4 --> Router 16
    # center_box = (switch_4_pos[0] + switch_size // 2, switch_4_pos[1] + switch_size)
    # x = center_box[0] - router_16_pos[0]
    # y = center_box[1] - router_16_pos[1]
    # a = math.atan2(y, x)
    # closest_point = (int(router_16_pos[0] + router_radius * math.cos(a)), int(router_16_pos[1] + router_radius * math.sin(a)))
    # pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

def InterAreaConnections():
    # Router 2 (Area 1) --> Router 7 (Area 2)
    center_box = (router_7_pos[0] - router_radius, router_7_pos[1])
    x = center_box[0] - router_2_pos[0]
    y = center_box[1] - router_2_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_2_pos[0] + router_radius * math.cos(a)), int(router_2_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # TODO: FIX THIS 
    # # Router 9 (Area 3) --> Switch 5 (Area 2)
    # center_box = (switch_5_pos[0] + switch_size // 2, switch_5_pos[1])
    # x = center_box[0] - router_9_pos[0]
    # y = center_box[1] - router_9_pos[1]
    # a = math.atan2(y, x)
    # closest_point = (int(router_9_pos[0] + router_radius * math.cos(a)), int(router_9_pos[1] + router_radius * math.sin(a)))
    # pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # # Router 13 (Area 4) --> Switch 5 (Area 2)
    # center_box = (switch_5_pos[0] + switch_size // 2, switch_5_pos[1] + switch_size)
    # x = center_box[0] - router_13_pos[0]
    # y = center_box[1] - router_13_pos[1]
    # a = math.atan2(y, x)
    # closest_point = (int(router_13_pos[0] + router_radius * math.cos(a)), int(router_13_pos[1] + router_radius * math.sin(a)))
    # pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)


def AddAnimationButtons():
    # Button for sending LSA 1s
    pygame.draw.rect(screen, (31, 128, 48), (button_LSA_1_pos[0], button_LSA_1_pos[1], button_width, button_height))
    pygame.draw.rect(screen, (31, 128, 48), (button_LSA_1_refresh[0], button_LSA_1_refresh[1], button_width, button_height))
    font = pygame.font.SysFont('Arial', 12)

    text_1 = font.render('Send LSA 1', True, (0, 0, 0))
    text_2 = font.render('Clear LSA1 text', True, (0, 0, 0))

    text_pos_switch = ((button_width - font.size('Send LSA 1')[0]) // 2, (button_height - font.size('Send LSA 1')[1]) // 2)
    screen.blit(text_1, (button_LSA_1_pos[0] + text_pos_switch[0], button_LSA_1_pos[1] + text_pos_switch[1]))

    text_pos_switch = ((button_width - font.size('Clear LSA1 text')[0]) // 2, (button_height - font.size('Clear LSA1 text')[1]) // 2)
    screen.blit(text_2, (button_LSA_1_refresh[0] + text_pos_switch[0], button_LSA_1_refresh[1] + text_pos_switch[1]))

    # making the slider here
    pygame.draw.rect(screen, (0,0,0), (slider_position[0], slider_position[1], slider_width, slider_height))
    slider_handle_x = slider_position[0] + 1 + (speed_slider_current_value - speed_slider_min_value) / (speed_slider_max_value - speed_slider_min_value) * slider_width
    pygame.draw.rect(screen, (230, 120, 89), (slider_handle_x, slider_position[1], slider_handle_width, slider_height))

# Adding the animation buttons


# Update the screen
pygame.display.flip()

# # Set up the clock
# clock = pygame.time.Clock()

# Run the game loop
running = True
res = 0
speed_slider_dragging = 0

while running:
    screen.fill((255,255,255))
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            mouse_pos = pygame.mouse.get_pos()
            if slider_position[0] <= mouse_pos[0] <= slider_position[0] + slider_width and slider_position[1] <= mouse_pos[1] <= slider_position[1] + slider_height:
                speed_slider_dragging = True
            
            # if the SEND_LSA_1 button gets clicked
            if (button_LSA_1_pos[0] < mouse_pos[0] < button_LSA_1_pos[0] + button_width) and \
               (button_LSA_1_pos[1] < mouse_pos[1] < button_LSA_1_pos[1] + button_height):
                # global_variables_file.triangle_pos = area_1_travel_routes["router_5_area_1__TO__router_1"][0]
                # global_variables_file.triangle_target = area_1_travel_routes["router_5_area_1__TO__router_1"][1]
                if res != 1:
                    Area_1_LSA.initialize_Area1_LSA()
                    Area_2_LSA.initialize_Area2_LSA()
                    res = 1
            
            if (button_LSA_1_refresh[0] < mouse_pos[0] < button_LSA_1_refresh[0] + button_width) and \
               (button_LSA_1_refresh[1] < mouse_pos[1] < button_LSA_1_refresh[1] + button_height):
                # TODO: If we set res = 0 in here, then the text dissapears but the LSA 1 sending process stops
                # to not stop the process while clearing the text, set res = 0 by some other button
                res = 0
                Area_1_LSA.erase_text()
                Area_2_LSA.erase_text()

    # elif event.type == pygame.MOUSEBUTTONUP:
    #     if event.button == 1:  # Left mouse button
    #         speed_slider_dragging = False
    #         LSA_Class.LSATriangles.shared_speed = int(speed_slider_current_value / 50)

    # elif event.type == pygame.MOUSEMOTION:
    #     if speed_slider_dragging == True:
    #         mouse_pos = pygame.mouse.get_pos()
    #         normalized_x = (mouse_pos[0] - slider_position[0]) / slider_width
    #         current_value = speed_slider_min_value + int(normalized_x * (speed_slider_max_value - speed_slider_min_value))
    #         speed_slider_current_value = max(speed_slider_min_value, min(current_value, speed_slider_max_value))

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
    AddAnimationButtons()
    if res == 1:
        Area_1_LSA.SendArea1LSA1(pygame, screen)
        Area_2_LSA.SendArea2LSA1(pygame, screen)
        # figure out some way to put res as 0
        
    # Update the screen
    pygame.display.flip()
    clock.tick(10)

# Clean up
pygame.quit()

