from mpu6050 import mpu6050
from time import *
import requests

sensor = mpu6050(0x68)

while True:
    gyro_data = sensor.get_gyro_data()
    print("x: " + str(gyro_data['x']))
    requests.post("http://127.0.0.1:5000/", datta = {'x':time(), 'y':gyro_data['x']})