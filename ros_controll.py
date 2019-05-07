
# coding: utf-8

import rospy
import numpy as np
from time import sleep
from sensor_msgs.msg import LaserScan, Image
from ackermann_msgs.msg import AckermannDriveStamped

class racecar_controller:
    def __init__(self):
        self.angle = 0
        self.speed = 0
	rospy.init_node('racecar_controller', anonymous=True)
	self.pub = rospy.Publisher('/ackermann_cmd_mux/input/navigation', AckermannDriveStamped, queue_size=1)
        self.cmd = AckermannDriveStamped()
    def get_speed(self):
        return self.speed
    def get_angle(self):
        return self.angle
    def set_speed(self,speed):
        self.speed = speed
    def set_angle(self,angle):
        self.angle = angle
    def racecar_control(self):
        rate = rospy.Rate(20)
        delay = 1000/25
        while not rospy.is_shutdown():
	    print self.cmd
            self.cmd.drive.steering_angle = self.angle
            self.cmd.drive.speed=self.speed
            self.pub.publish(self.cmd)
            rate.sleep()

