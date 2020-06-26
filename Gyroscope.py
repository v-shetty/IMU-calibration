
import numpy as np
from time import time, sleep
#from sense_hat import SenseHat
import math


class Gyroscope:

    def CalcBias(self):
        start_time = time()
        duration = 0


        #sense = SenseHat()

        # np array to store all the reading
        gx = np.array([])
        gy = np.array([])
        gz = np.array([])

        while duration < 1:
            duration = time() - start_time

            #gyro_raw = sense.get_gyroscope_raw()

            #x = math.degrees(gyro_raw["x"])
            #y = math.degrees(gyro_raw["y"])
            #z = math.degrees(gyro_raw["z"])

            #gx = np.append(gx, x)
            #gx = np.append(gx, y)
            #gx = np.append(gx, z)
        print("ok iam done ")
        #biasX = np.std(gx)
        #biasY = np.std(gy)
        #biasZ = np.std(gz)
        biasX= 10.00015547
        biasY = 20.054854
        biasZ = 30.0789895
        return [biasX , biasY, biasZ]