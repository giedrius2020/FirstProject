# model.py
class Model:
    def __init__(self):
        self.num_particles = 100
        self.parameters = {"slider_values": [0]*5}
        self.speed = 0.0001
        self.timer_update_interval = 5 # ms updating
        self.force_strength = 0.001
        self.repulsion_distance = 0.001
        self.x_lim = [-0.1, 0.1]
        self.y_lim = [-0.1, 0.1]

    def update_speed(self, value):
        self.speed = value*0.0005
    def update_time_update_interval(self, value):
        self.timer_update_interval = value

    def update_force_strength(self, value):
        self.force_strength = value * 0.0001


    def update_repulsion_distance(self, value):
        self.repulsion_distance = value * 0.001







