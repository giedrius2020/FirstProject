
# controller.py
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_model(self, slider_index, value):
        if slider_index == 0:
            self.model.update_speed(value)
        if slider_index == 1:
            self.model.update_repulsion_strength(value)
        if slider_index == 2:
            self.model.update_repulsion_distance(value)
        #print(f"Value: {value}") # 0 - 100
        # self.model.speed(value)
        self.view.update()

    def update_slider_label(self, slider_index, value):
        """Update the text of the slider label."""
        if slider_index == 0:
            self.view.slider_labels[slider_index].setText(f"Particle speed: {self.model.speed}")
        if slider_index == 1:
            self.view.slider_labels[slider_index].setText(f"Repulsion strength: {self.model.repulsion_strength}")
        if slider_index == 2:
            self.view.slider_labels[slider_index].setText(f"Repulsion distance: {self.model.repulsion_distance}")
