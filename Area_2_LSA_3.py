import math
import global_variables_file
from LSA_Class import LSATriangles
from global_variables_file import *

list_of_Area_2_triangles = []

# AREA 2 WOULD BE SENDING LSA 3s to AREA 1 (for now)
# TODO: Later we would want to add functionality so we can send it to other areas as well
router_1_text = [0,0,0]
router_2_text = [0,0,0]
router_3_text = [0,0,0]
router_4_text = [0,0,0]
router_5_text = [0,0,0]
router_6_text = [0,0,0]

increase_position = 10
text_dictionary_LSA_3 = {}
list_text_position = []

def initialize_Area2_LSA():
    global router_1_text, router_2_text, router_3_text, router_4_text, router_5_text, router_6_text
    global list_text_position, text_dictionary_LSA_3

    # initialize all the text positions
    router_1_text = [220, 250, 1]
    router_2_text = [405, 375, 1]
    router_3_text = [35, 530, 1]
    router_4_text = [35, 330, 1]
    router_5_text = [175, 410, 1]
    router_6_text = [325, 530, 1]

    list_text_position = []
    text_dictionary_LSA_3 = {}

    # ROUTER 7 LSA 3 --> only sent out by the boundary router
    router_2_t1 = LSATriangles(inter_area_routes["router_2__TO__router_7"][1], 
                                inter_area_routes["router_2__TO__router_7"][0], 
                                (117, 227, 104))
    router_2_t1.enable_full_route([inter_area_routes["router_2__TO__router_7"][1], 
                                    inter_area_routes["router_2__TO__router_7"][0],
                                    area_1_travel_routes["router_2__TO__router_6"][0],
                                    area_1_travel_routes["router_2__TO__router_6"][1]])
    router_2_t1.update_starting_router("router_7")
    router_2_t1.update_router_path_names(["router_2", "router_6"])
    
    router_2_t2 = LSATriangles(inter_area_routes["router_2__TO__router_7"][1], 
                                            inter_area_routes["router_2__TO__router_7"][0], 
                                            (117, 227, 104))
    router_2_t2.enable_full_route([inter_area_routes["router_2__TO__router_7"][1], 
                                    inter_area_routes["router_2__TO__router_7"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    
    router_2_t2.update_starting_router("router_7")
    router_2_t2.update_router_path_names(["router_2", "router_5", "router_1"])

    router_2_t3 = LSATriangles(inter_area_routes["router_2__TO__router_7"][1], 
                                            inter_area_routes["router_2__TO__router_7"][0], 
                                            (117, 227, 104))
    router_2_t3.enable_full_route([inter_area_routes["router_2__TO__router_7"][1], 
                                    inter_area_routes["router_2__TO__router_7"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                    area_1_travel_routes["router_4__TO__router_3"][1],
                                    area_1_travel_routes["router_4__TO__router_3"][0]])
    
    router_2_t3.update_starting_router("router_7")
    router_2_t3.update_router_path_names(["router_2", "router_5", "router_4", "router_3"])

    list_of_Area_2_triangles.append(router_2_t1)
    list_of_Area_2_triangles.append(router_2_t2)
    list_of_Area_2_triangles.append(router_2_t3)

def SendArea2LSA3(pygame, screen):
    global router_1_text, router_2_text, router_3_text, router_4_text, router_5_text, router_6_text
    global list_text_position, text_dictionary_LSA_3

    font = pygame.font.Font(None, 14)

    for i in list_of_Area_2_triangles:
        i.draw(pygame, screen)
        return_value = i.move_triangle(pygame, screen)
        router_reached = return_value[0]
        router_started = return_value[1]
        to_be_removed = return_value[2]

        if (to_be_removed == 1):
            list_of_Area_2_triangles.remove(i) # so we do not have a permanent triangle stattioned on the last router
        if (router_reached != None):
            text_string = "Received LSA 3: {}".format(router_started)
            dictionary_text_string = "{} Received LSA 3 from {}".format(router_reached, router_started)
            
            if (dictionary_text_string in text_dictionary_LSA_3):
                continue
            else:
                text_dictionary_LSA_3[dictionary_text_string] = 1

            
            if router_reached == "router_1":
                list_text_position.append([text_string, (router_1_text[0], router_1_text[1])])
                router_1_text[router_1_text[2]] += increase_position
            elif router_reached == "router_2":
                list_text_position.append([text_string, (router_2_text[0], router_2_text[1])])
                router_2_text[router_2_text[2]] += increase_position
            elif router_reached == "router_3":
                list_text_position.append([text_string, (router_3_text[0], router_3_text[1])])
                router_3_text[router_3_text[2]] += increase_position
            elif router_reached == "router_4":
                list_text_position.append([text_string, (router_4_text[0], router_4_text[1])])
                router_4_text[router_4_text[2]] -= increase_position
            elif router_reached == "router_5":
                list_text_position.append([text_string, (router_5_text[0], router_5_text[1])])
                router_5_text[router_5_text[2]] += increase_position
            elif router_reached == "router_6":
                list_text_position.append([text_string, (router_6_text[0], router_6_text[1])])
                router_6_text[router_6_text[2]] += increase_position

    for i in list_text_position:
        text = font.render(i[0], True, (0, 0, 0))
        screen.blit(text, (i[1][0], i[1][1]))

    if list_of_Area_2_triangles == []:
        return 1 # complete
    
    return 0 # in progress

def erase_text():
    global text_dictionary_LSA_3
    global list_text_position

    text_dictionary_LSA_3 = {}
    list_text_position = []


 