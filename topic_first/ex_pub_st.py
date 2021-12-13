#! /usr/bin/env python3
import rospy
from std_msgs.msg import String

# def gogo(y) :
#     rospy.init_node("sample_pub")
#     pub = rospy.Publisher(y, String, queue_size=10)

#     rate = rospy.Rate(10)
#     while True :
#         str = "hello : " +rospy.get_time()
#         pub.publish(str)
#         rate.sleep()

#     return


if __name__ == '__main__' :
    rospy.init_node("sample_pub01")
    pub = rospy.Publisher("hello", String, queue_size=10)

    rate = rospy.Rate(10)
    while rospy.is_shutdown :
        str = "hello_pubgogo01 : %s"  % rospy.get_time()
        pub.publish(str)
        rate.sleep()
    pass