import pygame
import math
import global_variables_file
from global_variables_file import *
import Area_1_LSA
import Area_2_LSA
import Area_3_LSA
import Area_1_LSA_3
import Area_2_LSA_3
import LSA_Class
import Area_LSA_4

# Initialize Pygame
pygame.init()

# Set up the window
# TODO: Make Area 3 a STUB AREA

screen = pygame.display.set_mode(size)
pygame.display.set_caption("OSPF Simulator")
clock = pygame.time.Clock()

screen.fill((255, 255, 255))

def AreaBoundaryDrawer():
    # Making Area 1 boundary
    pygame.draw.rect(screen, (231, 230, 240), (area_1_pos[0], area_1_pos[1], box_size * 5.4, box_size * 4.8))

    # Making the backbone area boundary: I will be calling this area 2
    pygame.draw.rect(screen, (231, 240, 230), (area_2_pos[0], area_2_pos[1], box_size * 5, box_size * 4.8))

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

    pygame.draw.circle(screen, (159, 173, 191), (router_abr_1[0], router_abr_1[1]), router_radius)

    # Render text to display inside each box
    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Router 1', True, (0, 0, 0))
    text_2 = font.render('Router 2', True, (0, 0, 0))
    text_3 = font.render('Router 3', True, (0, 0, 0))
    text_4 = font.render('Router 4', True, (0, 0, 0))
    text_5 = font.render('Router 5', True, (0, 0, 0))
    text_6 = font.render('Router 6', True, (0, 0, 0))
    text_7 = font.render('ABR 1', True, (0,0,0))
    # Calculate the position to display the text in the center of each box
    text_pos = ((box_size - font.size('Router 1')[0]) // 2, (box_size - font.size('Router 1')[1]) // 2)

    screen.blit(text_1, text_1.get_rect(center=router_1_pos))
    screen.blit(text_2, text_1.get_rect(center=router_2_pos))
    screen.blit(text_3, text_1.get_rect(center=router_3_pos))
    screen.blit(text_4, text_1.get_rect(center=router_4_pos))
    screen.blit(text_5, text_1.get_rect(center=router_5_pos_area_1))
    screen.blit(text_6, text_1.get_rect(center=router_6_pos_area_1))
    screen.blit(text_7, text_1.get_rect(center=router_abr_1))

    font = pygame.font.SysFont('Arial', 25)
    text = font.render("Area 1", True, (0, 0, 0))
    screen.blit(text, (140, 600))

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

    # making the ISP here
    # TODO: Make another function where we can have code related to ASBR
    pygame.draw.circle(screen, (159, 173, 191), (router_isp_pos[0], router_isp_pos[1]), router_radius)
    text_5 = font.render('ISP', True, (0, 0, 0))
    text_pos_1 = ((box_size - font.size('ISP')[0]) // 2, (box_size - font.size('ISP')[1]) // 2)
    screen.blit(text_5, text_5.get_rect(center=router_isp_pos))

    font = pygame.font.SysFont('Arial', 25)
    text = font.render("Area 2 (Backbone Area)", True, (0, 0, 0))
    screen.blit(text, (530, 530))

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
    pygame.draw.circle(screen, (159, 173, 191), (router_14_pos[0], router_14_pos[1]), router_radius)
    
     # Render text to display inside each box
    font = pygame.font.SysFont('Arial', 12)
    text_1 = font.render('Router 11', True, (0, 0, 0))
    text_2 = font.render('Router 12', True, (0, 0, 0))
    text_3 = font.render('Router 13', True, (0, 0, 0))
    text_4 = font.render('Router 14', True, (0, 0, 0))

    # Calculate the position to display the text in the center of each box
    text_pos = ((box_size - font.size('Router 1')[0]) // 2, (box_size - font.size('Router 1')[1]) // 2)

    screen.blit(text_1, text_1.get_rect(center=router_11_pos))
    screen.blit(text_2, text_2.get_rect(center=router_12_pos))
    screen.blit(text_3, text_3.get_rect(center=router_13_pos))
    screen.blit(text_4, text_4.get_rect(center=router_14_pos))

def Area3Connections():
    # Router 11 --> Router 13
    center_box = (router_11_pos[0] + router_radius, router_11_pos[1])
    x = center_box[0] - router_13_pos[0]
    y = center_box[1] - router_13_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_13_pos[0] + router_radius * math.cos(a)), int(router_13_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    area_3_travel_routes["router_11__TO__router_13"] = [center_box, closest_point]

    # Router 13 --> Router 14
    center_box = (router_14_pos[0], router_14_pos[1])
    x = center_box[0] - router_13_pos[0]
    y = center_box[1] - router_13_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_13_pos[0] + router_radius * math.cos(a)), int(router_13_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    area_3_travel_routes["router_13__TO__router_14"] = [closest_point, center_box]

    # Router 14 --> Router 12
    center_box = (router_14_pos[0], router_14_pos[1])
    x = center_box[0] - router_12_pos[0]
    y = center_box[1] - router_12_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_12_pos[0] + router_radius * math.cos(a)), int(router_12_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    area_3_travel_routes["router_14__TO__router_12"] = [center_box, closest_point]

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

    # Router 15 --> Router 17
    center_box = (router_15_pos[0] + router_radius, router_15_pos[1])
    x = center_box[0] - router_17_pos[0]
    y = center_box[1] - router_17_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_17_pos[0] + router_radius * math.cos(a)), int(router_17_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Router 17 --> Router 16
    center_box = (router_16_pos[0], router_16_pos[1] - router_radius)
    x = center_box[0] - router_17_pos[0]
    y = center_box[1] - router_17_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_17_pos[0] + router_radius * math.cos(a)), int(router_17_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # TODO: FIX THIS 
    # Router 17 --> Switch 4
    center_box = (switch_4_pos[0], switch_4_pos[1] + switch_size // 2)
    x = center_box[0] - router_17_pos[0]
    y = center_box[1] - router_17_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_17_pos[0] + router_radius * math.cos(a)), int(router_17_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

    # Switch 4 --> Router 18
    center_box = (switch_4_pos[0] + switch_size // 2, switch_4_pos[1] + switch_size)
    x = center_box[0] - router_18_pos[0]
    y = center_box[1] - router_18_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_18_pos[0] + router_radius * math.cos(a)), int(router_18_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)

def InterAreaConnections():
    
    # Router 2 (Area 1) --> ABR for Area 1 and 2
    center_box = (router_2_pos[0], router_2_pos[1] - router_radius)
    x = center_box[0] - router_abr_1[0]
    y = center_box[1] - router_abr_1[1]
    a = math.atan2(y, x)
    closest_point = (int(router_abr_1[0] + router_radius * math.cos(a)), int(router_abr_1[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    inter_area_routes["router_2__TO__router_abr1"] = [closest_point, center_box]

    # Router 7 (Area 2) --> ABR for Area 1 and 2
    center_box = (router_7_pos[0] - router_radius, router_7_pos[1])
    x = center_box[0] - router_abr_1[0]
    y = center_box[1] - router_abr_1[1]
    a = math.atan2(y, x)
    closest_point = (int(router_abr_1[0] + router_radius * math.cos(a)), int(router_abr_1[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    inter_area_routes["router_7__TO__router_abr1"] = [center_box, closest_point]
    
    # Router 2 (Area 1) --> Router 7 (Area 2)
    center_box = (router_7_pos[0] - router_radius, router_7_pos[1])
    x = center_box[0] - router_2_pos[0]
    y = center_box[1] - router_2_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_2_pos[0] + router_radius * math.cos(a)), int(router_2_pos[1] + router_radius * math.sin(a)))
    # pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    inter_area_routes["router_2__TO__router_7"] = [closest_point, center_box]
    
    # Router 10 (Area 2) --> Router 11 (Area 3)
    center_box = (router_10_pos[0] + router_radius, router_10_pos[1])
    x = center_box[0] - router_11_pos[0]
    y = center_box[1] - router_11_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_11_pos[0] + router_radius * math.cos(a)), int(router_11_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    inter_area_routes["router_10__TO__router_11"] = [center_box, closest_point]

    # NOTE: REMOVING THIS LINK FOR NOW
    # Router 10 (Area 2) --> Router 15 (Area 4)
    # center_box = (router_10_pos[0] + router_radius, router_10_pos[1])
    # x = center_box[0] - router_15_pos[0]
    # y = center_box[1] - router_15_pos[1]
    # a = math.atan2(y, x)
    # closest_point = (int(router_15_pos[0] + router_radius * math.cos(a)), int(router_15_pos[1] + router_radius * math.sin(a)))
    # pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    # inter_area_routes["router_10__TO__router__15"] = [center_box, closest_point]


    # Router 7 (Area 2) --> ISP
    center_box = (router_7_pos[0], router_7_pos[1] - router_radius)
    x = center_box[0] - router_isp_pos[0]
    y = center_box[1] - router_isp_pos[1]
    a = math.atan2(y, x)
    closest_point = (int(router_isp_pos[0] + router_radius * math.cos(a)), int(router_isp_pos[1] + router_radius * math.sin(a)))
    pygame.draw.line(screen, (0, 0, 0),  closest_point, center_box, 3)
    inter_area_routes["router_7__TO__router__isp"] = [center_box, closest_point]

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
    # Button to control the master simulation: which will do everything
    pygame.draw.rect(screen, master_button_color, (master_simulator[0], master_simulator[1], master_button_width, button_height))
    pygame.draw.rect(screen, master_button_color, (master_simulator_refresh[0], master_simulator_refresh[1], master_button_width, button_height))
    font = pygame.font.SysFont('Arial', 12)

    text_1 = font.render('Master Simulation', True, (0, 0, 0))
    text_2 = font.render('Clear Master Simulation', True, (0, 0, 0))

    text_pos_switch = ((master_button_width - font.size('Master Simulation')[0]) // 2, (button_height - font.size('Master Simulation')[1]) // 2)
    screen.blit(text_1, (master_simulator[0] + text_pos_switch[0], master_simulator[1] + text_pos_switch[1]))

    text_pos_switch = ((master_button_width - font.size('Clear Master Simulation')[0]) // 2, (button_height - font.size('Clear Master Simulation')[1]) // 2)
    screen.blit(text_2, (master_simulator_refresh[0] + text_pos_switch[0], master_simulator_refresh[1] + text_pos_switch[1]))

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

    # making the slider here --> commenting out the slider for now
    # pygame.draw.rect(screen, (0,0,0), (slider_position[0], slider_position[1], slider_width, slider_height))
    # slider_handle_x = slider_position[0] + 1 + (speed_slider_current_value - speed_slider_min_value) / (speed_slider_max_value - speed_slider_min_value) * slider_width
    # pygame.draw.rect(screen, (230, 120, 89), (slider_handle_x, slider_position[1], slider_handle_width, slider_height))

    # Buttons for LSA 3
    pygame.draw.rect(screen, (31, 128, 48), (button_LSA_3_pos[0], button_LSA_3_pos[1], button_width, button_height))
    pygame.draw.rect(screen, (31, 128, 48), (button_LSA_3_refresh[0], button_LSA_3_refresh[1], button_width, button_height))

    text_3 = font.render('Send LSA 3', True, (0, 0, 0))
    text_4 = font.render('Clear LSA3 text', True, (0, 0, 0))

    text_pos_switch = ((button_width - font.size('Send LSA 3')[0]) // 2, (button_height - font.size('Send LSA 3')[1]) // 2)
    screen.blit(text_3, (button_LSA_3_pos[0] + text_pos_switch[0], button_LSA_3_pos[1] + text_pos_switch[1]))

    text_pos_switch = ((button_width - font.size('Clear LSA3 text')[0]) // 2, (button_height - font.size('Clear LSA3 text')[1]) // 2)
    screen.blit(text_4, (button_LSA_3_refresh[0] + text_pos_switch[0], button_LSA_3_refresh[1] + text_pos_switch[1]))

    # Buttons for sending LSA 4
    pygame.draw.rect(screen, (31, 128, 48), (button_LSA_4_pos[0], button_LSA_4_pos[1], button_width, button_height))
    pygame.draw.rect(screen, (31, 128, 48), (button_LSA_4_refresh[0], button_LSA_4_refresh[1], button_width, button_height))

    text_3 = font.render('Send LSA 4', True, (0, 0, 0))
    text_4 = font.render('Clear LSA4 text', True, (0, 0, 0))

    text_pos_switch = ((button_width - font.size('Send LSA 4')[0]) // 2, (button_height - font.size('Send LSA 4')[1]) // 2)
    screen.blit(text_3, (button_LSA_4_pos[0] + text_pos_switch[0], button_LSA_4_pos[1] + text_pos_switch[1]))

    text_pos_switch = ((button_width - font.size('Clear LSA3 text')[0]) // 2, (button_height - font.size('Clear LSA3 text')[1]) // 2)
    screen.blit(text_4, (button_LSA_4_refresh[0] + text_pos_switch[0], button_LSA_4_refresh[1] + text_pos_switch[1]))
# Adding the animation buttons


# Update the screen
pygame.display.flip()

# # Set up the clock
# clock = pygame.time.Clock()

# Run the game loop
running = True

LSA_1_trigger = 0
LSA_3_trigger = 0
LSA_4_trigger = 0

master_simulation_trigger = 0
switch  = 1 # we start with LSA 1

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
                if LSA_1_trigger != 1:
                    Area_1_LSA.initialize_Area1_LSA()
                    Area_2_LSA.initialize_Area2_LSA()
                    Area_3_LSA.initialize_Area3_LSA()
                    LSA_1_trigger = 1
            
            if (button_LSA_1_refresh[0] < mouse_pos[0] < button_LSA_1_refresh[0] + button_width) and \
               (button_LSA_1_refresh[1] < mouse_pos[1] < button_LSA_1_refresh[1] + button_height):
                # TODO: If we set LSA_1_trigger = 0 in here, then the text dissapears but the LSA 1 sending process stops
                # to not stop the process while clearing the text, set LSA_1_trigger = 0 by some other button
                LSA_1_trigger = 0
                Area_1_LSA.erase_text()
                Area_2_LSA.erase_text()
                Area_3_LSA.erase_text()

            # if the SEND_LSA_3 button gets clicked
            if (button_LSA_3_pos[0] < mouse_pos[0] < button_LSA_3_pos[0] + button_width) and \
               (button_LSA_3_pos[1] < mouse_pos[1] < button_LSA_3_pos[1] + button_height):
                if LSA_3_trigger != 1:
                    Area_1_LSA_3.initialize_common_variables()
                    Area_1_LSA_3.initialize_Area1_LSA()
                    Area_1_LSA_3.initialize_Area2_LSA()
                    Area_1_LSA_3.initialize_Area3_LSA()
                    LSA_3_trigger = 1
            
            if (button_LSA_3_refresh[0] < mouse_pos[0] < button_LSA_3_refresh[0] + button_width) and \
               (button_LSA_3_refresh[1] < mouse_pos[1] < button_LSA_3_refresh[1] + button_height):
                LSA_3_trigger = 0
                Area_1_LSA_3.erase_text_area_1()
                Area_1_LSA_3.erase_text_area_2()
                Area_1_LSA_3.erase_text_area_3()

             # if the SEND_LSA_4 button gets clicked
            if (button_LSA_4_pos[0] < mouse_pos[0] < button_LSA_4_pos[0] + button_width) and \
               (button_LSA_4_pos[1] < mouse_pos[1] < button_LSA_4_pos[1] + button_height):
                if LSA_4_trigger != 1:
                    Area_LSA_4.initialize_common_variables()
                    Area_LSA_4.initialize_LSA_4_routes()
                    LSA_4_trigger = 1
            
            if (button_LSA_4_refresh[0] < mouse_pos[0] < button_LSA_4_refresh[0] + button_width) and \
               (button_LSA_4_refresh[1] < mouse_pos[1] < button_LSA_4_refresh[1] + button_height):
                LSA_4_trigger = 0
                Area_LSA_4.erase_LSA_4_text()

            
            # if the master_simulation button gets clicked
            if (master_simulator[0] < mouse_pos[0] < master_simulator[0] + master_button_width) and \
               (master_simulator[1] < mouse_pos[1] < master_simulator[1] + button_height):
                # ONE IDEA is to combiene all the LSA 3 files in 1 so we can reuse the positions
                if master_simulation_trigger != 1:
                    # doing LSA 1 initializations
                    Area_1_LSA.initialize_Area1_LSA()
                    Area_2_LSA.initialize_Area2_LSA()
                    Area_3_LSA.initialize_Area3_LSA()
                    
                    # doing Area 3 initializations
                    Area_1_LSA_3.initialize_Area1_LSA()
                    Area_1_LSA_3.initialize_Area2_LSA()
                    Area_1_LSA_3.initialize_Area3_LSA()
                    Area_1_LSA_3.initialize_common_variables()
                    master_simulation_trigger = 1
            
            if (master_simulator_refresh[0] < mouse_pos[0] < master_simulator_refresh[0] + master_button_width) and \
               (master_simulator_refresh[1] < mouse_pos[1] < master_simulator_refresh[1] + button_height):
                # TODO: we can remove this: it is un-needed
                master_simulation_trigger = 0
                # erase the last LSA (for now it is LSA 3)
                Area_1_LSA_3.erase_text_area_1()
                Area_1_LSA_3.erase_text_area_2()
                Area_1_LSA_3.erase_text_area_3()
            
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
    if LSA_1_trigger == 1:
        Area_1_LSA.SendArea1LSA1(pygame, screen) # figure out a way to know if all of this is complete or we would have to go all in manually
        Area_2_LSA.SendArea2LSA1(pygame, screen)
        Area_3_LSA.SendArea3LSA1(pygame, screen)
        # figure out some way to put LSA_1_trigger as 0
    
    if LSA_3_trigger == 1:
        Area_1_LSA_3.SendArea1LSA3(pygame, screen)
        Area_1_LSA_3.SendArea2LSA3(pygame, screen)
        Area_1_LSA_3.SendArea3LSA3(pygame, screen)

    if LSA_4_trigger == 1:
        Area_LSA_4.Send_LSA_4(pygame, screen)
    
    if master_simulation_trigger == 1:
        if switch == 1:
            r1 = Area_1_LSA.SendArea1LSA1(pygame, screen)
            r2 = Area_2_LSA.SendArea2LSA1(pygame, screen)
            r3 = Area_3_LSA.SendArea3LSA1(pygame, screen)
            # Add for area 3 in here
            if (r1 == 1 and r2 == 1 and r3 == 1):
                    switch = 3 # switch to LSA 3
                    # but also clear the data that was displayed because of LSA 1
                    Area_1_LSA.erase_text()
                    Area_2_LSA.erase_text()
                    Area_3_LSA.erase_text()
                    # TODO: Maybe display a text in here that LSA 1 is not complete
        elif switch == 3:
            r1 = Area_1_LSA_3.SendArea1LSA3(pygame, screen)
            r2 = Area_1_LSA_3.SendArea2LSA3(pygame, screen)
            r3 = Area_1_LSA_3.SendArea3LSA3(pygame, screen)
            if (r1 == 1 and r2 == 1 and r3 == 1):
                switch = 4 # switch to LSA 3
                # but also clear the data that was displayed because of LSA 1
                Area_1_LSA_3.erase_text_area_1()
                Area_1_LSA_3.erase_text_area_2()
                Area_1_LSA_3.erase_text_area_3()
        elif switch == 4:
            master_simulation_trigger = 0 # because we have no more LSAs to send right now
            switch = 1 # reset

    # Update the screen
    pygame.display.flip()
    clock.tick(10)

# Clean up
pygame.quit()

