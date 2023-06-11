
size = (1400, 700)
triangle_pos = (0,0)
triangle_target = (0,0)
tiangle_list = []
line = 0

# Parameters for Animation buttons
button_width = 100
button_height = 30
button_color = (255, 0, 0)

button_LSA_1_pos = (20, 20)
button_LSA_1_refresh = (130, 20)

button_LSA_3_pos = (20, 70)
button_LSA_3_refresh = (130, 70)

button_LSA_4_pos = (240, 20)
button_LSA_4_refresh = (350, 20)

button_LSA_5_pos = (240, 70)
button_LSA_5_refresh = (350, 70)

master_button_width = 150
master_button_color = (217, 215, 98)
master_simulator = (20, 120)
master_simulator_refresh = (190, 120)

button_display_seperate_lsa_3 = (1010, 20)
seperate_lsa_3_width = 150

button_clearing_texts = (1020, 80)

# For sliders
slider_width = 70
slider_height = 20
slider_handle_width = 9
slider_position = (280, 20)
speed_slider_min_value = 0
speed_slider_max_value = 150
speed_slider_current_value = 50


# Router and Switch
box_size = 80
switch_size = 50
padding = 20
border_width = 5
box_pos = (padding, padding)
router_radius = 30

# POsition of Area 1 routers
router_1_pos = (195, 250)
router_2_pos = (355, 375)
# router_2_pos = (455, 270)
router_3_pos = (65, 500)
router_4_pos = (65, 375)
router_5_pos_area_1 = (195, 375)
router_6_pos_area_1 = (355, 500)

area_1_travel_routes = {}
area_2_travel_routes = {}
area_3_travel_routes = {}
inter_area_routes = {}

# Position of all the area boundaries
area_1_pos = (20, 200)
area_2_pos = (450, 100) # backbone area
area_3_pos = (945, 230) # area 3
area_4_pos = (1010, 420) # area 4

# Position of all Area 2 Routers (There would be 3 routers (I am thinking))
router_7_pos = (610, 150)
router_8_pos = (610, 290)
router_9_pos = (610,430)
router_10_pos = (740, 290)

# Position of all Area 3 Routers and switches
router_11_pos = (950, 290)
router_12_pos = (1070, 425)
router_13_pos = (1270, 290)
router_14_pos = (1270, 425)
switch_3_pos = (1225, 275)

# Position of all Area 4 Routers and switches
router_15_pos = (1070, 470)
router_16_pos = (1200, 600)
router_17_pos = (1200, 470)
router_18_pos = (1320, 600)

# making some ABRs:
router_abr_1 = (455, 245)

# making the ASBR
router_isp_pos = (750, 60)


switch_4_pos = (1295, 445)

# Position of inter-area switch (I will build it in area 2 functions for now)
switch_5_pos = (850, 265)

# List of all LSAs here (as of now I am planning to represent it by a triangle)
area_1_LSA_1 = []


router_1_color = (137, 25, 181)
router_2_color = (181, 121, 25)
router_3_color = (32, 158, 3)
router_4_color = (219, 15, 43)
router_5_color = (50, 166, 168)
router_6_color = (237, 222, 9)
router_ABR1_color = (79, 24, 68)

router_7_color = (137, 25, 181)
router_8_color = (181, 121, 25)
router_9_color = (32, 158, 3)
router_10_color = (219, 15, 43)
router_11_color = (242, 154, 87)

router_12_color = (17, 125, 181)
router_13_color = (32, 158, 3)
router_14_color = (32, 15, 73)

# distinct colors
# router_1_color = (173, 216, 230)
# router_2_color = (0, 0, 139)
# router_3_color = (0, 255, 255)
# router_4_color = (0, 0, 128)
# router_5_color = (135, 206, 235)
# router_6_color = (65, 105, 225)
# router_ABR1_color = (138, 43, 226)
# router_7_color = (0, 255, 0)
# router_8_color = (34, 139, 34)
# router_9_color = (152, 255, 152)
# router_10_color = (128, 128, 0)
# router_11_color = (242, 154, 87)
# router_12_color =  (218, 165, 32)
# router_13_color = (255, 219, 88)
# router_14_color = (255, 191, 0)

