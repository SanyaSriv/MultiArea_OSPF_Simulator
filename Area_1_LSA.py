import math
import global_variables_file
from LSA_Class import LSATriangles
from global_variables_file import *

list_of_Area_1_triangles = []

# third parameter: which index to increase
router_1_text = [0,0,0]
router_2_text = [0,0,0]
router_3_text = [0,0,0]
router_4_text = [0,0,0]
router_5_text = [0,0,0]
router_6_text = [0,0,0]
router_ABR_text = [0,0,0]

increase_position = 10
text_dictionary_LSA_1 = {}
list_text_position = []

def initialize_Area1_LSA():
    global router_1_text, router_2_text, router_3_text, router_4_text, router_5_text, router_6_text
    global router_ABR_text
    global list_text_position, text_dictionary_LSA_1
    global list_of_Area_1_triangles

    # initialize all the text positions
    router_1_text = [220, 250, 1]
    router_2_text = [405, 375, 1]
    router_3_text = [35, 530, 1]
    router_4_text = [35, 330, 1]
    router_5_text = [175, 410, 1]
    router_6_text = [325, 530, 1]
    router_ABR_text = [350, 200, 1]

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
            text_string = "Received LSA 1: {}".format(router_started)
            dictionary_text_string = "{} Received LSA 1 from {}".format(router_reached, router_started)
            
            if (dictionary_text_string in text_dictionary_LSA_1):
                continue
            else:
                text_dictionary_LSA_1[dictionary_text_string] = 1

            
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
                router_ABR_text[router_ABR_text[2]] -= increase_position

    for i in list_text_position:
        text = font.render(i[0], True, (0, 0, 0))
        screen.blit(text, (i[1][0], i[1][1]))

    # our work in here is done and we can initiate the erasing process
    # all the triangles have reached their destinations: flooding complete
    if list_of_Area_1_triangles == []:
        return 1 # complete
    
    return 0 # in progress

def erase_text():
    global text_dictionary_LSA_1
    global list_text_position
    global list_of_Area_1_triangles

    text_dictionary_LSA_1 = {}
    list_text_position = []
    list_of_Area_1_triangles = []
