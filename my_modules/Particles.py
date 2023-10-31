import math
import random


class Particles:
    def __init__(self, x_positions, y_positions, speed, model, color):
        self.model = model
        self.x_positions = x_positions
        self.y_positions = y_positions
        self.speed = speed
        self.color = color

    def distance_and_direction(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        dist = math.sqrt(dx ** 2 + dy ** 2)
        return dist, dx, dy

    def update_positions(self):
        self.speed = self.model.speed
        force_strength = self.model.force_strength # Adjust this value to control the strength of the force
        repulsion_distance = self.model.repulsion_distance  # Distance at which particles start repelling each other

        # Initialize force accumulators
        forces_x = [0] * len(self.x_positions)
        forces_y = [0] * len(self.y_positions)

        # Calculate forces between particles
        for i in range(len(self.x_positions)):
            for j in range(i + 1, len(self.x_positions)):
                dist, dx, dy = self.distance_and_direction(self.x_positions[i], self.y_positions[i],
                                                           self.x_positions[j], self.y_positions[j])
                if dist > 0:
                    force_magnitude = -force_strength if dist < repulsion_distance else force_strength
                    force_x = force_magnitude * dx / dist
                    force_y = force_magnitude * dy / dist

                    forces_x[i] += force_x
                    forces_y[i] += force_y
                    forces_x[j] -= force_x  # Apply opposite force on the other particle
                    forces_y[j] -= force_y

        # Update positions based on forces and random movement
        for i in range(len(self.x_positions)):
            self.x_positions[i] += (random.random() - 0.5) * self.speed + forces_x[i]
            self.y_positions[i] += (random.random() - 0.5) * self.speed + forces_y[i]

            # Ensure particles stay within bounds and handle bouncing
            if self.x_positions[i] < self.model.x_lim[0] or self.x_positions[i] > self.model.x_lim[1]:
                self.x_positions[i] = max(self.model.x_lim[0], min(self.x_positions[i], self.model.x_lim[1]))
                self.speed = -self.speed

            if self.y_positions[i] < self.model.y_lim[0] or self.y_positions[i] > self.model.y_lim[1]:
                self.y_positions[i] = max(self.model.y_lim[0], min(self.y_positions[i], self.model.y_lim[1]))
                self.speed = -self.speed



class Particles2:
    def __init__(self, x_positions, y_positions, speed, model, color):
        self.model = model
        self.x_positions = x_positions
        self.y_positions = y_positions
        self.speed = speed
        self.color = color
        self.angle = [random.uniform(0, 2 * math.pi) for _ in x_positions]  # Random initial angle for each particle

    def distance_and_direction(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        dist = math.sqrt(dx ** 2 + dy ** 2)
        return dist, dx, dy

    def update_positions(self):
        self.speed = self.model.speed
        force_strength = self.model.force_strength
        repulsion_distance = self.model.repulsion_distance
        friction = 0.95  # Friction factor

        forces_x = [0] * len(self.x_positions)
        forces_y = [0] * len(self.y_positions)

        for i in range(len(self.x_positions)):
            for j in range(i + 1, len(self.x_positions)):
                dist, dx, dy = self.distance_and_direction(self.x_positions[i], self.y_positions[i],
                                                           self.x_positions[j], self.y_positions[j])
                if dist > 0:
                    force_magnitude = -force_strength if dist < repulsion_distance else force_strength
                    force_x = force_magnitude * dx / dist
                    force_y = force_magnitude * dy / dist

                    forces_x[i] += force_x
                    forces_y[i] += force_y
                    forces_x[j] -= force_x
                    forces_y[j] -= force_y

        for i in range(len(self.x_positions)):
            self.angle[i] += 0.01  # Slowly change the angle

            # Using sine and cosine for smoother movement
            move_x = math.cos(self.angle[i]) * self.speed
            move_y = math.sin(self.angle[i]) * self.speed

            self.x_positions[i] += move_x + forces_x[i]
            self.y_positions[i] += move_y + forces_y[i]

            self.x_positions[i] *= friction
            self.y_positions[i] *= friction

            if self.x_positions[i] < self.model.x_lim[0] or self.x_positions[i] > self.model.x_lim[1]:
                self.x_positions[i] = max(self.model.x_lim[0], min(self.x_positions[i], self.model.x_lim[1]))
                self.speed *= -0.9

            if self.y_positions[i] < self.model.y_lim[0] or self.y_positions[i] > self.model.y_lim[1]:
                self.y_positions[i] = max(self.model.y_lim[0], min(self.y_positions[i], self.model.y_lim[1]))
                self.speed *= -0.9



class Particle:
    def __init__(self, x, y, speed, direction, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.color = color
        self.history = []  # To store the positions for the fading tail

    def update(self, particles):
        # Update position based on speed and direction
        self.x += math.cos(self.direction) * self.speed
        self.y += math.sin(self.direction) * self.speed

        # Add current position to history for the tail
        self.history.append((self.x, self.y))
        if len(self.history) > 10:  # Limit the length of the tail
            self.history.pop(0)

        # Check for collisions with other particles and bounce
        for particle in particles:
            if particle != self and self.distance_to(particle) < 10:
                self.direction = (self.direction + math.pi) % (2 * math.pi)

    def distance_to(self, other_particle):
        dx = self.x - other_particle.x
        dy = self.y - other_particle.y
        return math.sqrt(dx**2 + dy**2)


class Particles3:
    def __init__(self, num_particles, width, height):
        self.particles = []
        for _ in range(num_particles):
            x = random.randint(0, width)
            y = random.randint(0, height)
            speed = random.uniform(1, 3)
            direction = random.uniform(0, 2 * math.pi)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.particles.append(Particle(x, y, speed, direction, color))

    def update_positions(self):
        for particle in self.particles:
            particle.update(self.particles)



