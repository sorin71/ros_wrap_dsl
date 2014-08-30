# -*- coding: utf-8 -*-
"""
Created on Thur Aug 28 16:55:45 2014

@author: sorin
"""
#execfile('/home/sorin/roswork_FRSC2014/src/EnhanceRosNode/Turtle_sim_test.py')

import sys
sys.path.append("/home/sorin/roswork_FRSC2014/src/EnhanceRosNode")

#print sys.path

from RosNode import rosNode
#reload(rosNode)

from geometry_msgs.msg import Twist
from turtlesim.msg import Color, Pose
from std_msgs.msg import String




def myCoolFn(data):
    print("myCoolFn received: {}".format(data))
    nd.write('onTopic1', data )
    
def myFn1(data):
    print("myFn1 received: {}, sending it".format(data))
    nd.write('onTopic1',data)
    
def myFn2(data):
    print("myFn2 received: {}, sending it".format(data))
    nd.write('onTopic2',data)   

nd = rosNode("super_talker_node")

nd.basePackage("rospy_tutorials")\
  .baseNode("talker") 
  
{
nd.reuse.publish(topic = "chatter",msgType = String)
}

nd.create()

#variable = raw_input("press enter for unsubscribe from inTopic1")

#replace a subscribed topic handler
#nd.unsubscribe("inTopic1")

#variable = raw_input("press enter for changing the handler function for inTopic1")
#nd.new.subscribe(topic = "inTopic1",handler = myCoolFn, msgType = String)
#nd.update("inTopic1")

#print "myCoolFn is active for inTopic1"
#nd.onTopic("onTopic1").publish("test message")
  
#nd.printNode()