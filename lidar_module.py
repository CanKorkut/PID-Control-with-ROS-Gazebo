
# coding: utf-8

import rospy
import pid_controll
import numpy as np
from time import sleep
import matplotlib.pyplot as plt
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped


class lidar_controll:
    def __init__(self):
        self.left_data = []
        self.right_data = []
        self.lidar_angle = 0
        self.lidar_speed = 0
	
    def set_lidar_angle(self,angle):
        self.lidar_angle = angle
    def get_lidar_angle(self):
        return self.lidar_angle
    def get_left_data(self):
        return self.left_data
    def get_right_data(self):
        return self.right_data
    def lidar(self,msg):
        self.left_data = msg.ranges [270:540]
        self.right_data = msg.ranges [540:810]
        left_min= min(self.left_data)
        right_min= min(self.right_data)
        pid_controller = pid_controll.pid()
        Left_set_point=60
        pid_controller.setPoint(Left_set_point)
        state = "right"
        if left_min != 'inf' and( left_min < right_min or right_min == 'inf') :
            current_value = left_min*100
            state = "left"
        elif right_min != 'inf' and (right_min < left_min or left_min == 'inf'):
            current_value = right_min*100
            state = "right"
        else:
            current_value = 80
        angle=pid_controller.update(current_value)
        if (pid_controller.getError()>0.0):
            if state == "right":
                x = angle*-1
                self.lidar_angle = x
            elif state == "left":
                self.lidar_angle = angle
    

