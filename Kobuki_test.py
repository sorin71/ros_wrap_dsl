# -*- coding: utf-8 -*-
"""
Created on Thur Aug 31 14:35:23 2014

@author: sorin
"""
#execfile('/home/sorin/roswork_FRSC2014/src/EnhanceRosNode/Kobuki_test.py')

import sys
sys.path.append("/home/sorin/roswork_FRSC2014/src/EnhanceRosNode")

#print sys.path



from RosNode import rosNode
#reload(rosNode)

#from std_msgs.msg import String

#from std_msgs.msg import Bool
#from kobuki_msgs.msg import MotorPower
#from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, PoseStamped
from move_base_msgs.msg import MoveBaseActionGoal
from tf2_msgs.msg import TFMessage

#from geometry_msgs.msg import PoseWithCovarianceStamped, PoseArray
#from nav_msgs.msg import Odometry
#from tf2_msgs.msg import TFMessage

drift = 0

 
def velocityProblemGen(data):
    #rostopic pub -1 /mobile_base/commands/velocity geometry_msgs/Twist '{linear:  {x: 1, y: 0.0, z: 5.5}, angular: {x: 0.0,y: 0.0,z: 0.5}}'
    #sudden max speed exceeded
    data.linear.x = 1.1
    #graduately exceeding max forward speed
    data.linear.x = data.linear.x + drift 
    drift = drift + 0.01
    #can't steer left
    if  data.angular.z > 0:
        data.angular.z = 0 
    #can't steer right
    if  data.angular.z < 0: 
        data.angular.z = 0 
    #angular velocity drift
    if data.angular.z >= 0:
        data.angular.z = data.angular.z + drift
    if data.angular.z < 0:
        data.angular.z = data.angular.z - drift
    drift = drift + 0.01

    nd.write('mobile_base/commands/velocity',data)

def relayVelocity(data):
    #print("myCoolFn received: {}".format(data))
    nd.write('mobile_base/commands/velocity',data)

def alterAngular(data):
    #angular velocity drift  
    global drift
    if data.angular.z >= 0:
        data.angular.z += drift
    if data.angular.z < 0:
        data.angular.z -= drift
    drift = drift + 0.01

    nd.write('mobile_base/commands/velocity',data)
 
    
def myFn2(data):
    print("myFn2 received: {}, sending it".format(data))
    nd.write('onTopic2',data)   

nd = rosNode("enhanced_move_base")

nd.basePackage("move_base")\
  .baseNode("move_base") 
  
{
 nd.reuse.publish(topic = "cmd_vel",msgType = Twist)
         .publish(topic =  "move_base/current_goal", msgType = PoseStamped)
         .publish(topic = "move_base/goal", msgType = MoveBaseActionGoal)
         .subscribe(topic = "tf_static",msgType = TFMessage)
         .subscribe(topic = "move_base_simple/goal",msgType = PoseStamped)
         .subscribe(topic = "tf",msgType = TFMessage)
}

#remap from="cmd_vel" to="mobile_base/commands/velocity

{
nd.new.subscribe(topic = "cmd_vel",handler = relayVelocity, msgType = Twist)
      .publish(topic = "mobile_base/commands/velocity", msgType = Twist)
}


nd.create()

variable = raw_input("press enter for modify velocity handling function")

nd.new.subscribe(topic = "cmd_vel",handler = alterAngular, msgType = Twist)

#replace a subscribed topic handler
#nd.unsubscribe("inTopic1")

#variable = raw_input("press enter for changing the handler function for inTopic1")
#nd.new.subscribe(topic = "inTopic1",handler = myCoolFn, msgType = String)
#nd.update("inTopic1")

#print "myCoolFn is active for inTopic1"
#nd.onTopic("onTopic1").publish("test message")
  
#nd.printNode()