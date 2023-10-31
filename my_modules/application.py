from Test import Test
from PyQt5.QtWidgets import QApplication
import sys
from MainView import MainView
from Model import Model
from Controller import Controller



class Application:
    def __init__(self):
        app = QApplication(sys.argv)
        model = Model()
        controller = Controller(model, None)
        view = MainView(controller)
        controller.view = view

        view.show()
        sys.exit(app.exec_())



