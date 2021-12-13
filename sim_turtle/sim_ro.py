#! /usr/bin/env python3
from threading import current_thread
import rospy
from geometry_msgs.msg import Twist




if __name__ == '__main__' :
    rospy.init_node("sim_turtle_pub")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    twist = Twist()

    twist.angular.z = 3.14
    rel = 3.14

    current = 3.13
    time0 = rospy.Time.now().to_sec()
    while current < rel :
        pub.publish(twist)
        time1 = rospy.Time.now().to_sec()
        current = current*(time0-time1)
        
    twist.angular.z =0.0
    pass