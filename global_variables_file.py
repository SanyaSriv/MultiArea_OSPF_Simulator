
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

button_LSA_4_pos = (260, 20)
button_LSA_4_refresh = (370, 20)

master_button_width = 150
master_button_color = (217, 215, 98)
master_simulator = (20, 120)
master_simulator_refresh = (190, 120)

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
area_2_pos = (550, 100) # backbone area
area_3_pos = (1010, 100) # area 3
area_4_pos = (1010, 420) # area 4

# Position of all Area 2 Routers (There would be 3 routers (I am thinking))
router_7_pos = (610, 150)
router_8_pos = (610, 290)
router_9_pos = (610,430)
router_10_pos = (740, 290)

# Position of all Area 3 Routers and switches
router_11_pos = (1070, 150)
router_12_pos = (1070, 300)
router_13_pos = (1270, 150)
router_14_pos = (1270, 300)
switch_3_pos = (1225, 275)

# Position of all Area 4 Routers and switches
router_15_pos = (1070, 470)
router_16_pos = (1200, 600)
router_17_pos = (1200, 470)
router_18_pos = (1320, 600)

# making the ASBR
router_isp_pos = (750, 60)


switch_4_pos = (1295, 445)

# Position of inter-area switch (I will build it in area 2 functions for now)
switch_5_pos = (850, 265)

# List of all LSAs here (as of now I am planning to represent it by a triangle)
area_1_LSA_1 = []
