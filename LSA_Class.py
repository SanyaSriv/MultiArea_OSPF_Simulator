import math

class LSATriangles:
    shared_speed = 5

    def __init__(self, position, target, color):
        self.position = position
        self.target = target
        self.color = color
        self.speed = LSATriangles.shared_speed
        self.size = 12
        self.starting_router = None
        self.router_path_names = []
        self.hop_count_number = 0

        # the triangle should follow this route
        self.full_route = []
        self.current_start = 0
        self.current_end = 1

        # which LSA type is this
        self.LSA_type = 0
        self.from_area = ""
        self.to_area = ""
        self.LSA_3_start = ""

    def enable_full_route(self, route):
        self.full_route = route

    def move_triangle(self, pygame, screen):
        dx = self.target[0] - self.position[0]
        dy = self.target[1] - self.position[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        direction = (dx / distance, dy / distance)

        to_ret = None
        # Update triangle position
        if distance > self.speed:
            self.position = (
                self.position[0] + direction[0] * self.speed,
                self.position[1] + direction[1] * self.speed
        )
        else:
            to_ret = self.router_path_names[self.hop_count_number] 
            self.hop_count_number += 1 # we switch paths

            if (self.current_end == len(self.full_route) - 1):
                return (to_ret, self.starting_router, 1) # nothing more to do, we have finished our work
            self.current_start += 2
            self.current_end += 2
            self.update_position(self.full_route[self.current_start], self.full_route[self.current_end])

        return (to_ret, self.starting_router, 0)
    
    def draw(self, pygame, screen):
        pygame.draw.polygon(
            screen, self.color,
            [(self.position[0], self.position[1] - self.size),
             (self.position[0] + self.size, self.position[1]),
             (self.position[0], self.position[1] + self.size)]
        )

    def update_position(self, new_position, new_target):
        self.target = new_target
        self.position = new_position

    def update_starting_router(self, start_router_name):
        self.starting_router = start_router_name

    def update_router_path_names(self, router_hop_name_list):
        self.router_path_names = router_hop_name_list

    def change_speed(self, new_speed):
        LSATriangles.shared_speed = new_speed

    def set_LSA_type(self, ty, from_area, to_area, start):
        self.LSA_type = ty
        self.to_area = to_area
        self.from_area = from_area
        self.LSA_3_start = start
    
    def get_LSA_type(self):
        return int(self.LSA_type)
    
    def get_from_area(self):
        return str(self.from_area)
    
    def get_to_area(self):
        return str(self.to_area)
    
    def get_lsa_3_starting_router(self):
        return str(self.LSA_3_start)