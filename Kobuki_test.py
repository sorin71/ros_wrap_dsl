# -*- coding: utf-8 -*-
"""
Created on Thur Aug 31 14:35:23 2014

@author: sorin
"""
#execfile('/home/sorin/roswork_FRSC2014/src/EnhanceRosNode/Kobuki_test.py')

import sys
sys.path.append("/home/sorin/roswork_FRSC2014/src/EnhanceRosNode")

#print sys.path

#rostopic pub -1 /mobile_base/commands/motor_power kobuki_msgs/MotorPower 1
#rostopic pub -1 /mobile_base/commands/velocity geometry_msgs/Twist '{linear:  {x: 1, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.5}}'

#<node pkg="fake_localization" name="fake_localization" type="fake_localization">
#    <remap from="base_pose_ground_truth" to="odom"/>
#  </node>

# <node pkg="nodelet" type="nodelet" name="mobile_base_nodelet_manager" args="manager"/>
#  <node pkg="nodelet" type="nodelet" name="mobile_base" args="load kobuki_softnode/SoftKobukiNodelet mobile_base_nodelet_manager">
#    <rosparam file="$(find kobuki_softnode)/param/base.yaml" command="load"/>
#  <!-- <remap from="mobile_base/odom" to="odom"/> -->
#    <remap from="mobile_base/joint_states" to="joint_states"/> 
#  </node>

#/amcl_pose  publ: Type: geometry_msgs/PoseWithCovarianceStamped
#/base_pose_ground_truth subs: nav_msgs/Odometry
#/initialpose subs: Type: geometry_msgs/PoseWithCovarianceStamped 
#/particlecloud publ: Type: geometry_msgs/PoseArray

#/tf publ & subs: Type: tf2_msgs/TFMessage
#/tf_static subs: Type: tf2_msgs/TFMessage


from RosNode import rosNode
#reload(rosNode)

#from std_msgs.msg import String

#from std_msgs.msg import Bool
#from kobuki_msgs.msg import MotorPower
#from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

#from geometry_msgs.msg import PoseWithCovarianceStamped, PoseArray
#from nav_msgs.msg import Odometry
#from tf2_msgs.msg import TFMessage


def myCoolFn(data):
    print("myCoolFn received: {}".format(data))
    nd.write('onTopic1', data )
    
def myFn1(data):
    print("myFn1 received: {}, sending it".format(data))
    nd.write('onTopic1',data)
    
def myFn2(data):
    print("myFn2 received: {}, sending it".format(data))
    nd.write('onTopic2',data)   

nd = rosNode("enhanced_move_base")

nd.basePackage("move_base")\
  .baseNode("move_base") 
  
{
 nd.reuse.publish(topic = "cmd_vel",msgType = Twist)
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