import math
import global_variables_file
from LSA_Class import LSATriangles
from global_variables_file import *

list_of_Area_2_triangles = []

# third parameter: which index to increase
router_7_text = [0, 0, 0]
router_8_text = [0, 0, 0]
router_9_text = [0, 0, 0]
router_10_text = [0, 0, 0]
router_ABR_text = [0,0,0]

increase_position = 10

text_dictionary_LSA_1_area_2 = {}
list_text_position_area_2 = []

def initialize_Area2_LSA():
    global router_7_text, router_8_text, router_9_text, router_10_text
    global router_ABR_text
    global list_text_position_area_2, text_dictionary_LSA_1_area_2
    global list_of_Area_2_triangles

    # initialize all the text positions
    router_7_text = [630, 130, 1]
    router_8_text = [460, 280, 1]
    router_9_text = [610, 460, 1]
    router_10_text = [750, 320, 1]
    router_ABR_text = [350, 80, 1]

    list_text_position_area_2 = []
    text_dictionary_LSA_1_area_2 = {}
    list_of_Area_2_triangles = []

    # ROUTER 7 LSA 1
    router_7_t1 = LSATriangles(area_2_travel_routes["router_7__TO__router_8"][0],
                               area_2_travel_routes["router_7__TO__router_8"][1],
                                (137, 25, 181))
    router_7_t1.enable_full_route([area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1]])
    router_7_t1.update_starting_router("router_7")
    router_7_t1.update_router_path_names(["router_8", "router_9", "router_10"])

    router_7_t2 = LSATriangles(area_2_travel_routes["router_7__TO__router_10"][0],
                               area_2_travel_routes["router_7__TO__router_10"][1],
                                (137, 25, 181))
    router_7_t2.enable_full_route([area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1]])
    router_7_t2.update_starting_router("router_7")
    router_7_t2.update_router_path_names(["router_10"])
    
    # ROUTER 8 LSA 1
    router_8_t1 = LSATriangles(area_2_travel_routes["router_8__TO__router_9"][0],
                               area_2_travel_routes["router_8__TO__router_9"][1],
                                (181, 121, 25))
    router_8_t1.enable_full_route([area_2_travel_routes["router_8__TO__router_9"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1]])
    router_8_t1.update_starting_router("router_8")
    router_8_t1.update_router_path_names(["router_9", "router_10"])

    router_8_t2 = LSATriangles(area_2_travel_routes["router_7__TO__router_8"][1],
                               area_2_travel_routes["router_7__TO__router_8"][0],
                                (181, 121, 25))
    router_8_t2.enable_full_route([area_2_travel_routes["router_7__TO__router_8"][1],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1]])
    router_8_t2.update_starting_router("router_8")
    router_8_t2.update_router_path_names(["router_7", "router_10"])


    # ROUTER 9 LSA 1
    router_9_t1 = LSATriangles(area_2_travel_routes["router_8__TO__router_9"][1],
                               area_2_travel_routes["router_8__TO__router_9"][0],
                                (32, 158, 3))
    router_9_t1.enable_full_route([area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][1],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1]])
    router_9_t1.update_starting_router("router_9")
    router_9_t1.update_router_path_names(["router_8", "router_7", "router_10"])

    router_9_t2 = LSATriangles(area_2_travel_routes["router_9__TO__router_10"][0],
                               area_2_travel_routes["router_9__TO__router_10"][1],
                                (32, 158, 3))
    router_9_t2.enable_full_route([area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1]])
    router_9_t2.update_starting_router("router_9")
    router_9_t2.update_router_path_names(["router_10"])

    # ROUTER 10 LSA 1
    router_10_t1 = LSATriangles(area_2_travel_routes["router_7__TO__router_10"][1],
                               area_2_travel_routes["router_7__TO__router_10"][0],
                                (219, 15, 43))
    router_10_t1.enable_full_route([area_2_travel_routes["router_7__TO__router_10"][1],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][1]])
    router_10_t1.update_starting_router("router_10")
    router_10_t1.update_router_path_names(["router_7", "router_8"])

    router_10_t2 = LSATriangles(area_2_travel_routes["router_9__TO__router_10"][1],
                               area_2_travel_routes["router_9__TO__router_10"][0],
                                (219, 15, 43))
    router_10_t2.enable_full_route([area_2_travel_routes["router_9__TO__router_10"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0]])
    router_10_t2.update_starting_router("router_10")
    router_10_t2.update_router_path_names(["router_9", "router_8"])


    list_of_Area_2_triangles.append(router_7_t1)
    list_of_Area_2_triangles.append(router_7_t2)
    list_of_Area_2_triangles.append(router_8_t1)
    list_of_Area_2_triangles.append(router_8_t2)
    list_of_Area_2_triangles.append(router_9_t1)
    list_of_Area_2_triangles.append(router_9_t2)
    list_of_Area_2_triangles.append(router_10_t1)
    list_of_Area_2_triangles.append(router_10_t2)
    

    # ADDING CODE SO OUT NEW ABR 1 ROUTER RECIEVES LSA 1 FROM AREA 2
    
    # FROM ROUTER 7 TO ABR 1
    router_7_t3 = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][0],
                               inter_area_routes["router_7__TO__router_abr1"][1],
                                (137, 25, 181))
    router_7_t3.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][0],
                                inter_area_routes["router_7__TO__router_abr1"][1]])
    router_7_t3.update_starting_router("router_7")
    router_7_t3.update_router_path_names(["ABR_1"])

    # FROM ROUTER 8 TO ABR 1
    router_8_t3 = LSATriangles(area_2_travel_routes["router_7__TO__router_8"][1],
                               area_2_travel_routes["router_7__TO__router_8"][0],
                                (181, 121, 25))
    router_8_t3.enable_full_route([area_2_travel_routes["router_7__TO__router_8"][1],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][1]])
    router_8_t3.update_starting_router("router_8")
    router_8_t3.update_router_path_names(["router_7", "ABR_1"])

    # FROM ROUTER 9 TO ABR 1
    router_9_t3 = LSATriangles(area_2_travel_routes["router_8__TO__router_9"][1],
                               area_2_travel_routes["router_8__TO__router_9"][0],
                                (32, 158, 3))
    router_9_t3.enable_full_route([area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][1],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][1]])
    router_9_t3.update_starting_router("router_9")
    router_9_t3.update_router_path_names(["router_8", "router_7", "ABR_1"])

    # FROM ROUTER 10 TO ABR 1
    router_10_t3 = LSATriangles(area_2_travel_routes["router_7__TO__router_10"][1],
                               area_2_travel_routes["router_7__TO__router_10"][0],
                                (219, 15, 43))
    router_10_t3.enable_full_route([area_2_travel_routes["router_7__TO__router_10"][1],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][1]])
    router_10_t3.update_starting_router("router_10")
    router_10_t3.update_router_path_names(["router_7", "ABR_1"])

    list_of_Area_2_triangles.append(router_7_t3)
    list_of_Area_2_triangles.append(router_8_t3)
    list_of_Area_2_triangles.append(router_9_t3)
    list_of_Area_2_triangles.append(router_10_t3)
    
    # FROM ABR 1 TO OTHER ROUTERS
    # ABR 1 SHOULD ADVERTISE ITS OWN LSA 1s AS WELL
    router_ABR_t1 = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][1],
                                inter_area_routes["router_7__TO__router_abr1"][0],
                                (79, 24, 68))
    router_ABR_t1.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][1],
                                    inter_area_routes["router_7__TO__router_abr1"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1]])
    router_ABR_t1.update_starting_router("ABR_1")
    router_ABR_t1.update_router_path_names(["router_7", "router_8", "router_9", "router_10"])

    router_ABR_t2 = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][1],
                                inter_area_routes["router_7__TO__router_abr1"][0],
                                (79, 24, 68))
    router_ABR_t2.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][1],
                                    inter_area_routes["router_7__TO__router_abr1"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1]])
    router_ABR_t2.update_starting_router("ABR_1")
    router_ABR_t2.update_router_path_names(["router_7", "router_10"])

    list_of_Area_2_triangles.append(router_ABR_t1)
    list_of_Area_2_triangles.append(router_ABR_t2)

def SendArea2LSA1(pygame, screen):
    
    global router_7_text, router_8_text, router_9_text, router_10_text
    global text_dictionary_LSA_1_area_2
    global list_text_position_area_2

    font = pygame.font.Font(None, 14)

    for i in list_of_Area_2_triangles:
        i.draw(pygame, screen)
        return_value = i.move_triangle(pygame, screen)
        router_reached = return_value[0]
        router_started = return_value[1]
        to_be_removed = return_value[2]

        if (to_be_removed == 1):
            list_of_Area_2_triangles.remove(i) # so we do not have a permanent triangle stationed on the last router
        if (router_reached != None):
            text_string = "Recieved LSA 1: {}".format(router_started)
            dictionary_text_string = "{} Recieved LSA 1 from {}".format(router_reached, router_started)
            
            if (dictionary_text_string in text_dictionary_LSA_1_area_2):
                continue
            else:
                text_dictionary_LSA_1_area_2[dictionary_text_string] = 1

            if router_reached == "router_7":
                list_text_position_area_2.append([text_string, (router_7_text[0], router_7_text[1])])
                router_7_text[1] -= increase_position
            elif router_reached == "router_8":
                list_text_position_area_2.append([text_string, (router_8_text[0], router_8_text[1])])
                router_8_text[1] += increase_position
            elif router_reached == "router_9":
                list_text_position_area_2.append([text_string, (router_9_text[0], router_9_text[1])])
                router_9_text[1] += increase_position
            elif router_reached == "router_10":
                list_text_position_area_2.append([text_string, (router_10_text[0], router_10_text[1])])
                router_10_text[1] += increase_position
            elif router_reached == "ABR_1":
                list_text_position_area_2.append([text_string, (router_ABR_text[0], router_ABR_text[1])])
                router_ABR_text[router_ABR_text[2]] += increase_position
        
    for i in list_text_position_area_2:
        text = font.render(i[0], True, (0, 0, 0))
        screen.blit(text, (i[1][0], i[1][1]))

    if list_of_Area_2_triangles == []:
        return 1 # complete
    
    return 0 # in progress


def erase_text():
    global text_dictionary_LSA_1_area_2
    global list_text_position_area_2
    global list_of_Area_2_triangles

    list_of_Area_2_triangles = []
    text_dictionary_LSA_1_area_2 = {}
    list_text_position_area_2 = []
