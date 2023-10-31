import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
from Particles import Particles
from Particles import Particles2
from Particles import Particles3

class SimulationWidget(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.initUI()

        # Initialize particle positions

        self.x_positions1 = [self.set_starting_positions() for _ in range(self.model.num_particles)]
        self.y_positions1 = [self.set_starting_positions() for _ in range(self.model.num_particles)]

        self.x_positions2 = [self.set_starting_positions() for _ in range(self.model.num_particles)]
        self.y_positions2 = [self.set_starting_positions() for _ in range(self.model.num_particles)]

        self.speed = self.model.speed # Adjust this value to make particles move faster or slower

        self.particles1 = Particles(self.x_positions1, self.y_positions1, self.speed, self.model, "red")
        self.particles2 = Particles2(self.x_positions2, self.y_positions2, self.speed, self.model, "blue")



        # Define the speed of the particles

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.graphWidget = pg.PlotWidget()
        self.layout.addWidget(self.graphWidget)

        # Set the background color to white
        self.graphWidget.setBackground('w')

        # Setting the range for the axes
        self.graphWidget.setXRange(self.model.x_lim[0], self.model.x_lim[1])
        self.graphWidget.setYRange(self.model.y_lim[0], self.model.y_lim[1])

        # Initialize scatter plot items for particles
        self.scatter1 = pg.ScatterPlotItem(pen=pg.mkPen(width=0.001, color='r'), brush=pg.mkBrush('r'))
        self.scatter2 = pg.ScatterPlotItem(pen=pg.mkPen(width=0.001, color='b'), brush=pg.mkBrush('b'))

        self.graphWidget.addItem(self.scatter1)
        self.graphWidget.addItem(self.scatter2)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
        self.timer.setInterval(self.model.timer_update_interval)  # Update every 50 milliseconds

    def set_starting_positions(self):
        return random.gauss(0, 0)


    def update_plot(self):
        self.speed = self.model.speed  # Adjust this value to make particles move faster or slower

        self.update_particle_positions()

        # Update scatter plot data
        self.scatter1.setData(self.particles1.x_positions, self.particles1.y_positions)
        self.scatter2.setData(self.particles2.x_positions, self.particles2.y_positions)



    def update_particle_positions(self):
        self.particles1.update_positions()
        self.particles2.update_positions()





