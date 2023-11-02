import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
from ParticleSystem import ParticleSystem
from SpeciesManager import SpeciesManager

class SimulationWidget(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.species_manager = SpeciesManager(model)
        self.particle_systems = self.species_manager.all_species

        self.scatter_plots = []  # List to store scatter plots for each particle system


        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.graphWidget = pg.PlotWidget()
        self.layout.addWidget(self.graphWidget)

        # Set the background color to white
        self.graphWidget.setBackground('w')

        # Setting the range for the axes
        self.graphWidget.setXRange(self.model.x_lim[0], self.model.x_lim[1])
        self.graphWidget.setYRange(self.model.y_lim[0], self.model.y_lim[1])

        # Create scatter plot items for each particle system
        for particle_system in self.particle_systems:
            scatter_plot = pg.ScatterPlotItem(pen=pg.mkPen(width=0.001, color=particle_system.color),
                                              brush=pg.mkBrush(particle_system.color))
            self.scatter_plots.append(scatter_plot)
            self.graphWidget.addItem(scatter_plot)



        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
        self.timer.setInterval(self.model.timer_update_interval)  # Update every 50 milliseconds




    def update_plot(self):
        self.speed = self.model.speed  # Adjust this value to make particles move faster or slower.
        # TODO: Refactor to update only during slider changes, not on each frame.
        # Updating particle system:
        for particle_system, scatter_plot in zip(self.particle_systems, self.scatter_plots):
            particle_system.update_positions()
            particle_system.update_parameters()

            # Updating scatter data of the system:
            scatter_plot.setData(particle_system.x_positions, particle_system.y_positions)





