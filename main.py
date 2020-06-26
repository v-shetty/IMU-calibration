'''
Created on Nov 25, 2019

@author: Vikas Shetty
'''

import sys, os
from time import time, sleep
import numpy as np
from time import time, sleep
import math
#from sense_hat import SenseHat
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit, QPushButton, QFileDialog, QSplashScreen, QCheckBox, QTableWidgetItem,QHeaderView,QProgressBar)
from Gyroscope import Gyroscope as GP
from Accelerometer import Accelerometer as Acc
print("hello")
class SearchWindow(QMainWindow):

    def __init__(self, *args):
        super(SearchWindow, self).__init__(*args)
        self.ui = loadUi(str(os.getcwd() + '\\CalibrationWindow.ui'), self)
        self.setGeometry(500, 150, 800, 600)

        # initialize the buttons
        self.ui.pb_calibrateGyro.clicked.connect(self.calibrateGyro)
        self.ui.pb_calibrateAcc.clicked.connect(self.calibrateAcc)
        #self.ui.sb_Gyro = QProgressBar(self)
        #self.sb_Gyro.setGeometry(60, 370, 600, 25)


    def calibrateAcc(self):


        [biasX, biasY, biasZ , OffX ,OffY ,OffZ] = Acc.calibrate(self)


        self.cb_Acc.setEnabled(True)
        self.cb_Acc.setChecked(True)

        self.tv_AccScaleX.setText(str(round(biasX, 4)))
        self.tv_AccScaleY.setText(str(round(biasY, 4)))
        self.tv_AccScaleZ.setText(str(round(biasZ, 4)))

        self.tv_AccOffX.setText(str(round(OffX, 4)))
        self.tv_AccOffY.setText(str(round(OffY, 4)))
        self.tv_AccOffZ.setText(str(round(OffZ, 4)))





    def calibrateGyro(self):

        buttonReply = QMessageBox.question(self, 'Gyroscope Calibration ?',
                                           "Keep the Gyroscope in static environment for 10 seconds.?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:

            [biasX , biasY, biasZ] = GP.CalcBias(self)
            print(biasZ)
            self.cb_Gyro.setEnabled(True)
            self.cb_Gyro.setChecked(True)
            self.tv_GyroBiasX.setText(str(round(biasX,4)))
            self.tv_GyroBiasY.setText(str(round(biasY,4)))
            self.tv_GyroBiasZ.setText(str(round(biasZ,4)))

        else:
            print('No clicked.')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SearchWindow()
    app_icon = QtGui.QIcon()
    app_icon.addFile('mblogo.jfif', QtCore.QSize(500, 500))
    widget.setWindowIcon(app_icon)
    widget.show()
    sys.exit(app.exec_())