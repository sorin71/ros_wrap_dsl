# -*- coding: utf-8 -*-
"""
Created on Thur Oct 7 11:04:40 2014

@author: sorin
"""
#execfile('/home/sorin/roswork_FRSC2014/src/EnhanceRosNode/Turtle_sim_test.py')

import sys
sys.path.append("/home/sorin/roswork_FRSC2014/src/EnhanceRosNode")

#print sys.path

from RosNode import rosNode
#from rospy import Timer
import rospy
#reload(rosNode)

from geometry_msgs.msg import Twist
from turtlesim.msg import Color, Pose
from std_msgs.msg import String

#  Pose
#float32 x
#float32 y
#float32 theta

#float32 linear_velocity
#float32 angular_velocity

#  Twist
#Vector3  linear
#Vector3  angular

show = False

def showPose(data):
    global show;
    if show :
        print("Pose: {}".format(data))
        
nd = rosNode("turtle_control_node")

{
nd.new.subscribe(topic = "/turtle1/pose", handler = showPose, msgType = Pose)
      .publish(topic = "/turtle1/cmd_vel", msgType = Twist)
}

nd.create()

def onTimer(event):
    msg = Twist()
    msg.linear.x = 2.0 
    msg.angular.z = 1.8
    nd.write("/turtle1/cmd_vel", msg )

timer = rospy.Timer(rospy.Duration(1), onTimer)
timer.shutdown()

#nd.update("inTopic1")

#variable = raw_input("press enter for unsubscribe from inTopic1")

#replace a subscribed topic handler
#nd.unsubscribe("inTopic1")

#variable = raw_input("press enter for changing the handler function for inTopic1")
#nd.new.subscribe(topic = "inTopic1",handler = myCoolFn, msgType = String)
#nd.update("inTopic1")

#print "myCoolFn is active for inTopic1"
#nd.onTopic("onTopic1").publish("test message")
  
#nd.printNode()