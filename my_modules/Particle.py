import math

class Particle:
    def __init__(self, model, x, y, speed, direction, color, collision_distance, attraction_strength, repulsion_strength, repulsion_distance):
        self.model = model

        self.width = model.x_lim
        self.height = model.y_lim

        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.color = color
        self.collision_distance = collision_distance
        self.attraction_strength = attraction_strength
        self.repulsion_strength = repulsion_strength
        self.repulsion_distance = repulsion_distance

    def update_parameters(self):
        # Used for updating parameters, after user changes the slider.
        self.speed = self.model.speed
        self.repulsion_distance = self.model.repulsion_distance
        self.repulsion_strength = self.model.repulsion_strength

    def update(self, particles):
        # Update position based on speed and direction
        self.x += math.cos(self.direction) * self.speed
        self.y += math.sin(self.direction) * self.speed

        # Attraction and repulsion
        for particle in particles:
            if particle != self:
                distance = self.distance_to(particle)
                if distance < self.repulsion_distance:
                    # Repulsion
                    repulsion_direction = math.atan2(self.y - particle.y, self.x - particle.x)
                    self.x += math.cos(repulsion_direction) * self.repulsion_strength
                    self.y += math.sin(repulsion_direction) * self.repulsion_strength
                else:
                    # Attraction
                    attraction_direction = math.atan2(particle.y - self.y, particle.x - self.x)
                    self.x += math.cos(attraction_direction) * self.attraction_strength
                    self.y += math.sin(attraction_direction) * self.attraction_strength

        # Check for collisions with other particles and bounce
        # for particle in particles:
        #     if particle != self and self.distance_to(particle) < self.collision_distance:
        #         self.direction = (self.direction + math.pi) % (2 * math.pi)

        # Wall collision
        # If particle hits the right wall or left wall
        if self.x <= self.width[0]:
            self.x = self.width[0]  # Adjust position
            self.direction = math.pi - self.direction
        elif self.x >= self.width[1]:
            self.x = self.width[1]  # Adjust position
            self.direction = math.pi - self.direction

            # If particle hits the top wall or bottom wall
        if self.y <= self.height[0]:
            self.y = self.height[0]  # Adjust position
            self.direction = -self.direction
        elif self.y >= self.height[1]:
            self.y = self.height[1]  # Adjust position
            self.direction = -self.direction

    def distance_to(self, other_particle):
        dx = self.x - other_particle.x
        dy = self.y - other_particle.y
        return math.sqrt(dx**2 + dy**2)
