import math
import global_variables_file
from LSA_Class import LSATriangles
from global_variables_file import *

list_of_LSA_4_triangles = []
list_text_position = []
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
router_11_text = [0, 0, 0]
router_12_text = [0, 0, 0]
router_13_text = [0, 0, 0]
router_14_text = [0, 0, 0]
router_ABR_text = [0,0,0]

increase_position = 10

text_dictionary_LSA_4 = {}

def initialize_common_variables():
    global router_1_text, router_2_text, router_3_text, router_4_text
    global router_5_text, router_6_text, router_ABR_text
    global router_7_text, router_8_text, router_9_text, router_10_text
    global router_11_text, router_12_text, router_13_text, router_14_text

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
    router_ABR_text = [350, 200, 1]

def initialize_LSA_4_routes():
    global list_text_position, text_dictionary_LSA_4
   
    list_text_position = []
    text_dictionary_LSA_4 = {}

    # ROUTER 7 LSA 3 --> only sent out by the boundary router
    router_7_t1 = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][0],
                                inter_area_routes["router_7__TO__router_abr1"][1],
                                (117, 227, 104))
    router_7_t1.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][0],
                                   inter_area_routes["router_7__TO__router_abr1"][1],
                                    inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_2__TO__router_6"][0],
                                    area_1_travel_routes["router_2__TO__router_6"][1]])
    router_7_t1.update_starting_router("router_7")
    router_7_t1.update_router_path_names(["ABR_1", "router_2", "router_6"])
    
    router_7_t2 = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][0],
                                inter_area_routes["router_7__TO__router_abr1"][1],
                                (117, 227, 104))
    router_7_t2.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][0],
                                   inter_area_routes["router_7__TO__router_abr1"][1],
                                    inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    
    router_7_t2.update_starting_router("router_7")
    router_7_t2.update_router_path_names(["ABR_1", "router_2", "router_5", "router_1"])

    router_7_t3 = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][0],
                                   inter_area_routes["router_7__TO__router_abr1"][1],
                                            (117, 227, 104))
    router_7_t3.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][0],
                                   inter_area_routes["router_7__TO__router_abr1"][1],
                                    inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                    area_1_travel_routes["router_4__TO__router_3"][1],
                                    area_1_travel_routes["router_4__TO__router_3"][0]])
    
    router_7_t3.update_starting_router("router_7")
    router_7_t3.update_router_path_names(["ABR_1", "router_2", "router_5", "router_4", "router_3"])

    router_7_t5 = LSATriangles(area_2_travel_routes["router_7__TO__router_10"][0],
                                area_2_travel_routes["router_7__TO__router_10"][1],
                                (117, 227, 104))
    router_7_t5.enable_full_route([area_2_travel_routes["router_7__TO__router_10"][0],
                                   area_2_travel_routes["router_7__TO__router_10"][1],
                                   area_2_travel_routes["router_9__TO__router_10"][1],
                                   area_2_travel_routes["router_9__TO__router_10"][0]])
    router_7_t5.update_starting_router("router_7")
    router_7_t5.update_router_path_names(["router_10", "router_9"])

    router_7_t6 = LSATriangles(area_2_travel_routes["router_7__TO__router_8"][0],
                                area_2_travel_routes["router_7__TO__router_8"][1],
                                (117, 227, 104))
    router_7_t6.enable_full_route([area_2_travel_routes["router_7__TO__router_8"][0],
                                   area_2_travel_routes["router_7__TO__router_8"][1],
                                   area_2_travel_routes["router_8__TO__router_9"][0],
                                   area_2_travel_routes["router_8__TO__router_9"][1],
                                   area_2_travel_routes["router_9__TO__router_10"][0],
                                   area_2_travel_routes["router_9__TO__router_10"][1]])
    router_7_t6.update_starting_router("router_7")
    router_7_t6.update_router_path_names(["router_8", "router_9", "router_10"])

    # ASK PROFESSOR ABOUT THIS: IS IT OKAY IS 9 SENDS IT TO 10, OR SHOULD IT NOT?

    # Area 3 is stubby area so the below should not happen
    # Something to confirm with Professor: ASK PROFESSOR ABOUT THIS:
    # Should Router 10 not even send something to Area 3? 
    # Or does router 10 send to router 11 but router 11 rejects it and does not propagate

    # router_7_t4 = LSATriangles(area_2_travel_routes["router_7__TO__router_10"][0],
    #                             area_2_travel_routes["router_7__TO__router_10"][1],
    #                             (117, 227, 104))
    # router_7_t4.enable_full_route([area_2_travel_routes["router_7__TO__router_10"][0],
    #                                 area_2_travel_routes["router_7__TO__router_10"][1],
    #                                 inter_area_routes["router_10__TO__router_11"][0],
    #                                 inter_area_routes["router_10__TO__router_11"][1],
    #                                 area_3_travel_routes["router_11__TO__router_13"][0],
    #                                 area_3_travel_routes["router_11__TO__router_13"][1],
    #                                 area_3_travel_routes["router_13__TO__router_14"][0],
    #                                 area_3_travel_routes["router_13__TO__router_14"][1],
    #                                 area_3_travel_routes["router_14__TO__router_12"][0],
    #                                 area_3_travel_routes["router_14__TO__router_12"][1]])
    # router_7_t4.update_starting_router("router_7")
    # router_7_t4.update_router_path_names(["router_10", "router_11", "router_13", "router_14", "router_12"])

    # ABR 2 RECIEVES BUT DOES NOT PROPOGATE
    router_7_t4 = LSATriangles(area_2_travel_routes["router_7__TO__router_10"][0],
                                area_2_travel_routes["router_7__TO__router_10"][1],
                                (117, 227, 104))
    router_7_t4.enable_full_route([area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    inter_area_routes["router_10__TO__router_11"][1]])
    router_7_t4.update_starting_router("router_7")
    router_7_t4.update_router_path_names(["router_10", "router_11"])

    list_of_LSA_4_triangles.append(router_7_t1)
    list_of_LSA_4_triangles.append(router_7_t2)
    list_of_LSA_4_triangles.append(router_7_t3)
    list_of_LSA_4_triangles.append(router_7_t4)
    list_of_LSA_4_triangles.append(router_7_t5)
    list_of_LSA_4_triangles.append(router_7_t6)

def Send_LSA_4(pygame, screen):
    global router_1_text, router_2_text, router_3_text, router_4_text, router_5_text, router_6_text
    global list_text_position, text_dictionary_LSA_4
    global router_ABR_text

    font = pygame.font.Font(None, 14)

    for i in list_of_LSA_4_triangles:
        i.draw(pygame, screen)
        return_value = i.move_triangle(pygame, screen)
        router_reached = return_value[0]
        router_started = return_value[1]
        to_be_removed = return_value[2]

        if (to_be_removed == 1):
            list_of_LSA_4_triangles.remove(i) # so we do not have a permanent triangle stattioned on the last router
        if (router_reached != None):
            if router_reached in ["router_7", "router_8", "router_9", "router_10", "ABR_1", "router_11"]:
                text_string = "Received LSA 1: {}".format(router_started)
                dictionary_text_string = "{} Received LSA 4 from {}".format(router_reached, router_started)
            else:
                text_string = "Received LSA 4: {}".format(router_started)
                dictionary_text_string = "{} Received LSA 4 from {}".format(router_reached, router_started)
            
            if (dictionary_text_string in text_dictionary_LSA_4):
                continue
            else:
                text_dictionary_LSA_4[dictionary_text_string] = 1

            
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
            elif router_reached == "router_7":
                list_text_position.append([text_string, (router_7_text[0], router_7_text[1])])
                router_7_text[1] -= increase_position
            elif router_reached == "router_8":
                list_text_position.append([text_string, (router_8_text[0], router_8_text[1])])
                router_8_text[1] += increase_position
            elif router_reached == "router_9":
                list_text_position.append([text_string, (router_9_text[0], router_9_text[1])])
                router_9_text[1] += increase_position
            elif router_reached == "router_10":
                list_text_position.append([text_string, (router_10_text[0], router_10_text[1])])
                router_10_text[1] += increase_position
            elif router_reached == "router_11":
                list_text_position.append([text_string, (router_11_text[0], router_11_text[1])])
                router_11_text[1] -= increase_position
            elif router_reached == "router_12":
                list_text_position.append([text_string, (router_12_text[0], router_12_text[1])])
                router_12_text[1] -= increase_position
            elif router_reached == "router_13":
                list_text_position.append([text_string, (router_13_text[0], router_13_text[1])])
                router_13_text[1] -= increase_position
            elif router_reached == "router_14":
                list_text_position.append([text_string, (router_14_text[0], router_14_text[1])])
                router_14_text[1] += increase_position
            elif router_reached == "ABR_1":
                list_text_position.append([text_string, (router_ABR_text[0], router_ABR_text[1])])
                router_ABR_text[1] += increase_position

    for i in list_text_position:
        text = font.render(i[0], True, (0, 0, 0))
        screen.blit(text, (i[1][0], i[1][1]))

    if list_of_LSA_4_triangles == []:
        return 1 # complete
    
    return 0 # in progress


def erase_LSA_4_text():
    global text_dictionary_LSA_4
    global list_text_position
    global list_of_LSA_4_triangles

    text_dictionary_LSA_4 = {}
    list_text_position = []
    list_of_LSA_4_triangles = []