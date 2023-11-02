# model.py
class Model:
    def __init__(self):
        # TODO: starting dialog, which asks to enter some basic starting parameters (species count and particle num)
        self.num_particles = 100 # for one species
        self.parameters = {"slider_values": [0]*5}
        self.speed = 0.0001
        self.timer_update_interval = 5 # ms updating
        self.attraction_strength = 0.001
        self.repulsion_distance = 0.001
        self.repulsion_strength = 0.001
        self.x_lim = [-0.1, 0.1]
        self.y_lim = [-0.1, 0.1]
        self.species_count = 2

    def update_speed(self, value):
        self.speed = value*0.0005
    def update_time_update_interval(self, value):
        self.timer_update_interval = value

    def update_attraction_strength(self, value):
        self.attraction_strength = value * 0.001

    def update_repulsion_strength(self, value):
        self.repulsion_strength = value * 0.0001

    def update_repulsion_distance(self, value):
        self.repulsion_distance = value * 0.001







