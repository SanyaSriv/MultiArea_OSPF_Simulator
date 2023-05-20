import math

class LSATriangles:
    def __init__(self, position, target, color):
        self.position = position
        self.target = target
        self.color = color
        self.speed = 5
        self.size = 10

        # the triangle should follow this route
        self.full_route = []
        self.current_start = 0
        self.current_end = 1

    def enable_full_route(self, route):
        self.full_route = route

    def move_triangle(self):
        dx = self.target[0] - self.position[0]
        dy = self.target[1] - self.position[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        direction = (dx / distance, dy / distance)
    
        # Update triangle position
        if distance > self.speed:
            self.position = (
                self.position[0] + direction[0] * self.speed,
                self.position[1] + direction[1] * self.speed
        )
        else:
            # update the line travelled on
            if (self.current_end == len(self.full_route) - 1):
                return 1 # nothing more to do, we have finished our work
            self.current_start += 2
            self.current_end += 2
            self.update_position(self.full_route[self.current_start], self.full_route[self.current_end])

    def draw(self, pygame, screen):
        pygame.draw.polygon(
            screen, (0, 0, 0),
            [(self.position[0], self.position[1] - self.size),
             (self.position[0] + self.size, self.position[1]),
             (self.position[0], self.position[1] + self.size)]
        )

    def update_position(self, new_position, new_target):
        self.target = new_target
        self.position = new_position

