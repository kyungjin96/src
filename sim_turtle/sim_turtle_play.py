#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time, cv2
from std_srvs.srv import Empty

img = cv2.imread('./sim_turtle/kyung_jin.jpeg')

def rreset():
    rospy.wait_for_service('/reset')
    reset_world = rospy.ServiceProxy('/reset', Empty)
    return reset_world()


def reset():
    twist.linear.y = twist.linear.z = twist.linear.x =0.0
    twist.angular.x = twist.angular.y = twist.angular.z = 0.0
    return

def play():
    distance = 2.0
    while True: 
        cv2.imshow('kyungjin',img)
        key = cv2.waitKey(1)
        if key == 27 :
            break
        elif key == ord('w'):
            reset()        
            twist.linear.x = distance*2
            pub.publish(twist)
            time.sleep(0.5)
        elif key == ord('s'):
            reset()
            twist.linear.x = -distance
            pub.publish(twist)
            time.sleep(1)
        elif key == ord('a'):
            reset()
            twist.angular.z = distance
            pub.publish(twist)
            time.sleep(0.5)
        elif key == ord('d'):
            reset()
            twist.angular.z = -distance
            pub.publish(twist)
            time.sleep(0.5)
        elif key == ord('z'):
            reset()
            twist.linear.y = distance
            pub.publish(twist)
            time.sleep(1)
        elif key == ord('x'):
            reset()
            twist.linear.y = -distance
            pub.publish(twist)
            time.sleep(1)
        elif key == ord('q'):
            rreset()
            pub.publish(twist)

    cv2.destroyAllWindows()
    return


if __name__ == '__main__' :
    rospy.init_node("sim_turtle_pub")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    twist = Twist()
    play()
    
    pass