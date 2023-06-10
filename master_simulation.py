import math
import global_variables_file
from LSA_Class import LSATriangles
from global_variables_file import *

# third parameter: which index to increase
router_1_text = [0,0,0]
router_2_text = [0,0,0]
router_3_text = [0,0,0]
router_4_text = [0,0,0]
router_5_text = [0,0,0]
router_6_text = [0,0,0]
router_ABR_text = [0,0,0]
router_7_text = [0, 0, 0]
router_8_text = [0, 0, 0]
router_9_text = [0, 0, 0]
router_10_text = [0, 0, 0]
router_11_text = [0,0,0]
router_12_text = [0,0,0]
router_13_text = [0,0,0]
router_14_text = [0,0,0]

seperate_lsa_3 = 0

increase_position = 10
global_counter = 0

# for area 1
list_of_Area_1_triangles = []
text_dictionary_LSA_1 = {}
list_text_position = []

# for area 2
list_of_Area_2_triangles = []
text_dictionary_LSA_1_area_2 = {}
list_text_position_area_2 = []

# for area 3
list_of_Area_3_triangles = []
text_dictionary_LSA_1_area_3 = {}
list_text_position_area_3 = []
color_property = 0

def sub_some_x(lis, val):
    return [lis[0] - val, lis[1], lis[2]]

def global_initialization(LSA_3):
     # initialize all the text positions
    global router_1_text, router_2_text, router_3_text, router_4_text
    global router_5_text, router_6_text
    global router_7_text, router_8_text, router_9_text, router_10_text
    global router_12_text, router_13_text, router_14_text
    global router_11_text
    global router_ABR_text
    global global_counter
    global seperate_lsa_3

    global_counter = 0
    seperate_lsa_3 = LSA_3

    # if LSA_3 == 0:
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
    router_ABR_text = [350, 100, 1]
    router_11_text = [950, 245, 1]
    router_12_text = [1030, 385, 1]
    router_13_text = [1220, 245, 1]
    router_14_text = [1220, 455, 1]
    # elif LSA_3 == 1:
    #     router_1_text = [200, 250, 1]
    #     router_2_text = [380, 375, 1]
    #     router_3_text = [35, 530, 1]
    #     router_4_text = [35, 330, 1]
    #     router_5_text = [175, 410, 1]
    #     router_6_text = [325, 530, 1]
    #     router_7_text = [630, 130, 1]
    #     router_8_text = [460, 280, 1]
    #     router_9_text = [610, 460, 1]
    #     router_10_text = [750, 320, 1]
    #     router_ABR_text = [350, 100, 1]
    #     router_11_text = [950, 245, 1]
    #     router_12_text = [1030, 385, 1]
    #     router_13_text = [1220, 245, 1]
    #     router_14_text = [1220, 455, 1]

def initialize_Area1_LSA():
    global router_1_text, router_2_text, router_3_text, router_4_text, router_5_text, router_6_text
    global router_ABR_text
    global list_text_position, text_dictionary_LSA_1
    global list_of_Area_1_triangles

    list_text_position = []
    text_dictionary_LSA_1 = {}
    list_of_Area_1_triangles = []

    # ROUTER 1 LSA 1
    router_1_t1 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_1"][0], 
                                            area_1_travel_routes["router_5_area_1__TO__router_1"][1], 
                                            router_1_color)
    router_1_t1.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_1"][0],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                                area_1_travel_routes["router_2__TO__router_6"][0],
                                                area_1_travel_routes["router_2__TO__router_6"][1]])
    router_1_t1.update_starting_router("router_1")
    router_1_t1.update_router_path_names(["router_5", "router_2", "router_6"])
    
    router_1_t2 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_1"][0], 
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][1], 
                                                router_1_color)
    router_1_t2.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_1"][0],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                                area_1_travel_routes["router_4__TO__router_3"][1],
                                                area_1_travel_routes["router_4__TO__router_3"][0]])
    router_1_t2.update_starting_router("router_1")
    router_1_t2.update_router_path_names(["router_5", "router_4", "router_3"])

    # ROUTER 2 LSA 1
    router_2_t1 = LSATriangles(area_1_travel_routes["router_2__TO__router_6"][0], 
                                            area_1_travel_routes["router_2__TO__router_6"][1], 
                                            router_2_color)
    router_2_t1.enable_full_route([area_1_travel_routes["router_2__TO__router_6"][0],
                                                area_1_travel_routes["router_2__TO__router_6"][1]])
    router_2_t1.update_starting_router("router_2")
    router_2_t1.update_router_path_names(["router_6"])
    
    router_2_t2 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_2"][0], 
                                            area_1_travel_routes["router_5_area_1__TO__router_2"][1], 
                                            router_2_color)
    router_2_t2.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    router_2_t2.update_starting_router("router_2")
    router_2_t2.update_router_path_names(["router_5", "router_1"])
    
    router_2_t3 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_2"][0], 
                                            area_1_travel_routes["router_5_area_1__TO__router_2"][1], 
                                            router_2_color)
    router_2_t3.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                                area_1_travel_routes["router_4__TO__router_3"][1],
                                                area_1_travel_routes["router_4__TO__router_3"][0]])
    router_2_t3.update_starting_router("router_2")
    router_2_t3.update_router_path_names(["router_5", "router_4", "router_3"])

    # ROUTER 3 LSA 1
    router_3_t1 = LSATriangles(area_1_travel_routes["router_4__TO__router_3"][0],
                               area_1_travel_routes["router_4__TO__router_3"][1],
                                router_3_color)
    router_3_t1.enable_full_route([area_1_travel_routes["router_4__TO__router_3"][0],
                                   area_1_travel_routes["router_4__TO__router_3"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                   area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    router_3_t1.update_starting_router("router_3")
    router_3_t1.update_router_path_names(["router_4", "router_5", "router_1"])

    router_3_t2 = LSATriangles(area_1_travel_routes["router_4__TO__router_3"][0],
                               area_1_travel_routes["router_4__TO__router_3"][1],
                                router_3_color)
    router_3_t2.enable_full_route([area_1_travel_routes["router_4__TO__router_3"][0],
                                   area_1_travel_routes["router_4__TO__router_3"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                   area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                   area_1_travel_routes["router_2__TO__router_6"][0],
                                   area_1_travel_routes["router_2__TO__router_6"][1]])
    router_3_t2.update_starting_router("router_3")
    router_3_t2.update_router_path_names(["router_4", "router_5", "router_2", "router_6"])

    # ROUTER 4 LSA 1
    router_4_t1 = LSATriangles(area_1_travel_routes["router_4__TO__router_3"][1],
                               area_1_travel_routes["router_4__TO__router_3"][0],
                                router_4_color)
    router_4_t1.enable_full_route([area_1_travel_routes["router_4__TO__router_3"][1],
                                   area_1_travel_routes["router_4__TO__router_3"][0]])
    router_4_t1.update_starting_router("router_4")
    router_4_t1.update_router_path_names(["router_3"])

    router_4_t2 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                               area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                router_4_color)
    router_4_t2.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                   area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    router_4_t2.update_starting_router("router_4")
    router_4_t2.update_router_path_names(["router_5", "router_1"])

    router_4_t3 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                               area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                router_4_color)
    router_4_t3.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                   area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                   area_1_travel_routes["router_2__TO__router_6"][0],
                                   area_1_travel_routes["router_2__TO__router_6"][1]])
    router_4_t3.update_starting_router("router_4")
    router_4_t3.update_router_path_names(["router_5", "router_2", "router_6"])

    # ROUTER 5 LSA 1
    router_5_t1 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_1"][1], 
                                            area_1_travel_routes["router_5_area_1__TO__router_1"][0], 
                                            router_5_color)
    router_5_t1.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    router_5_t1.update_starting_router("router_5")
    router_5_t1.update_router_path_names(["router_1"])

    router_5_t2 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_4"][1], 
                                            area_1_travel_routes["router_5_area_1__TO__router_4"][0], 
                                            router_5_color)
    router_5_t2.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                                area_1_travel_routes["router_4__TO__router_3"][1],
                                                area_1_travel_routes["router_4__TO__router_3"][0]])
    router_5_t2.update_starting_router("router_5")
    router_5_t2.update_router_path_names(["router_4", "router_3"])

    router_5_t3 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_2"][1], 
                                            area_1_travel_routes["router_5_area_1__TO__router_2"][0], 
                                            router_5_color)
    router_5_t3.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                                area_1_travel_routes["router_2__TO__router_6"][0],
                                                area_1_travel_routes["router_2__TO__router_6"][1]])
    router_5_t3.update_starting_router("router_5")
    router_5_t3.update_router_path_names(["router_2", "router_6"])

    # ROUTER 6 LSA 1
    router_6_t1 = LSATriangles(area_1_travel_routes["router_2__TO__router_6"][1],
                               area_1_travel_routes["router_2__TO__router_6"][0],
                               router_6_color)
    router_6_t1.enable_full_route([area_1_travel_routes["router_2__TO__router_6"][1],
                                   area_1_travel_routes["router_2__TO__router_6"][0],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    router_6_t1.update_starting_router("router_6")
    router_6_t1.update_router_path_names(["router_2", "router_5", "router_1"])

    router_6_t2 = LSATriangles(area_1_travel_routes["router_2__TO__router_6"][1],
                               area_1_travel_routes["router_2__TO__router_6"][0],
                               router_6_color)
    router_6_t2.enable_full_route([area_1_travel_routes["router_2__TO__router_6"][1],
                                   area_1_travel_routes["router_2__TO__router_6"][0],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                   area_1_travel_routes["router_4__TO__router_3"][1],
                                   area_1_travel_routes["router_4__TO__router_3"][0]])
    router_6_t2.update_starting_router("router_6")
    router_6_t2.update_router_path_names(["router_2", "router_5", "router_4", "router_3"])

    list_of_Area_1_triangles.append(router_1_t1)
    list_of_Area_1_triangles.append(router_1_t2)
    list_of_Area_1_triangles.append(router_2_t1)
    list_of_Area_1_triangles.append(router_2_t2)
    list_of_Area_1_triangles.append(router_2_t3)
    list_of_Area_1_triangles.append(router_3_t1)
    list_of_Area_1_triangles.append(router_3_t2)
    list_of_Area_1_triangles.append(router_4_t1)
    list_of_Area_1_triangles.append(router_4_t2)
    list_of_Area_1_triangles.append(router_4_t3)
    list_of_Area_1_triangles.append(router_5_t1)
    list_of_Area_1_triangles.append(router_5_t2)
    list_of_Area_1_triangles.append(router_5_t3)
    list_of_Area_1_triangles.append(router_6_t1)
    list_of_Area_1_triangles.append(router_6_t2)

    # Adding some additional code so the ABR recieves the LSA 1s as well

    # FROM ROUTER 1 TO ABR 1 
    router_1_t3 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_1"][0], 
                                            area_1_travel_routes["router_5_area_1__TO__router_1"][1], 
                                            router_1_color)
    router_1_t3.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_1"][0],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                                inter_area_routes["router_2__TO__router_abr1"][1],
                                                inter_area_routes["router_2__TO__router_abr1"][0]])
    router_1_t3.update_starting_router("router_1")
    router_1_t3.update_router_path_names(["router_5", "router_2", "ABR_1"])

    # FROM ROUTER 1 TO ABR 1
    router_2_t4 = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][1],
                                inter_area_routes["router_2__TO__router_abr1"][0], 
                                            router_2_color)
    router_2_t4.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][1],
                                   inter_area_routes["router_2__TO__router_abr1"][0]])
    router_2_t4.update_starting_router("router_2")
    router_2_t4.update_router_path_names(["ABR_1"])

    # FROM ROUTER 3 TO ABR 1
    router_3_t3 = LSATriangles(area_1_travel_routes["router_4__TO__router_3"][0],
                               area_1_travel_routes["router_4__TO__router_3"][1],
                                router_3_color)
    router_3_t3.enable_full_route([area_1_travel_routes["router_4__TO__router_3"][0],
                                   area_1_travel_routes["router_4__TO__router_3"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                   area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                   inter_area_routes["router_2__TO__router_abr1"][1],
                                   inter_area_routes["router_2__TO__router_abr1"][0]])
    router_3_t3.update_starting_router("router_3")
    router_3_t3.update_router_path_names(["router_4", "router_5", "router_2", "ABR_1"])

    # FROM ROUTER 4 TO ABR 1
    router_4_t4 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                               area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                router_4_color)
    router_4_t4.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                   area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                   area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                   inter_area_routes["router_2__TO__router_abr1"][1],
                                   inter_area_routes["router_2__TO__router_abr1"][0]])
    router_4_t4.update_starting_router("router_4")
    router_4_t4.update_router_path_names(["router_5", "router_2", "ABR_1"])

    # FROM ROUTER 5 TO ABR 1
    router_5_t4 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_2"][1], 
                                area_1_travel_routes["router_5_area_1__TO__router_2"][0], 
                                            router_5_color)
    router_5_t4.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                                inter_area_routes["router_2__TO__router_abr1"][1],
                                                inter_area_routes["router_2__TO__router_abr1"][0]])
    router_5_t4.update_starting_router("router_5")
    router_5_t4.update_router_path_names(["router_2", "ABR_1"])

    # FROM ROUTER 6 TO ABR 1
    router_6_t3 = LSATriangles(area_1_travel_routes["router_2__TO__router_6"][1],
                               area_1_travel_routes["router_2__TO__router_6"][0],
                               router_6_color)
    router_6_t3.enable_full_route([area_1_travel_routes["router_2__TO__router_6"][1],
                                   area_1_travel_routes["router_2__TO__router_6"][0],
                                   inter_area_routes["router_2__TO__router_abr1"][1],
                                   inter_area_routes["router_2__TO__router_abr1"][0]])
    router_6_t3.update_starting_router("router_6")
    router_6_t3.update_router_path_names(["router_2", "ABR_1"])
    

    list_of_Area_1_triangles.append(router_1_t3)
    list_of_Area_1_triangles.append(router_2_t4)
    list_of_Area_1_triangles.append(router_3_t3)
    list_of_Area_1_triangles.append(router_4_t4)
    list_of_Area_1_triangles.append(router_5_t4)
    list_of_Area_1_triangles.append(router_6_t3)


    # ABR sends its LSA 1s
    router_ABR_t1 = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0],
                                inter_area_routes["router_2__TO__router_abr1"][1],
                               router_ABR1_color)
    router_ABR_t1.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0],
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_2__TO__router_6"][0],
                                    area_1_travel_routes["router_2__TO__router_6"][1]])
    router_ABR_t1.update_starting_router("ABR_1")
    router_ABR_t1.update_router_path_names(["router_2", "router_6"])
    
    router_ABR_t2 = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0],
                                inter_area_routes["router_2__TO__router_abr1"][1], 
                               router_ABR1_color)
    router_ABR_t2.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0],
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    router_ABR_t2.update_starting_router("ABR_1")
    router_ABR_t2.update_router_path_names(["router_2", "router_5", "router_1"])
    
    router_ABR_t3 = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0],
                                inter_area_routes["router_2__TO__router_abr1"][1], 
                               router_ABR1_color)
    router_ABR_t3.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0],
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                    area_1_travel_routes["router_4__TO__router_3"][1],
                                    area_1_travel_routes["router_4__TO__router_3"][0]])
    router_ABR_t3.update_starting_router("ABR_1")
    router_ABR_t3.update_router_path_names(["router_2", "router_5", "router_4", "router_3"])

    list_of_Area_1_triangles.append(router_ABR_t1)
    list_of_Area_1_triangles.append(router_ABR_t2)
    list_of_Area_1_triangles.append(router_ABR_t3)

def SendArea1LSA1(pygame, screen):
    
    global router_1_text, router_2_text, router_3_text, router_4_text, router_5_text, router_6_text
    global router_ABR_text
    global text_dictionary_LSA_1
    global list_text_position
    global seperate_lsa_3

    font = pygame.font.Font(None, 14)

    for i in list_of_Area_1_triangles:
        i.draw(pygame, screen)
        return_value = i.move_triangle(pygame, screen)
        router_reached = return_value[0]
        router_started = return_value[1]
        to_be_removed = return_value[2]

        if (to_be_removed == 1):
            list_of_Area_1_triangles.remove(i) # so we do not have a permanent triangle stattioned on the last router
        if (router_reached != None):
            # this might recieve LSA 3 or LSA 1
            text_string = ""
            dictionary_text_string = ""
            if i.get_LSA_type() == 3:
                if seperate_lsa_3 == 1:
                    text_string = "Recieved LSA 3: area {} : {}".format(i.get_from_area(), i.get_lsa_3_starting_router())
                    dictionary_text_string = "{} Recieved LSA 3 from {} : {}".format(router_reached, i.get_from_area(), i.get_lsa_3_starting_router())
                else:
                    text_string = "Recieved LSA 3: area {}".format(i.get_from_area())
                    dictionary_text_string = "{} Recieved LSA 3 from {}".format(router_reached, i.get_from_area())
            elif i.get_LSA_type() == 4:
                text_string = "Recieved LSA 4: area {}".format(i.get_from_area())
                dictionary_text_string = "{} Recieved LSA 4 from {}".format(router_reached, i.get_from_area())
            else:
                text_string = "Recieved LSA 1: {}".format(router_started)
                dictionary_text_string = "{} Recieved LSA 1 from {}".format(router_reached, router_started)
            
            if (dictionary_text_string in text_dictionary_LSA_1):
                continue
            else:
                text_dictionary_LSA_1[dictionary_text_string] = 1

            # print(router_reached, router_started)
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
            elif router_reached == "ABR_1":
                list_text_position.append([text_string, (router_ABR_text[0], router_ABR_text[1])])
                router_ABR_text[router_ABR_text[2]] += increase_position
                # time to send an LSA 3 TO AREA 2
                initialize_LSA3_from_area_1_to_area_2(router_started)
            elif router_reached == "router_11: ABR_2":
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
            # print(list_text_position)
    for i in list_text_position:
        if "LSA 3" in i[0]:
            # represent it in a different color
            text = font.render(i[0], True, (255, 0, 0))
            screen.blit(text, (i[1][0], i[1][1]))
        elif "LSA 4" in i[0]:
            # represent it in a different color
            text = font.render(i[0], True, (0, 0, 255))
            screen.blit(text, (i[1][0], i[1][1]))
        else:
            text = font.render(i[0], True, (0, 0, 0))
            screen.blit(text, (i[1][0], i[1][1]))

    # our work in here is done and we can initiate the erasing process
    # all the triangles have reached their destinations: flooding complete
    if list_of_Area_1_triangles == []:
        return 1 # complete
    
    return 0 # in progress

def erase_text_area_1():
    global text_dictionary_LSA_1
    global list_text_position
    global list_of_Area_1_triangles

    text_dictionary_LSA_1 = {}
    list_text_position = []
    list_of_Area_1_triangles = []



########################################################################################################

def initialize_Area2_LSA():
    global router_7_text, router_8_text, router_9_text, router_10_text
    global router_ABR_text
    global router_11_text
    global list_text_position_area_2, text_dictionary_LSA_1_area_2
    global list_of_Area_2_triangles

    list_text_position_area_2 = []
    text_dictionary_LSA_1_area_2 = {}
    list_of_Area_2_triangles = []

    # ROUTER 7 LSA 1
    router_7_t1 = LSATriangles(area_2_travel_routes["router_7__TO__router_8"][0],
                               area_2_travel_routes["router_7__TO__router_8"][1],
                                router_7_color)
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
                                router_7_color)
    router_7_t2.enable_full_route([area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1]])
    router_7_t2.update_starting_router("router_7")
    router_7_t2.update_router_path_names(["router_10"])
    
    # ROUTER 8 LSA 1
    router_8_t1 = LSATriangles(area_2_travel_routes["router_8__TO__router_9"][0],
                               area_2_travel_routes["router_8__TO__router_9"][1],
                                router_8_color)
    router_8_t1.enable_full_route([area_2_travel_routes["router_8__TO__router_9"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1]])
    router_8_t1.update_starting_router("router_8")
    router_8_t1.update_router_path_names(["router_9", "router_10"])

    router_8_t2 = LSATriangles(area_2_travel_routes["router_7__TO__router_8"][1],
                               area_2_travel_routes["router_7__TO__router_8"][0],
                                router_8_color)
    router_8_t2.enable_full_route([area_2_travel_routes["router_7__TO__router_8"][1],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1]])
    router_8_t2.update_starting_router("router_8")
    router_8_t2.update_router_path_names(["router_7", "router_10"])


    # ROUTER 9 LSA 1
    router_9_t1 = LSATriangles(area_2_travel_routes["router_8__TO__router_9"][1],
                               area_2_travel_routes["router_8__TO__router_9"][0],
                                router_9_color)
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
                                router_9_color)
    router_9_t2.enable_full_route([area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1]])
    router_9_t2.update_starting_router("router_9")
    router_9_t2.update_router_path_names(["router_10"])

    # ROUTER 10 LSA 1
    router_10_t1 = LSATriangles(area_2_travel_routes["router_7__TO__router_10"][1],
                               area_2_travel_routes["router_7__TO__router_10"][0],
                                router_10_color)
    router_10_t1.enable_full_route([area_2_travel_routes["router_7__TO__router_10"][1],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][1]])
    router_10_t1.update_starting_router("router_10")
    router_10_t1.update_router_path_names(["router_7", "router_8"])

    router_10_t2 = LSATriangles(area_2_travel_routes["router_9__TO__router_10"][1],
                               area_2_travel_routes["router_9__TO__router_10"][0],
                                router_10_color)
    router_10_t2.enable_full_route([area_2_travel_routes["router_9__TO__router_10"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0]])
    router_10_t2.update_starting_router("router_10")
    router_10_t2.update_router_path_names(["router_9", "router_8"])


    list_of_Area_2_triangles.append(router_7_t1)
    list_of_Area_2_triangles.append(router_7_t2)
    list_of_Area_2_triangles.append(router_10_t1)
    list_of_Area_2_triangles.append(router_10_t2)
    list_of_Area_2_triangles.append(router_8_t1)
    list_of_Area_2_triangles.append(router_8_t2)
    list_of_Area_2_triangles.append(router_9_t1)
    list_of_Area_2_triangles.append(router_9_t2)
    

    # ADDING CODE SO OUT NEW ABR 1 ROUTER RECIEVES LSA 1 FROM AREA 2
    
    # FROM ROUTER 7 TO ABR 1
    router_7_t3 = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][0],
                               inter_area_routes["router_7__TO__router_abr1"][1],
                                router_7_color)
    router_7_t3.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][0],
                                inter_area_routes["router_7__TO__router_abr1"][1]])
    router_7_t3.update_starting_router("router_7")
    router_7_t3.update_router_path_names(["ABR_1"])

    # FROM ROUTER 8 TO ABR 1
    router_8_t3 = LSATriangles(area_2_travel_routes["router_7__TO__router_8"][1],
                               area_2_travel_routes["router_7__TO__router_8"][0],
                                router_8_color)
    router_8_t3.enable_full_route([area_2_travel_routes["router_7__TO__router_8"][1],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][1]])
    router_8_t3.update_starting_router("router_8")
    router_8_t3.update_router_path_names(["router_7", "ABR_1"])

    # FROM ROUTER 9 TO ABR 1
    router_9_t3 = LSATriangles(area_2_travel_routes["router_8__TO__router_9"][1],
                               area_2_travel_routes["router_8__TO__router_9"][0],
                                router_9_color)
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
                                router_10_color)
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
                                router_ABR1_color)
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
                                router_ABR1_color)
    router_ABR_t2.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][1],
                                    inter_area_routes["router_7__TO__router_abr1"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1]])
    router_ABR_t2.update_starting_router("ABR_1")
    router_ABR_t2.update_router_path_names(["router_7", "router_10"])

    list_of_Area_2_triangles.append(router_ABR_t1)
    list_of_Area_2_triangles.append(router_ABR_t2)

    # ABR 2 (ROUTER 11) should send LSA 1s inside Area 2 as well:
    router_11_t1 = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0],
                                router_11_color)
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
                                router_11_color)
    router_11_t2.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0]])
    router_11_t2.update_starting_router("router_11: ABR_2")
    router_11_t2.update_router_path_names(["router_10", "router_9", "router_8"])

    list_of_Area_2_triangles.append(router_11_t1)
    list_of_Area_2_triangles.append(router_11_t2)

    # FROM ABR 2 (Router 11) TO ABR 1:
    router_11_t3 = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0],
                                router_11_color)
    router_11_t3.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][1]])
    router_11_t3.update_starting_router("router_11: ABR_2")
    router_11_t3.update_router_path_names(["router_10", "router_7", "ABR_1"])

    list_of_Area_2_triangles.append(router_11_t3)

    # TODO (SanyaSriv): ALL THE ROUTERS IN AREA 2 MUST SEND THEIR LSA 1s to ROUTER 11: ABR_2
    # FROM ROUTER 7 TO ABR 2
    router_7_t4 = LSATriangles(area_2_travel_routes["router_7__TO__router_10"][0],
                                area_2_travel_routes["router_7__TO__router_10"][1],
                                router_7_color)
    router_7_t4.enable_full_route([area_2_travel_routes["router_7__TO__router_10"][0],
                                area_2_travel_routes["router_7__TO__router_10"][1],
                                inter_area_routes["router_10__TO__router_11"][0],
                                inter_area_routes["router_10__TO__router_11"][1]])
    router_7_t4.update_starting_router("router_7")
    router_7_t4.update_router_path_names(["router_10", "router_11: ABR_2"])

    # ROUTER 8 TO ABR 2
    router_8_t4 = LSATriangles(area_2_travel_routes["router_8__TO__router_9"][0],
                               area_2_travel_routes["router_8__TO__router_9"][1],
                                router_8_color)
    router_8_t4.enable_full_route([area_2_travel_routes["router_8__TO__router_9"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    inter_area_routes["router_10__TO__router_11"][1]])
    router_8_t4.update_starting_router("router_8")
    router_8_t4.update_router_path_names(["router_9", "router_10", "router_11: ABR_2"])

    # ROUTER 9 TO ABR 2
    router_9_t4 = LSATriangles(area_2_travel_routes["router_9__TO__router_10"][0],
                               area_2_travel_routes["router_9__TO__router_10"][1],
                                router_9_color)
    router_9_t4.enable_full_route([area_2_travel_routes["router_9__TO__router_10"][0],
                                area_2_travel_routes["router_9__TO__router_10"][1],
                                inter_area_routes["router_10__TO__router_11"][0],
                                inter_area_routes["router_10__TO__router_11"][1]])
    router_9_t4.update_starting_router("router_9")
    router_9_t4.update_router_path_names(["router_10", "router_11: ABR_2"])

    # ROUTER 10 TO ABR 2
    router_10_t4 = LSATriangles(inter_area_routes["router_10__TO__router_11"][0],
                                inter_area_routes["router_10__TO__router_11"][1],
                                router_10_color)
    router_10_t4.enable_full_route([inter_area_routes["router_10__TO__router_11"][0],
                                    inter_area_routes["router_10__TO__router_11"][1]])
    router_10_t4.update_starting_router("router_10")
    router_10_t4.update_router_path_names(["router_11: ABR_2"])

    # ABR 1 TO ABR 2
    router_ABR_t3 = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][1],
                                inter_area_routes["router_7__TO__router_abr1"][0],
                                router_ABR1_color)
    router_ABR_t3.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][1],
                                    inter_area_routes["router_7__TO__router_abr1"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    inter_area_routes["router_10__TO__router_11"][1]])
    router_ABR_t3.update_starting_router("ABR_1")
    router_ABR_t3.update_router_path_names(["router_7", "router_10", "router_11: ABR_2"])

    list_of_Area_2_triangles.append(router_7_t4)
    list_of_Area_2_triangles.append(router_8_t4)
    list_of_Area_2_triangles.append(router_9_t4)
    list_of_Area_2_triangles.append(router_10_t4)
    list_of_Area_2_triangles.append(router_ABR_t3)

def SendArea2LSA1(pygame, screen):
    
    global router_7_text, router_8_text, router_9_text, router_10_text
    global text_dictionary_LSA_1_area_2
    global list_text_position_area_2
    global global_counter
    global seperate_lsa_3

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
            if i.get_LSA_type() == 3:
                if seperate_lsa_3 == 1:
                    text_string = "Recieved LSA 3: area {} : {}".format(i.get_from_area(), i.get_lsa_3_starting_router())
                    dictionary_text_string = "{} Recieved LSA 3 from {} : {}".format(router_reached, i.get_from_area(), i.get_lsa_3_starting_router())
                else:
                    text_string = "Recieved LSA 3: area {}".format(i.get_from_area())
                    dictionary_text_string = "{} Recieved LSA 3 from {}".format(router_reached, i.get_from_area())
            else:
                text_string = "Recieved LSA 1: {}".format(router_started)
                dictionary_text_string = "{} Recieved LSA 1 from {}".format(router_reached, router_started)
            # text_string = "Recieved LSA 1: {}".format(router_started)
            # dictionary_text_string = "{} Recieved LSA 1 from {}".format(router_reached, router_started)
            
            if (dictionary_text_string in text_dictionary_LSA_1_area_2):
                continue
            else:
                text_dictionary_LSA_1_area_2[dictionary_text_string] = 1
            
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
                # this would mean that we now need to send LSA3 in area 1
                print("TYPE IN HERE IS: ")
                if (i.get_LSA_type() == 0):
                    # only send out LSA 3 if this is an lsa 1
                    initialize_LSA3_from_area_2_to_area_1(router_started)
                    if (router_started == "router_7"):
                        # THE ASBR sent it: so we also need to send LSA4
                        send_LSA_4_from_area_2_to_area_1(router_started)
            elif router_reached == "router_11: ABR_2":
                # this would mean that we now need to send LSA3 in area 1
                list_text_position_area_2.append([text_string, (router_11_text[0], router_11_text[1])])
                router_11_text[router_11_text[2]] -= increase_position
                initialize_LSA3_from_area_2_to_area_3(router_started)
                # this would mean that we now need to send LSA3 in area 3 (stubby area)
            elif router_reached == "router_12":
                print("ROUTER 2 REACHED")
                list_text_position_area_2.append([text_string, (router_12_text[0], router_12_text[1])])
                router_12_text[1] -= increase_position
            elif router_reached == "router_13":
                list_text_position_area_2.append([text_string, (router_13_text[0], router_13_text[1])])
                router_13_text[1] -= increase_position
            elif router_reached == "router_14":
                list_text_position_area_2.append([text_string, (router_14_text[0], router_14_text[1])])
                router_14_text[1] += increase_position

    for i in list_text_position_area_2:
        if "LSA 3" in i[0]:
            # represent it in a different color
            text = font.render(i[0], True, (255, 0, 0))
            screen.blit(text, (i[1][0], i[1][1]))
        else:
            text = font.render(i[0], True, (0, 0, 0))
            screen.blit(text, (i[1][0], i[1][1]))

    if list_of_Area_2_triangles == []:
        return 1 # complete
    
    return 0 # in progress


def erase_text_area_2():
    global text_dictionary_LSA_1_area_2
    global list_text_position_area_2
    global list_of_Area_2_triangles

    list_of_Area_2_triangles = []
    text_dictionary_LSA_1_area_2 = {}
    list_text_position_area_2 = []


def initialize_LSA3_from_area_2_to_area_1(starting_router):
    global global_counter
    global list_of_Area_1_triangles

    name_of_lsa = "area_1_lsa_3" + str(global_counter)
    global_counter += 1
    print("name_of_lsa = ", name_of_lsa)
    name_of_lsa = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0], 
                    inter_area_routes["router_2__TO__router_abr1"][1], 
                    router_ABR1_color)
    name_of_lsa.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_2__TO__router_6"][0],
                                    area_1_travel_routes["router_2__TO__router_6"][1]])
    name_of_lsa.update_starting_router("ABR_1")
    name_of_lsa.update_router_path_names(["router_2", "router_6"])
    # LSA 3 from area 2 to area 1
    name_of_lsa.set_LSA_type(3, 2, 1, starting_router)
    list_of_Area_1_triangles.append(name_of_lsa)

    name_of_lsa = "area_1_lsa_3" + str(global_counter)
    global_counter += 1
    print("name_of_lsa = ", name_of_lsa)
    name_of_lsa = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0], 
                                inter_area_routes["router_2__TO__router_abr1"][1], 
                                router_ABR1_color)
    name_of_lsa.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    name_of_lsa.update_starting_router("ABR_1")
    name_of_lsa.update_router_path_names(["router_2", "router_5", "router_1"])
    # LSA 3 from area 2 to area 1
    name_of_lsa.set_LSA_type(3, 2, 1, starting_router)
    list_of_Area_1_triangles.append(name_of_lsa)

    name_of_lsa = "area_1_lsa_3" + str(global_counter)
    global_counter += 1
    name_of_lsa = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0], 
                                inter_area_routes["router_2__TO__router_abr1"][1], 
                                router_ABR1_color)
    name_of_lsa.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                    area_1_travel_routes["router_4__TO__router_3"][1],
                                    area_1_travel_routes["router_4__TO__router_3"][0]])
    
    name_of_lsa.update_starting_router("ABR_1")
    name_of_lsa.update_router_path_names(["router_2", "router_5", "router_4", "router_3"])
    # LSA 3 from area 2 to area 1
    name_of_lsa.set_LSA_type(3, 2, 1, starting_router)
    list_of_Area_1_triangles.append(name_of_lsa)


def initialize_LSA3_from_area_1_to_area_2(starting_router):
    # ROUTER 2 LSA 3 --> only sent out by the boundary router
    global global_counter

    name_of_lsa = "area_2_lsa_3" + str(global_counter)
    global_counter += 1
    name_of_lsa = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][1], 
                                inter_area_routes["router_7__TO__router_abr1"][0], 
                                router_ABR1_color)
    name_of_lsa.enable_full_route([inter_area_routes["router_2__TO__router_7"][0], 
                                    inter_area_routes["router_2__TO__router_7"][1],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1]])
    name_of_lsa.update_starting_router("ABR_1")
    name_of_lsa.update_router_path_names(["router_7", "router_8", "router_9", "router_10"])
    name_of_lsa.set_LSA_type(3, 1, 2, starting_router)
    list_of_Area_2_triangles.append(name_of_lsa)
    
    name_of_lsa = "area_2_lsa_3" + str(global_counter)
    global_counter += 1
    name_of_lsa = LSATriangles(inter_area_routes["router_7__TO__router_abr1"][1], 
                                inter_area_routes["router_7__TO__router_abr1"][0], 
                                router_ABR1_color)
    name_of_lsa.enable_full_route([inter_area_routes["router_7__TO__router_abr1"][1], 
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
    name_of_lsa.update_starting_router("ABR_1")
    name_of_lsa.update_router_path_names(["router_7", "router_10", "router_11: ABR_2", "router_13", "router_14", "router_12"])
    name_of_lsa.set_LSA_type(3, 1, 2, starting_router)
    list_of_Area_2_triangles.append(name_of_lsa)
    

def initialize_Area3_LSA():
    global router_11_text, router_12_text, router_13_text, router_14_text
    global list_text_position_area_3, text_dictionary_LSA_1_area_3
    global list_of_Area_3_triangles

    # initialize all the text positions
    router_11_text = [950, 245, 1]
    router_12_text = [1030, 385, 1]
    router_13_text = [1220, 245, 1]
    router_14_text = [1220, 455, 1]

    list_of_Area_3_triangles = []
    list_text_position_area_3 = []
    text_dictionary_LSA_1_area_3 = {}

    # ROUTER 11 LSA 1
    router_11_t1 = LSATriangles(area_3_travel_routes["router_11__TO__router_13"][0],
                               area_3_travel_routes["router_11__TO__router_13"][1],
                                router_11_color)
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
                                router_12_color)
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
                                router_13_color)
    router_13_t1.enable_full_route([area_3_travel_routes["router_11__TO__router_13"][1],
                                    area_3_travel_routes["router_11__TO__router_13"][0]])
    router_13_t1.update_starting_router("router_13")
    router_13_t1.update_router_path_names(["router_11"])

    router_13_t2 = LSATriangles(area_3_travel_routes["router_13__TO__router_14"][0],
                               area_3_travel_routes["router_13__TO__router_14"][1],
                                router_13_color)
    router_13_t2.enable_full_route([area_3_travel_routes["router_13__TO__router_14"][0],
                                    area_3_travel_routes["router_13__TO__router_14"][1],
                                    area_3_travel_routes["router_14__TO__router_12"][0],
                                    area_3_travel_routes["router_14__TO__router_12"][1]])
    router_13_t2.update_starting_router("router_13")
    router_13_t2.update_router_path_names(["router_14", "router_12"])

    # ROUTER 14 LSA 1
    router_14_t1 = LSATriangles(area_3_travel_routes["router_14__TO__router_12"][0],
                                area_3_travel_routes["router_14__TO__router_12"][1],
                                router_14_color)
    router_14_t1.enable_full_route([area_3_travel_routes["router_14__TO__router_12"][0],
                                    area_3_travel_routes["router_14__TO__router_12"][1]])
    router_14_t1.update_starting_router("router_14")
    router_14_t1.update_router_path_names(["router_12"])

    router_14_t2 = LSATriangles(area_3_travel_routes["router_13__TO__router_14"][1],
                                area_3_travel_routes["router_13__TO__router_14"][0],
                                router_14_color)
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
            if i.get_LSA_type() == 3:
                if seperate_lsa_3 == 1:
                    text_string = "Recieved LSA 3: area {} : {}".format(i.get_from_area(), i.get_lsa_3_starting_router())
                    dictionary_text_string = "{} Recieved LSA 3 from {} : {}".format(router_reached, i.get_from_area(), i.get_lsa_3_starting_router())
                else:
                    text_string = "Recieved LSA 3: area {}".format(i.get_from_area())
                    dictionary_text_string = "{} Recieved LSA 3 from {}".format(router_reached, i.get_from_area())
            else:
                text_string = "Recieved LSA 1: {}".format(router_started)
                dictionary_text_string = "{} Recieved LSA 1 from {}".format(router_reached, router_started)
            
            if (dictionary_text_string in text_dictionary_LSA_1_area_3):
                continue
            else:
                text_dictionary_LSA_1_area_3[dictionary_text_string] = 1

            if router_reached == "router_11":
                list_text_position_area_3.append([text_string, (router_11_text[0], router_11_text[1])])
                router_11_text[1] -= increase_position
                # SEND OUT LSA 3S BECAUSE THIS IS AN ABR
                initialize_LSA3_from_area_3_to_area_2(router_started)
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


def initialize_LSA3_from_area_2_to_area_3(router_started):
    global global_counter

    name_of_lsa = "area_3_lsa_3" + str(global_counter)
    global_counter += 1
    name_of_lsa = LSATriangles(area_3_travel_routes["router_11__TO__router_13"][0],
                                area_3_travel_routes["router_11__TO__router_13"][1],
                                router_11_color)
    name_of_lsa.enable_full_route([area_3_travel_routes["router_11__TO__router_13"][0],
                                    area_3_travel_routes["router_11__TO__router_13"][1],
                                    area_3_travel_routes["router_13__TO__router_14"][0],
                                    area_3_travel_routes["router_13__TO__router_14"][1],
                                    area_3_travel_routes["router_14__TO__router_12"][0],
                                    area_3_travel_routes["router_14__TO__router_12"][1]])
    name_of_lsa.update_starting_router("router_11: ABR_2")
    name_of_lsa.update_router_path_names(["router_13", "router_14", "router_12"])
    name_of_lsa.set_LSA_type(3, 2, 3, router_started)
    list_of_Area_2_triangles.append(name_of_lsa)

def initialize_LSA3_from_area_3_to_area_2(router_started):
    global global_counter
    global list_of_Area_2_triangles

    name_of_lsa = "area_2_lsa_3" + str(global_counter)
    global_counter += 1
    name_of_lsa = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0], 
                                (237, 234, 57))
    name_of_lsa.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][0],
                                    area_2_travel_routes["router_7__TO__router_8"][1]])
    name_of_lsa.update_starting_router("router_11: ABR_2")
    name_of_lsa.update_router_path_names(["router_10", "router_7", "router_8"])
    name_of_lsa.set_LSA_type(3, 3, 2, router_started)
    list_of_Area_2_triangles.append(name_of_lsa)

    name_of_lsa = "area_2_lsa_3" + str(global_counter)
    global_counter += 1
    name_of_lsa = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0], 
                                (237, 234, 57))
    name_of_lsa.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    area_2_travel_routes["router_9__TO__router_10"][1],
                                    area_2_travel_routes["router_9__TO__router_10"][0],
                                    area_2_travel_routes["router_8__TO__router_9"][1],
                                    area_2_travel_routes["router_8__TO__router_9"][0]])
    name_of_lsa.update_starting_router("router_11: ABR_2")
    name_of_lsa.update_router_path_names(["router_10", "router_9", "router_8"])
    name_of_lsa.set_LSA_type(3, 3, 2, router_started)
    list_of_Area_2_triangles.append(name_of_lsa)

    name_of_lsa = "area_2_lsa_3" + str(global_counter)
    global_counter += 1
    name_of_lsa = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0],
                                (237, 234, 57))
    name_of_lsa.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
                                    inter_area_routes["router_10__TO__router_11"][0],
                                    area_2_travel_routes["router_7__TO__router_10"][1],
                                    area_2_travel_routes["router_7__TO__router_10"][0],
                                    inter_area_routes["router_7__TO__router_abr1"][0], 
                                    inter_area_routes["router_7__TO__router_abr1"][1], 
                                    inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1], 
                                    area_1_travel_routes["router_2__TO__router_6"][0],
                                    area_1_travel_routes["router_2__TO__router_6"][1]])
    name_of_lsa.update_starting_router("router_11: ABR_2")
    name_of_lsa.update_router_path_names(["router_10", "router_7", "ABR_1", "router_2", "router_6"])
    name_of_lsa.set_LSA_type(3, 3, 1, router_started)
    list_of_Area_2_triangles.append(name_of_lsa)

    name_of_lsa = "area_2_lsa_3" + str(global_counter)
    global_counter += 1
    name_of_lsa = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0],
                                (237, 234, 57))
    name_of_lsa.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
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
    name_of_lsa.update_starting_router("router_11: ABR_2")
    name_of_lsa.update_router_path_names(["router_10", "router_7", "ABR_1", "router_2", "router_5", "router_1"])
    name_of_lsa.set_LSA_type(3, 3, 1, router_started)
    list_of_Area_2_triangles.append(name_of_lsa)

    name_of_lsa = "area_2_lsa_3" + str(global_counter)
    global_counter += 1
    name_of_lsa = LSATriangles(inter_area_routes["router_10__TO__router_11"][1],
                                inter_area_routes["router_10__TO__router_11"][0],
                                (237, 234, 57))
    name_of_lsa.enable_full_route([inter_area_routes["router_10__TO__router_11"][1],
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
    
    name_of_lsa.update_starting_router("router_11: ABR_2")
    name_of_lsa.update_router_path_names(["router_10", "router_7", "ABR_1", "router_2", "router_5", "router_4", "router_3"])
    name_of_lsa.set_LSA_type(3, 3, 1, router_started)
    list_of_Area_2_triangles.append(name_of_lsa)

def send_LSA_4_from_area_2_to_area_1(starting_router):
    global global_counter
    global list_of_Area_1_triangles

    name_of_lsa = "area_1_lsa_4" + str(global_counter)
    global_counter += 1
    print("name_of_lsa = ", name_of_lsa)
    name_of_lsa = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0], 
                    inter_area_routes["router_2__TO__router_abr1"][1], 
                    router_7_color)
    name_of_lsa.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_2__TO__router_6"][0],
                                    area_1_travel_routes["router_2__TO__router_6"][1]])
    name_of_lsa.update_starting_router("ABR_1")
    name_of_lsa.update_router_path_names(["router_2", "router_6"])
    # LSA 3 from area 2 to area 1
    name_of_lsa.set_LSA_type(4, 2, 1, starting_router)
    list_of_Area_1_triangles.append(name_of_lsa)

    name_of_lsa = "area_1_lsa_4" + str(global_counter)
    global_counter += 1
    print("name_of_lsa = ", name_of_lsa)
    name_of_lsa = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0], 
                                inter_area_routes["router_2__TO__router_abr1"][1], 
                                router_7_color)
    name_of_lsa.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    name_of_lsa.update_starting_router("ABR_1")
    name_of_lsa.update_router_path_names(["router_2", "router_5", "router_1"])
    # LSA 3 from area 2 to area 1
    name_of_lsa.set_LSA_type(4, 2, 1, starting_router)
    list_of_Area_1_triangles.append(name_of_lsa)

    name_of_lsa = "area_1_lsa_4" + str(global_counter)
    global_counter += 1
    name_of_lsa = LSATriangles(inter_area_routes["router_2__TO__router_abr1"][0], 
                                inter_area_routes["router_2__TO__router_abr1"][1], 
                                router_7_color)
    name_of_lsa.enable_full_route([inter_area_routes["router_2__TO__router_abr1"][0], 
                                    inter_area_routes["router_2__TO__router_abr1"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                    area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                    area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                    area_1_travel_routes["router_4__TO__router_3"][1],
                                    area_1_travel_routes["router_4__TO__router_3"][0]])
    
    name_of_lsa.update_starting_router("ABR_1")
    name_of_lsa.update_router_path_names(["router_2", "router_5", "router_4", "router_3"])
    # LSA 3 from area 2 to area 1
    name_of_lsa.set_LSA_type(4, 2, 1, starting_router)
    list_of_Area_1_triangles.append(name_of_lsa)


def initialise_LSA_5():
    # ROUTER 7 LSA 3 --> only sent out by the boundary router
    name_of_lsa = "area_1_lsa_4" + str(global_counter)
    global_counter += 1
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
    
    name_of_lsa = "area_1_lsa_4" + str(global_counter)
    global_counter += 1
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

    name_of_lsa = "area_1_lsa_4" + str(global_counter)
    global_counter += 1
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

    name_of_lsa = "area_1_lsa_4" + str(global_counter)
    global_counter += 1
    router_7_t5 = LSATriangles(area_2_travel_routes["router_7__TO__router_10"][0],
                                area_2_travel_routes["router_7__TO__router_10"][1],
                                (117, 227, 104))
    router_7_t5.enable_full_route([area_2_travel_routes["router_7__TO__router_10"][0],
                                   area_2_travel_routes["router_7__TO__router_10"][1],
                                   area_2_travel_routes["router_9__TO__router_10"][1],
                                   area_2_travel_routes["router_9__TO__router_10"][0]])
    router_7_t5.update_starting_router("router_7")
    router_7_t5.update_router_path_names(["router_10", "router_9"])

    name_of_lsa = "area_1_lsa_4" + str(global_counter)
    global_counter += 1
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
