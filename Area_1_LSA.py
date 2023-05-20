import math
import global_variables_file
from LSA_Class import LSATriangles
from global_variables_file import *

list_of_Area_1_triangles = []

def initialize_Area1_LSA():
    # ROUTER 1 LSA 1
    router_1_t1 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_1"][0], 
                                            area_1_travel_routes["router_5_area_1__TO__router_1"][1], 
                                            (137, 25, 181))
    router_1_t1.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_1"][0],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                                area_1_travel_routes["router_2__TO__router_6"][0],
                                                area_1_travel_routes["router_2__TO__router_6"][1]])
    
    router_1_t2 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_1"][0], 
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][1], 
                                                (137, 25, 181))
    router_1_t2.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_1"][0],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                                area_1_travel_routes["router_4__TO__router_3"][1],
                                                area_1_travel_routes["router_4__TO__router_3"][0]])
    
    list_of_Area_1_triangles.append(router_1_t1)
    list_of_Area_1_triangles.append(router_1_t2)

    # ROUTER 2 LSA 1
    router_2_t1 = LSATriangles(area_1_travel_routes["router_2__TO__router_6"][0], 
                                            area_1_travel_routes["router_2__TO__router_6"][1], 
                                            (181, 121, 25))
    router_2_t1.enable_full_route([area_1_travel_routes["router_2__TO__router_6"][0],
                                                area_1_travel_routes["router_2__TO__router_6"][1]])
    
    router_2_t2 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_2"][0], 
                                            area_1_travel_routes["router_5_area_1__TO__router_2"][1], 
                                            (181, 121, 25))
    router_2_t2.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    
    router_2_t3 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_2"][0], 
                                            area_1_travel_routes["router_5_area_1__TO__router_2"][1], 
                                            (181, 121, 25))
    router_2_t3.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                                area_1_travel_routes["router_4__TO__router_3"][1],
                                                area_1_travel_routes["router_4__TO__router_3"][0]])
    
    list_of_Area_1_triangles.append(router_2_t1)
    list_of_Area_1_triangles.append(router_2_t2)
    list_of_Area_1_triangles.append(router_2_t3)


    # ROUTER 5 LSA 1
    router_5_t1 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_1"][1], 
                                            area_1_travel_routes["router_5_area_1__TO__router_1"][0], 
                                            (50, 166, 168))
    router_5_t1.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_1"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_1"][0]])
    
    router_5_t2 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_4"][1], 
                                            area_1_travel_routes["router_5_area_1__TO__router_4"][0], 
                                            (50, 166, 168))
    router_5_t2.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_4"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_4"][0],
                                                area_1_travel_routes["router_4__TO__router_3"][1],
                                                area_1_travel_routes["router_4__TO__router_3"][0]])
    
    router_5_t3 = LSATriangles(area_1_travel_routes["router_5_area_1__TO__router_2"][1], 
                                            area_1_travel_routes["router_5_area_1__TO__router_2"][0], 
                                            (50, 166, 168))
    router_5_t3.enable_full_route([area_1_travel_routes["router_5_area_1__TO__router_2"][1],
                                                area_1_travel_routes["router_5_area_1__TO__router_2"][0],
                                                area_1_travel_routes["router_2__TO__router_6"][0],
                                                area_1_travel_routes["router_2__TO__router_6"][1]])

    list_of_Area_1_triangles.append(router_5_t1)
    list_of_Area_1_triangles.append(router_5_t2)
    list_of_Area_1_triangles.append(router_5_t3)


def SendArea1LSA1(pygame, screen):
    
    for i in list_of_Area_1_triangles:
        i.draw(pygame, screen)
        i.move_triangle()