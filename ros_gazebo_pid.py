
# coding: utf-8

import cv2
import rospy
import ros_controll
import lidar_module
from time import sleep
from threading import Thread
from sensor_msgs.msg import LaserScan,Image
from cv_bridge import CvBridge, CvBridgeError


racecar = ros_controll.racecar_controller()
racecar_thread =Thread(target = racecar.racecar_control)
bridge = CvBridge()
racecar.set_speed(2) 


class super_class:
    def __init__(self):
        self.angle=0
        self.speed=0
    def lidar_data(self,msg):
        x =lidar_module.lidar_controll()
        x.lidar(msg)
        lidar_angle = x.get_lidar_angle()
        self.angle = lidar_angle
    def set_speed_angle(self):
        while(True):
            racecar.set_angle(self.angle)



def image_callback(msg):
        try:
            cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
            cv2.imshow('kamera',cv2_img)
            cv2.waitKey(0)
        except CvBridgeError, e:
            print(e)



if __name__ == '__main__':
	s = super_class()
	control_thread = Thread(target=s.set_speed_angle)
	rospy.Subscriber("/scan",LaserScan,s.lidar_data)
	image_topic = "/camera/zed/rgb/image_rect_color"
	rospy.Subscriber(image_topic, Image, image_callback)
	racecar_thread.start()
	control_thread.start()

