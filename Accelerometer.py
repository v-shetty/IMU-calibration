
import numpy as np
from time import time, sleep
#from sense_hat import SenseHat
import math
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit, QPushButton, QFileDialog, QSplashScreen, QCheckBox, QTableWidgetItem,QHeaderView,QProgressBar)

class Accelerometer:

    def calibrate(self):
        print("asdf")
        buttonReply = QMessageBox.question(self, 'Accelerometer Calibration ?',
                                           "Keep the each axis vertically upwards and downwards",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:

            #Read the accelerometer values and calculate the calibration parameters as per 4 point algorithm
           print(" Reading the sensor data")




        biasX= 0.25
        biasY = 0.852555
        biasZ = 0.789555545
        OffX = 0.789654
        OffY = 0.855555
        OffZ = 0.855555

        return [biasX, biasY, biasZ , OffX ,OffY ,OffZ]