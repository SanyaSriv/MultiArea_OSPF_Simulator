import math
import global_variables_file
from LSA_Class import LSATriangles
from global_variables_file import *

list_of_Area_3_triangles = []

# third parameter: which index to increase
router_11_text = [0, 0, 0]
router_12_text = [0, 0, 0]
router_13_text = [0, 0, 0]
router_14_text = [0, 0, 0]
increase_position = 10

text_dictionary_LSA_1_area_3 = {}
list_text_position_area_3 = []

def initialize_Area3_LSA():
    global router_11_text, router_12_text, router_13_text, router_14_text
    global list_text_position_area_3, text_dictionary_LSA_1_area_3
    global list_of_Area_3_triangles
    
    # initialize all the text positions
    router_11_text = [1030, 110, 1]
    router_12_text = [1030, 260, 1]
    router_13_text = [1220, 110, 1]
    router_14_text = [1220, 325, 1]

    list_of_Area_3_triangles = []
    list_text_position_area_3 = []
    text_dictionary_LSA_1_area_3 = {}

    # ROUTER 11 LSA 1
    router_11_t1 = LSATriangles(area_3_travel_routes["router_11__TO__router_13"][0],
                               area_3_travel_routes["router_11__TO__router_13"][1],
                                (137, 25, 181))
    router_11_t1.enable_full_route([area_3_travel_routes["router_11__TO__router_13"][0],
                                    area_3_travel_routes["router_11__TO__router_13"][1],
                                    area_3_travel_routes["router_13__TO__router_14"][0],
                                    area_3_travel_routes["router_13__TO__router_14"][1],
                                    area_3_travel_routes["router_14__TO__router_12"][0],
                                    area_3_travel_routes["router_14__TO__router_12"][1]])
    router_11_t1.update_starting_router("router_11")
    router_11_t1.update_router_path_names(["router_13", "router_14", "router_12"])
    
    # ROUTER 12 LSA 1
    router_12_t1 = LSATriangles(area_3_travel_routes["router_14__TO__router_12"][1],
                               area_3_travel_routes["router_14__TO__router_12"][0],
                                (17, 125, 181))
    router_12_t1.enable_full_route([area_3_travel_routes["router_14__TO__router_12"][1],
                                    area_3_travel_routes["router_14__TO__router_12"][0],
                                    area_3_travel_routes["router_13__TO__router_14"][1],
                                    area_3_travel_routes["router_13__TO__router_14"][0],
                                    area_3_travel_routes["router_11__TO__router_13"][1],
                                    area_3_travel_routes["router_11__TO__router_13"][0]])
    router_12_t1.update_starting_router("router_12")
    router_12_t1.update_router_path_names(["router_14", "router_13", "router_11"])


    # ROUTER 13 LSA 1
    router_13_t1 = LSATriangles(area_3_travel_routes["router_11__TO__router_13"][1],
                               area_3_travel_routes["router_11__TO__router_13"][0],
                                (32, 158, 3))
    router_13_t1.enable_full_route([area_3_travel_routes["router_11__TO__router_13"][1],
                                    area_3_travel_routes["router_11__TO__router_13"][0]])
    router_13_t1.update_starting_router("router_13")
    router_13_t1.update_router_path_names(["router_11"])

    router_13_t2 = LSATriangles(area_3_travel_routes["router_13__TO__router_14"][0],
                               area_3_travel_routes["router_13__TO__router_14"][1],
                                (32, 158, 3))
    router_13_t2.enable_full_route([area_3_travel_routes["router_13__TO__router_14"][0],
                                    area_3_travel_routes["router_13__TO__router_14"][1],
                                    area_3_travel_routes["router_14__TO__router_12"][0],
                                    area_3_travel_routes["router_14__TO__router_12"][1]])
    router_13_t2.update_starting_router("router_13")
    router_13_t2.update_router_path_names(["router_14", "router_12"])

    # ROUTER 14 LSA 1
    router_14_t1 = LSATriangles(area_3_travel_routes["router_14__TO__router_12"][0],
                                area_3_travel_routes["router_14__TO__router_12"][1],
                                (32, 15, 73))
    router_14_t1.enable_full_route([area_3_travel_routes["router_14__TO__router_12"][0],
                                    area_3_travel_routes["router_14__TO__router_12"][1]])
    router_14_t1.update_starting_router("router_14")
    router_14_t1.update_router_path_names(["router_12"])

    router_14_t2 = LSATriangles(area_3_travel_routes["router_13__TO__router_14"][1],
                                area_3_travel_routes["router_13__TO__router_14"][0],
                                (32, 15, 73))
    router_14_t2.enable_full_route([area_3_travel_routes["router_13__TO__router_14"][1],
                                    area_3_travel_routes["router_13__TO__router_14"][0],
                                    area_3_travel_routes["router_11__TO__router_13"][1],
                                    area_3_travel_routes["router_11__TO__router_13"][0]])
    router_14_t2.update_starting_router("router_14")
    router_14_t2.update_router_path_names(["router_13", "router_11"])

    list_of_Area_3_triangles.append(router_11_t1)
    list_of_Area_3_triangles.append(router_12_t1)
    list_of_Area_3_triangles.append(router_13_t2)
    list_of_Area_3_triangles.append(router_13_t1)
    list_of_Area_3_triangles.append(router_14_t1)
    list_of_Area_3_triangles.append(router_14_t2)
   
    
def SendArea3LSA1(pygame, screen):
    
    global router_11_text, router_12_text, router_13_text, router_14_text
    global text_dictionary_LSA_1_area_3
    global list_text_position_area_3

    font = pygame.font.Font(None, 14)

    for i in list_of_Area_3_triangles:
        i.draw(pygame, screen)
        return_value = i.move_triangle(pygame, screen)
        router_reached = return_value[0]
        router_started = return_value[1]
        to_be_removed = return_value[2]

        if (to_be_removed == 1):
            list_of_Area_3_triangles.remove(i) # so we do not have a permanent triangle stationed on the last router
        if (router_reached != None):
            text_string = "Recieved LSA 1: {}".format(router_started)
            dictionary_text_string = "{} Recieved LSA 1 from {}".format(router_reached, router_started)
            
            if (dictionary_text_string in text_dictionary_LSA_1_area_3):
                continue
            else:
                text_dictionary_LSA_1_area_3[dictionary_text_string] = 1

            if router_reached == "router_11":
                list_text_position_area_3.append([text_string, (router_11_text[0], router_11_text[1])])
                router_11_text[1] -= increase_position
            elif router_reached == "router_12":
                list_text_position_area_3.append([text_string, (router_12_text[0], router_12_text[1])])
                router_12_text[1] -= increase_position
            elif router_reached == "router_13":
                list_text_position_area_3.append([text_string, (router_13_text[0], router_13_text[1])])
                router_13_text[1] -= increase_position
            elif router_reached == "router_14":
                list_text_position_area_3.append([text_string, (router_14_text[0], router_14_text[1])])
                router_14_text[1] += increase_position
        
    for i in list_text_position_area_3:
        text = font.render(i[0], True, (0, 0, 0))
        screen.blit(text, (i[1][0], i[1][1]))

    if list_of_Area_3_triangles == []:
        return 1 # complete
    
    return 0 # in progress


def erase_text():
    global text_dictionary_LSA_1_area_3
    global list_text_position_area_3
    global list_of_Area_3_triangles

    text_dictionary_LSA_1_area_3 = {}
    list_text_position_area_3 = []
    list_of_Area_3_triangles = []
