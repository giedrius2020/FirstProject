import random
import math
from Particle import Particle


class ParticleSystem:
    # TODO: let init all sorts of different parameters, which make species unique.
    def __init__(self, model, color, collision_distance, attraction_strength, repulsion_strength, repulsion_distance):
        self.model = model
        self.color = color
        self.particles = []
        self.x_positions = []
        self.y_positions = []
        for _ in range(model.num_particles):
            x = random.uniform(-0.01, 0.01)
            y = random.uniform(-0.01, 0.01)
            # speed = random.uniform(-0.1, 0.1)
            direction = random.uniform(0, 2 * math.pi)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.particles.append(Particle(self.model,
                                           x, y,
                                           model.speed,
                                           direction,
                                           color,
                                           collision_distance,
                                           attraction_strength,
                                           repulsion_strength,
                                           repulsion_distance
                                           ))

    def update_positions(self):
        for particle in self.particles:
            particle.update(self.particles)
        self.x_positions, self.y_positions = ([particle.x for particle in self.particles],
                                              [particle.y for particle in self.particles])

    def update_parameters(self):
        for particle in self.particles:
            particle.update_parameters()

    # def set_starting_positions(self):
    #     self.x_positions2 = [self.starting_positions_function() for _ in range(self.model.num_particles)]
    #
    #
    # def starting_positions_function(self):
    #     return random.gauss(0, 0)
