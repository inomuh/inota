#!/usr/bin/env python3
import rospy
from agv_msgs.msg import RobotLow

class EncoderWrite:
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("agv1/robot_low", RobotLow, self.callback)
        self.f_encoder = open("covid_encoder.csv","a")
        self.f_encoder.write("Ros time;encoder_left;encoder_right\n")
        self.right = None
        self.left = None        
        while not rospy.is_shutdown():
            self.counter = 0

    def callback(self,data):
        self.right = data.encoder_right
        self.left = data.encoder_left
        self.f_encoder.write(str(rospy.Time.now()) + ";" + str(self.left) + ";" + str(self.right) + "\n")

if __name__ == '__main__':
    EncoderWrite()