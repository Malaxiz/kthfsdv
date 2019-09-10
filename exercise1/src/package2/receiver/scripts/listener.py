#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def listener():
    pub = rospy.Publisher('kthfs/result', String, queue_size=10)

    def callback(data):
        q = 0.15
        msg = '%f' % (int(data.data) / q)
        rospy.loginfo(msg)
        pub.publish(msg)

    rospy.init_node('nodeB', anonymous=True)
    rospy.Subscriber('didrik', String, callback)
    
    rospy.spin()

if __name__ == '__main__':
    listener()
