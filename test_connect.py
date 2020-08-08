"""Purpose: This file is for connecting airsim to Unreal? (Please edit this comment @Harris)"""

# Libraries 
import airsim
import pprint
import time
import cv2 #conda install opencv

# Custom include path just for my machine
import sys 
sys.path.append('../../../../AirSim/PythonClient/car')

import setup_path 

# connect to the AirSim simulator 
client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)
car_controls = airsim.CarControls()

client.reset()

# client.startRecording()

# Test program: Drive the car a bunch of ways
client.simPrintLogMessage("AirSim Test Drive")
client.simPrintLogMessage("Car drive straight")

# go forward
car_controls.throttle = 2.0
car_controls.steering = 0
client.setCarControls(car_controls)

time.sleep(3)

# go right 
client.simPrintLogMessage("Car drive right")
car_controls.throttle = 2.0
car_controls.steering = 1
client.setCarControls(car_controls)

time.sleep(1)

# go left 
client.simPrintLogMessage("Car drive left")
car_controls.throttle = 2.0
car_controls.steering = -1
client.setCarControls(car_controls)

time.sleep(2)

# Grab the state of the car 
car_state = client.getCarState()
pos = car_state.kinematics_estimated.position
orientation = car_state.kinematics_estimated.orientation
client.simPrintLogMessage("pos.x_val: ", str(pos.x_val))
client.simPrintLogMessage("pos.y_val: ", str(pos.y_val))
client.simPrintLogMessage("pos.z_val: ", str(pos.z_val))
client.simPrintLogMessage("orientation.w_val: ",str(orientation.w_val))
client.simPrintLogMessage("orientation.x_val: ",str(orientation.x_val))
client.simPrintLogMessage("orientation.y_val: ",str(orientation.y_val))
client.simPrintLogMessage("orientation.z_val: ",str(orientation.z_val))

# client.stopRecording()

client.enableApiControl(False)

