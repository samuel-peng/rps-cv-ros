#!/usr/bin/env python
# Software License Agreement (BSD License)
#
## Simple talker demo that listens to std_msgs/Strings published
## to the 'chatter' topic

import rospy
from settings import subscriberTopic
from talker import talker
from playgui import getResult

from std_msgs.msg import String
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge, CvBridgeError

gestureTxt = {ROCK: 'rock', PAPER: 'paper', SCISSORS: 'scissors'}
resultTxt = {TIE: 'tie', ROBOT: 'robot wins', HUMAN: 'player wins'}


def callback(data):
    image = bridge.imgmsg_to_cv2(data, desired_encoding = "rgb9: CV_8UC3")
    result = getResult(image)
    talker(resultTxt[result[0]], gestureTxt[result[1]], gestureTxt[result[2]])

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber(subscriberTopic, Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
