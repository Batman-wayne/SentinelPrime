"""This script is to explore the use of AirSim's provided LIDAR APIs 

    Author: Harris M  
"""

# Libraries 
import airsim
import pprint
import time
import math
import argparse
import pprint
import numpy

# Custom include path just for my machine
import sys 
sys.path.append('../../../../AirSim/PythonClient/car')

import setup_path 

def parse_lidarData(data):
    """Converts the raw LIDAR output from AirSim into a numpy array of floats

        Parameters
        ----------
        data : LidarData (AirSim class)
            The raw lidar data from AirSim

        Returns
        -------
        points
            A numpy array in the format [X Y Z] of the LIDAR points
    """
    points = numpy.array(data.point_cloud, dtype=numpy.dtype('f4'))
    points = numpy.reshape(points, (int(points.shape[0]/3), 3))

    return points
       
# Establish connection with the car
client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)
car_controls = airsim.CarControls()

# Grab the current state of the car and print it out      
state = client.getCarState()
s = pprint.pformat(state)


# File writing test: Wait for the user's key press, then write the coordinates to a file 

# Wait for the user input to continue                        
airsim.wait_key('Press any key to continue')

# Grab the raw lidar data 
lidarData = client.getLidarData() 

# Make sure it is valid 
if (len(lidarData.point_cloud) < 3):
    print("\tNo points received from Lidar data")
else:
    points = parse_lidarData(lidarData)
    print("\tReading data with time_stamp: %d number_of_points: %d" % (lidarData.time_stamp, len(points)))
    points_size = len(points)
    
    # Write the points to a file 
    with open("out.txt", "w") as file:
        for i in range(points_size):
            file.write(str(points[i][0]) + ", " + str(points[i][1]) + ", " + str(points[i][2]) + "\n")

# for i in range(1000):        
#     lidarData = client.getLidarData()

#     if (len(lidarData.point_cloud) < 3):
#         print("\tNo points received from Lidar data")
#     else:
#         points = parse_lidarData(lidarData)
#         print("\tReading data with time_stamp: %d number_of_points: %d" % (lidarData.time_stamp, len(points)))
#         print("\tSample point: " + str(points[0]))
#         print("\t\tlidar position: %s" % (pprint.pformat(lidarData.pose.position)))
#         print("\t\tlidar orientation: %s" % (pprint.pformat(lidarData.pose.orientation)))
