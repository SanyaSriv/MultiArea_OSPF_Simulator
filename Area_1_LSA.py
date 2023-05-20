import math
import global_variables_file
from LSA_Class import LSATriangles
from global_variables_file import *

list_of_Area_1_triangles = []

def initialize_Area1_LSA():
    # I need 1 trianglesfrom router 1 (for now)
    var = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_1"][0], 
                                                 area_1_travel_routes["router_5_area_1__TO__router_1"][1], 
                                                 (120, 255, 100))
    var.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_1"][0],
                                                  area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                                  area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                  area_1_travel_routes["router_5_area_1__TO__router_2"][0]])
    list_of_Area_1_triangles.append(var)

def SendArea1LSA1(pygame, screen):
    global line
    
    for i in list_of_Area_1_triangles:
        i.draw(pygame, screen)
        i.move_triangle()

    # dx = global_variables_file.triangle_target[0] - global_variables_file.triangle_pos[0]
    # dy = global_variables_file.triangle_target[1] - global_variables_file.triangle_pos[1]
    # distance = math.sqrt(dx ** 2 + dy ** 2)
    # direction = (dx / distance, dy / distance)
    
    # # Update triangle position
    # if distance > triangle_speed:

    #     global_variables_file.triangle_pos = (
    #         global_variables_file.triangle_pos[0] + direction[0] * triangle_speed,
    #         global_variables_file.triangle_pos[1] + direction[1] * triangle_speed
    # )
    # elif (line == 0):
    #     # now it should travel from 5 to 2
    #     global_variables_file.triangle_pos = area_1_travel_routes["router_5_area_1__TO__router_2"][1]
    #     triangle_list.append([global_variables_file.triangle_pos])
    #     global_variables_file.triangle_target = area_1_travel_routes["router_5_area_1__TO__router_2"][0]
    #     line = 1

