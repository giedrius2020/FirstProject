# view.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt  # Import the Qt module
from SImulationWidget import SimulationWidget




from PyQt5.QtGui import QPainter, QColor, QBrush



class MainView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Particle Simulation")
        self.setGeometry(100, 100, 600, 600)  # Set position and size of window

        # Main layout
        main_layout = QVBoxLayout()  # Changed from QHBoxLayout to QVBoxLayout

        # Particle Simulation Section
        self.simulation_widget = SimulationWidget(self.controller.model)
        self.simulation_widget.setFixedSize(600, 600)
        main_layout.addWidget(self.simulation_widget)

        # Sliders Section
        sliders_layout = QVBoxLayout()
        self.sliders = []
        self.slider_labels = []  # List to keep track of slider value labels
        for i in range(3):  # Create 5 sliders as an example
            slider = QSlider()
            slider.setOrientation(Qt.Horizontal)
            slider.setRange(0, 100)  # Set the range of the slider

            # Label to display the slider's value
            slider_label = QLabel(f"Slider {i + 1}: {slider.value()}")
            self.slider_labels.append(slider_label)

            # Connect slider valueChanged signal
            slider.valueChanged.connect(lambda value, index=i: self.controller.update_slider_label(index, value))
            slider.valueChanged.connect(lambda value, index=i: self.controller.update_model(index, value))
            self.sliders.append(slider)
            sliders_layout.addWidget(slider)
            sliders_layout.addWidget(QLabel(f"Slider {i+1}"))
            sliders_layout.addWidget(slider_label)

        sliders_widget = QWidget()
        sliders_widget.setLayout(sliders_layout)
        main_layout.addWidget(sliders_widget)

        # Set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Center the window on the screen
        self.centerWindow()

    def centerWindow(self):
        """Center the window on the screen."""
        screen_rect = QApplication.desktop().screenGeometry()
        window_rect = self.frameGeometry()
        center_point = screen_rect.center()
        window_rect.moveCenter(center_point)
        self.move(window_rect.topLeft())