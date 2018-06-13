#!/usr/bin/env python
# Software License Agreement (BSD License)

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from settings import talkerTopic
from settings import pubRobotResult
from settings import pubHumanResult
from std_msgs.msg import String

def talker(result, human, robot):
    pub = rospy.Publisher(talkerTopic, String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(result)
        pub.publish(result)
        if pubHumanResult == True :
            rospy.loginfo(human)
            pub.publish(human)
        if pubRobotResult == True :
            rospy.loginfo(robot)
            pub.publish(robot)
        rate.sleep()
"""
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
"""
