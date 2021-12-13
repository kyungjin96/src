#! /usr/bin/env python3
from threading import current_thread

from yaml import tokens
import rospy
from geometry_msgs.msg import Twist
import time




if __name__ == '__main__' :
    rospy.init_node("sim_turtle_pub")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)



    twist = Twist()

    twist.linear.y = twist.linear.z = 0.0
    twist.angular.x = twist.angular.y = twist.angular.z = 0.0

    distance = 2

    current_distance = 0

    speed = 0.8

    twist.linear.x = distance
    while not rospy.is_shutdown():
        time0 = rospy.Time.now().to_sec()
        # twist.linear.x = distance

        while current_distance < distance :
            pub.publish(twist)
            time1 = rospy.Time.now().to_sec()
            current_distance = speed * (time1-time0)
        twist.linear.x = 0
        pub.publish(twist)
       





    # rate = rospy.Rate(10)
    # while rospy.is_shutdown :
    #     str = "hello_pubgogo01 : %s"  % rospy.get_time()
    #     pub.publish(str)
    #     rate.sleep()
    pass