from ParticleSystem import ParticleSystem
import numpy as np
import matplotlib.colors as mcolors

class SpeciesManager:
    # Each particle system is defined as different species. It will have different set of paramaters.

    # When creating multiple species, certain parameters can differ a bit and be constant,
    # while other can be mutual and adjustable in real time.

    # Each species has a profile - it describes the parameters of the species.

    def __init__(self, model):
        self.model = model

        self.species_profiles = []

        self.all_species = []
        self.color_palette = None
        self.collision_distance_range = None

        self.generate_parameter_ranges()
        self.create_multiple_species()

    def create_multiple_species(self):
        # Parameters constant for all species:
        collision_distance = 0.0001
        attraction_strength, repulsion_strength, repulsion_distance = 0.001, 0.001, 0.001


        # Generate species:
        for i, _ in enumerate(self.color_palette):
            item = ParticleSystem(self.model,
                                  self.color_palette[i],
                                  collision_distance,
                                  self.attraction_strength_range[i],
                                  repulsion_strength,
                                  repulsion_distance)
            self.all_species.append(item)

    def generate_parameter_ranges(self):
        steps = self.model.species_count
        # Start color: cool blue, end color: warm red.
        self.color_palette = self.generate_color_gradient(start_color="#4575B4", end_color="#D73027", steps=steps)
        # self.collision_distance_range = np.linspace(0.001, 0.01, steps)
        self.attraction_strength_range = np.linspace(0.0001, 0.001, steps)



    def generate_species_profiles(self):
        pass

    def rgb_to_hex(self, rgb_color):
        return '#{:02x}{:02x}{:02x}'.format(int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255))

    def generate_color_gradient(self, start_color, end_color, steps):
        # Convert colors to RGB
        start_rgb = mcolors.to_rgb(start_color)
        end_rgb = mcolors.to_rgb(end_color)

        # Generate gradient
        gradient = []
        for i in range(steps):
            r = (end_rgb[0] - start_rgb[0]) * i / (steps - 1) + start_rgb[0]
            g = (end_rgb[1] - start_rgb[1]) * i / (steps - 1) + start_rgb[1]
            b = (end_rgb[2] - start_rgb[2]) * i / (steps - 1) + start_rgb[2]
            gradient.append(self.rgb_to_hex((r, g, b)))
        return gradient
