import math
import global_variables_file
from LSA_Class import LSATriangles
from global_variables_file import *

list_of_Area_1_triangles = []
list_of_Area_2_triangles = []
list_text_position_area_3 = []
# AREA 1 WOULD BE SENDING LSA 3s to AREA 2 (Backbone Area) (FOR NOW)
# TODO: Later we would want to add functionality so we can send it to other areas as well

router_1_text = [0,0,0]
router_2_text = [0,0,0]
router_3_text = [0,0,0]
router_4_text = [0,0,0]
router_5_text = [0,0,0]
router_6_text = [0,0,0]
router_7_text = [0, 0, 0]
router_8_text = [0, 0, 0]
router_9_text = [0, 0, 0]
router_10_text = [0, 0, 0]
router_11_text = [0, 0, 0] # this is ABR 2
router_12_text = [0, 0, 0]
router_13_text = [0, 0, 0]
router_14_text = [0, 0, 0]
router_ABR1_text = [0,0,0]

increase_position = 10

text_dictionary_LSA_3_area_1 = {}
text_dictionary_LSA_3_area_2 = {}
text_dictionary_LSA_3_area_3 = {}

list_text_position_area_1 = []
list_text_position_area_2 = []
list_of_Area_3_triangles = []

def initialize_common_variables():
    global router_1_text, router_2_text, router_3_text, router_4_text
    global router_5_text, router_6_text
    global router_7_text, router_8_text, router_9_text, router_10_text
    global router_11_text, router_12_text, router_13_text, router_14_text
    global router_ABR1_text

    router_1_text = [220, 250, 1]
    router_2_text = [405, 375, 1]
    router_3_text = [35, 530, 1]
    router_4_text = [35, 330, 1]
    router_5_text = [175, 410, 1]
    router_6_text = [325, 530, 1]
    router_7_text = [630, 130, 1]
    router_8_text = [460, 280, 1]
    router_9_text = [610, 460, 1]
    router_10_text = [750, 320, 1]
    router_11_text = [950, 245, 1]
    router_12_text = [1030, 385, 1]
    router_13_text = [1220, 245, 1]
    router_14_text = [1220, 455, 1]
    router_ABR1_text = [350, 200, 1]

def initialize_Area1_LSA():
    global list_text_position_area_1, text_dictionary_LSA_3_area_1
   
    list_text_position_area_1 = []
    text_dictionary_LSA_3_area_1 = {}

    # ROUTER 2 LSA 3 --> only sent out by the boundary router
    router_2_t1 = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][1], 
                                inter_area_routes["router_7__TO__router_abr1"][0], 
                                (143, 134, 227))
    router_2_t1.enable_full_route([inter_area_routes["router_2__TO__router_7"][0], 
                                    inter_area_routes["router_2__TO__router_7"][1],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1]])
    router_2_t1.update_starting_router("ABR_1")
    router_2_t1.update_router_path_names(["router_7", "router_8", "router_9", "router_10"])
    
    router_2_t2 = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][1], 
                                inter_area_routes["router_7__TO__router_abr1"][0], 
                                (143, 134, 227))
    router_2_t2.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][1], 
                                    inter_area_routes["router_7__TO__router_abr1"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    inter_area_routes["router_10__TO__router_11"][1],
                                    area_3_travel_routes["router_11__TO__router_13"][0],
                                    area_3_travel_routes["router_11__TO__router_13"][1],
                                    area_3_travel_routes["router_13__TO__router_14"][0],
                                    area_3_travel_routes["router_13__TO__router_14"][1],
                                    area_3_travel_routes["router_14__TO__router_12"][0],
                                    area_3_travel_routes["router_14__TO__router_12"][1]])
    router_2_t2.update_starting_router("ABR_1")
    router_2_t2.update_router_path_names(["router_7", "router_10", "router_11: ABR_2", "router_13", "router_14", "router_12"])

    list_of_Area_1_triangles.append(router_2_t1)
    list_of_Area_1_triangles.append(router_2_t2)

    
def SendArea1LSA3(pygame, screen):
    
    global router_7_text, router_8_text, router_9_text, router_10_text
    global list_text_position_area_1, text_dictionary_LSA_3_area_1

    font = pygame.font.Font(None, 14)

    for i in list_of_Area_1_triangles:
        i.draw(pygame, screen)
        return_value = i.move_triangle(pygame, screen)
        router_reached = return_value[0]
        router_started = return_value[1]
        to_be_removed = return_value[2]

        if (to_be_removed == 1):
            list_of_Area_1_triangles.remove(i) # so we do not have a permanent triangle stationed on the last router
        if (router_reached != None):
            text_string = "Received LSA 3: Area 1"
            dictionary_text_string = "{} Received LSA 3 from Area 1".format(router_reached)
            # text_string = "Received LSA 3: {}".format(router_started)
            # dictionary_text_string = "{} Received LSA 3 from {}".format(router_reached, router_started)
            
            if (dictionary_text_string in text_dictionary_LSA_3_area_1):
                continue
            else:
                text_dictionary_LSA_3_area_1[dictionary_text_string] = 1

            if router_reached == "router_7":
                list_text_position_area_1.append([text_string, (router_7_text[0], router_7_text[1])])
                router_7_text[1] -= increase_position
            elif router_reached == "router_8":
                list_text_position_area_1.append([text_string, (router_8_text[0], router_8_text[1])])
                router_8_text[1] += increase_position
            elif router_reached == "router_9":
                list_text_position_area_1.append([text_string, (router_9_text[0], router_9_text[1])])
                router_9_text[1] += increase_position
            elif router_reached == "router_10":
                list_text_position_area_1.append([text_string, (router_10_text[0], router_10_text[1])])
                router_10_text[1] += increase_position
            elif router_reached == "router_11: ABR_2":
                list_text_position_area_1.append([text_string, (router_11_text[0], router_11_text[1])])
                router_11_text[1] -= increase_position
            elif router_reached == "router_12":
                list_text_position_area_1.append([text_string, (router_12_text[0], router_12_text[1])])
                router_12_text[1] -= increase_position
            elif router_reached == "router_13":
                list_text_position_area_1.append([text_string, (router_13_text[0], router_13_text[1])])
                router_13_text[1] -= increase_position
            elif router_reached == "router_14":
                list_text_position_area_1.append([text_string, (router_14_text[0], router_14_text[1])])
                router_14_text[1] += increase_position
            elif router_reached == "ABR_1":
                list_text_position_area_1.append([text_string, (router_ABR1_text[0], router_ABR1_text[1])])
                router_ABR1_text[1] -= increase_position
            
        
    for i in list_text_position_area_1:
        text = font.render(i[0], True, (0, 0, 0))
        screen.blit(text, (i[1][0], i[1][1]))

    if list_of_Area_1_triangles == []:
        return 1 # complete
    
    return 0 # in progress

def erase_text_area_1():
    global text_dictionary_LSA_3_area_1
    global list_text_position_area_1

    text_dictionary_LSA_3_area_1 = {}
    list_text_position_area_1 = []
    list_of_Area_1_triangles = []

def initialize_Area2_LSA():
    global router_1_text, router_2_text, router_3_text, router_4_text, router_5_text, router_6_text
    global list_text_position_area_2, text_dictionary_LSA_3_area_2
   
    list_text_position_area_2 = []
    text_dictionary_LSA_3_area_2 = {}

    # ROUTER 7 LSA 3 --> only sent out by the boundary router
    router_7_t1 = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0], 
                                inter_area_routes["router_2__TO__router_abr1"][1], 
                                (117, 227, 104))
    router_7_t1.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_2__TO__router_6"][0],
                                    area_1_travel_routes["router_2__TO__router_6"][1]])
    router_7_t1.update_starting_router("ABR_1")
    router_7_t1.update_router_path_names(["router_2", "router_6"])
    
    router_7_t2 = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0], 
                                inter_area_routes["router_2__TO__router_abr1"][1], 
                                (117, 227, 104))
    router_7_t2.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    
    router_7_t2.update_starting_router("ABR_1")
    router_7_t2.update_router_path_names(["router_2", "router_5", "router_1"])

    router_7_t3 = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0], 
                                inter_area_routes["router_2__TO__router_abr1"][1], 
                                (117, 227, 104))
    router_7_t3.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                    area_1_travel_routes["router_4__TO__router_3"][1],
                                    area_1_travel_routes["router_4__TO__router_3"][0]])
    
    router_7_t3.update_starting_router("ABR_1")
    router_7_t3.update_router_path_names(["router_2", "router_5", "router_4", "router_3"])

    router_10_t1 = LSATriangles(area_3_travel_routes["router_11__TO__router_13"][0],
                                area_3_travel_routes["router_11__TO__router_13"][1],
                                (117, 227, 104))
    router_10_t1.enable_full_route([area_3_travel_routes["router_11__TO__router_13"][0],
                                    area_3_travel_routes["router_11__TO__router_13"][1],
                                    area_3_travel_routes["router_13__TO__router_14"][0],
                                    area_3_travel_routes["router_13__TO__router_14"][1],
                                    area_3_travel_routes["router_14__TO__router_12"][0],
                                    area_3_travel_routes["router_14__TO__router_12"][1]])
    router_10_t1.update_starting_router("router_11: ABR_2")
    router_10_t1.update_router_path_names(["router_13", "router_14", "router_12"])

    list_of_Area_2_triangles.append(router_7_t1)
    list_of_Area_2_triangles.append(router_7_t2)
    list_of_Area_2_triangles.append(router_7_t3)
    list_of_Area_2_triangles.append(router_10_t1)

def SendArea2LSA3(pygame, screen):
    global router_1_text, router_2_text, router_3_text, router_4_text, router_5_text, router_6_text
    global list_text_position_area_2, text_dictionary_LSA_3_area_2

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
            text_string = "Received LSA 3: Area 2"
            dictionary_text_string = "{} Received LSA 3 from Area 2".format(router_reached)
            # text_string = "Received LSA 3: {}".format(router_started)
            # dictionary_text_string = "{} Received LSA 3 from {}".format(router_reached, router_started)
            
            if (dictionary_text_string in text_dictionary_LSA_3_area_2):
                continue
            else:
                text_dictionary_LSA_3_area_2[dictionary_text_string] = 1

            
            if router_reached == "router_1":
                list_text_position_area_2.append([text_string, (router_1_text[0], router_1_text[1])])
                router_1_text[router_1_text[2]] += increase_position
            elif router_reached == "router_2":
                list_text_position_area_2.append([text_string, (router_2_text[0], router_2_text[1])])
                router_2_text[router_2_text[2]] += increase_position
            elif router_reached == "router_3":
                list_text_position_area_2.append([text_string, (router_3_text[0], router_3_text[1])])
                router_3_text[router_3_text[2]] += increase_position
            elif router_reached == "router_4":
                list_text_position_area_2.append([text_string, (router_4_text[0], router_4_text[1])])
                router_4_text[router_4_text[2]] -= increase_position
            elif router_reached == "router_5":
                list_text_position_area_2.append([text_string, (router_5_text[0], router_5_text[1])])
                router_5_text[router_5_text[2]] += increase_position
            elif router_reached == "router_6":
                list_text_position_area_2.append([text_string, (router_6_text[0], router_6_text[1])])
                router_6_text[router_6_text[2]] += increase_position
            elif router_reached == "router_11: ABR_2":
                list_text_position_area_2.append([text_string, (router_11_text[0], router_11_text[1])])
                router_11_text[1] -= increase_position
            elif router_reached == "router_12":
                list_text_position_area_2.append([text_string, (router_12_text[0], router_12_text[1])])
                router_12_text[1] -= increase_position
            elif router_reached == "router_13":
                list_text_position_area_2.append([text_string, (router_13_text[0], router_13_text[1])])
                router_13_text[1] -= increase_position
            elif router_reached == "router_14":
                list_text_position_area_2.append([text_string, (router_14_text[0], router_14_text[1])])
                router_14_text[1] += increase_position
            elif router_reached == "ABR_1":
                list_text_position_area_1.append([text_string, (router_ABR1_text[0], router_ABR1_text[1])])
                router_ABR1_text[1] -= increase_position

    for i in list_text_position_area_2:
        text = font.render(i[0], True, (0, 0, 0))
        screen.blit(text, (i[1][0], i[1][1]))

    if list_of_Area_2_triangles == []:
        return 1 # complete
    
    return 0 # in progress

def erase_text_area_2():
    global text_dictionary_LSA_3_area_2
    global list_text_position_area_2
    global list_of_Area_2_triangles

    text_dictionary_LSA_3_area_2 = {}
    list_text_position_area_2 = []
    list_of_Area_2_triangles = []


def initialize_Area3_LSA():
    global list_text_position_area_3, text_dictionary_LSA_3_area_3
   
    list_text_position_area_3 = []
    text_dictionary_LSA_3_area_3 = {}

    router_11_t1 = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0], 
                                (237, 234, 57))
    router_11_t1.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][1]])
    router_11_t1.update_starting_router("router_11: ABR_2")
    router_11_t1.update_router_path_names(["router_10", "router_7", "router_8"])

    router_11_t2 = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0], 
                                (237, 234, 57))
    router_11_t2.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0]])
    router_11_t2.update_starting_router("router_11: ABR_2")
    router_11_t2.update_router_path_names(["router_10", "router_9", "router_8"])
    
    router_11_t3 = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0],
                                (237, 234, 57))
    router_11_t3.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][0], 
                                    inter_area_routes["router_7__TO__router_abr1"][1], 
                                    inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1], 
                                    area_1_travel_routes["router_2__TO__router_6"][0],
                                    area_1_travel_routes["router_2__TO__router_6"][1]])
    router_11_t3.update_starting_router("router_11: ABR_2")
    router_11_t3.update_router_path_names(["router_10", "router_7", "ABR_1", "router_2", "router_6"])
    
    router_11_t4 = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0],
                                (237, 234, 57))
    router_11_t4.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][0], 
                                    inter_area_routes["router_7__TO__router_abr1"][1], 
                                    inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1], 
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    
    router_11_t4.update_starting_router("router_11: ABR_2")
    router_11_t4.update_router_path_names(["router_10", "router_7", "ABR_1", "router_2", "router_5", "router_1"])

    router_11_t5 = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0],
                                (237, 234, 57))
    router_11_t5.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][0], 
                                    inter_area_routes["router_7__TO__router_abr1"][1], 
                                    inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1], 
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                    area_1_travel_routes["router_4__TO__router_3"][1],
                                    area_1_travel_routes["router_4__TO__router_3"][0]])
    
    router_11_t5.update_starting_router("router_11: ABR_2")
    router_11_t5.update_router_path_names(["router_10", "router_7", "ABR_1", "router_2", "router_5", "router_4", "router_3"])

    list_of_Area_3_triangles.append(router_11_t1)
    list_of_Area_3_triangles.append(router_11_t2)
    list_of_Area_3_triangles.append(router_11_t3)
    list_of_Area_3_triangles.append(router_11_t4)
    list_of_Area_3_triangles.append(router_11_t5)

def SendArea3LSA3(pygame, screen):
    global router_10_text, router_7_text, router_8_text, router_9_text
    global router_1_text, router_2_text, router_3_text, router_4_text, router_5_text, router_6_text

    global list_text_position_area_3, text_dictionary_LSA_3_area_3

    font = pygame.font.Font(None, 14)

    for i in list_of_Area_3_triangles:
        i.draw(pygame, screen)
        return_value = i.move_triangle(pygame, screen)
        router_reached = return_value[0]
        router_started = return_value[1]
        to_be_removed = return_value[2]

        if (to_be_removed == 1):
            list_of_Area_3_triangles.remove(i) # so we do not have a permanent triangle stattioned on the last router
        if (router_reached != None):
            text_string = "Received LSA 3: Area 3"
            dictionary_text_string = "{} Received LSA 3 from Area 3".format(router_reached)
            
            if (dictionary_text_string in text_dictionary_LSA_3_area_3):
                continue
            else:
                text_dictionary_LSA_3_area_3[dictionary_text_string] = 1

            if router_reached == "router_1":
                list_text_position_area_3.append([text_string, (router_1_text[0], router_1_text[1])])
                router_1_text[router_1_text[2]] += increase_position
            elif router_reached == "router_2":
                list_text_position_area_3.append([text_string, (router_2_text[0], router_2_text[1])])
                router_2_text[router_2_text[2]] += increase_position
            elif router_reached == "router_3":
                list_text_position_area_3.append([text_string, (router_3_text[0], router_3_text[1])])
                router_3_text[router_3_text[2]] += increase_position
            elif router_reached == "router_4":
                list_text_position_area_3.append([text_string, (router_4_text[0], router_4_text[1])])
                router_4_text[router_4_text[2]] -= increase_position
            elif router_reached == "router_5":
                list_text_position_area_3.append([text_string, (router_5_text[0], router_5_text[1])])
                router_5_text[router_5_text[2]] += increase_position
            elif router_reached == "router_6":
                list_text_position_area_3.append([text_string, (router_6_text[0], router_6_text[1])])
                router_6_text[router_6_text[2]] += increase_position
            elif router_reached == "router_7":
                list_text_position_area_3.append([text_string, (router_7_text[0], router_7_text[1])])
                router_7_text[1] -= increase_position
            elif router_reached == "router_8":
                list_text_position_area_3.append([text_string, (router_8_text[0], router_8_text[1])])
                router_8_text[1] += increase_position
            elif router_reached == "router_9":
                list_text_position_area_3.append([text_string, (router_9_text[0], router_9_text[1])])
                router_9_text[1] += increase_position
            elif router_reached == "router_10":
                list_text_position_area_3.append([text_string, (router_10_text[0], router_10_text[1])])
                router_10_text[1] += increase_position
            elif router_reached == "ABR_1":
                list_text_position_area_1.append([text_string, (router_ABR1_text[0], router_ABR1_text[1])])
                router_ABR1_text[1] -= increase_position

    for i in list_text_position_area_3:
        text = font.render(i[0], True, (0, 0, 0))
        screen.blit(text, (i[1][0], i[1][1]))

    if list_of_Area_3_triangles == []:
        return 1 # complete
    
    return 0 # in progress

def erase_text_area_3():
    global text_dictionary_LSA_3_area_3
    global list_text_position_area_3
    global list_of_Area_3_triangles

    text_dictionary_LSA_3_area_3 = {}
    list_text_position_area_3 = []
    list_of_Area_3_triangles = []


