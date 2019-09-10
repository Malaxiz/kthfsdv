#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('didrik', String, queue_size=10)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(20) # 20hz

    n = 4
    k = 1

    while not rospy.is_shutdown():
        hello_str = "%s" % k
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        k += n

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
