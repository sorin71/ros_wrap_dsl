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

#sorin@LTS14:~/roswork_FRSC2014$ rosnode info /move_base_node 
#--------------------------------------------------------------------------------
#Node [/move_base_node]
#Publications: 
# * /move_base_node/current_goal [geometry_msgs/PoseStamped]
# * /rosout [rosgraph_msgs/Log]
# * /relay_cmd_vel [geometry_msgs/Twist]
# * /move_base/goal [move_base_msgs/MoveBaseActionGoal]

#Subscriptions: 
# * /tf_static [unknown type]
# * /move_base_simple/goal [unknown type]
# * /tf [unknown type]

#Services: 
# * /move_base_node/get_loggers
# * /move_base_node/set_logger_level

#----------------------- sorin@LTS14:~/roswork_FRSC2014$ rosnode info /move_base
#------------------------------------------------------------- Node [/move_base]
#----------------------------------------------------------------- Publications:
 #--- * /move_base/global_costmap/costmap_updates [map_msgs/OccupancyGridUpdate]
 #------------------------ * /move_base/current_goal [geometry_msgs/PoseStamped]
 #-- * /move_base/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
  # * /move_base/local_costmap/inflation_layer/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 #---------------- * /move_base/feedback [move_base_msgs/MoveBaseActionFeedback]
 #--- * /move_base/global_costmap/parameter_updates [dynamic_reconfigure/Config]
 #-------------------- * /move_base/result [move_base_msgs/MoveBaseActionResult]
 #------------------ * /move_base/local_costmap/costmap [nav_msgs/OccupancyGrid]
 # * /move_base/global_costmap/static_layer/parameter_updates [dynamic_reconfigure/Config]
 # * /move_base/global_costmap/obstacle_layer_footprint/footprint_stamped [geometry_msgs/PolygonStamped]
 # * /move_base/local_costmap/inflation_layer/parameter_updates [dynamic_reconfigure/Config]
 # * /move_base/local_costmap/obstacle_layer_footprint/parameter_updates [dynamic_reconfigure/Config]
 # * /move_base/global_costmap/static_layer/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 #---- * /move_base/local_costmap/costmap_updates [map_msgs/OccupancyGridUpdate]
 #----------------------------------- * /move_base/NavfnROS/plan [nav_msgs/Path]
 # * /move_base/local_costmap/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 #------------------ * /move_base/parameter_updates [dynamic_reconfigure/Config]
 #------------------------- * /move_base/status [actionlib_msgs/GoalStatusArray]
 # * /move_base/global_costmap/inflation_layer/parameter_updates [dynamic_reconfigure/Config]
 #----------------- * /move_base/global_costmap/costmap [nav_msgs/OccupancyGrid]
 # * /move_base/global_costmap/obstacle_layer/clearing_endpoints [sensor_msgs/PointCloud]
 # * /move_base/local_costmap/obstacle_layer_footprint/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 #---- * /move_base/local_costmap/parameter_updates [dynamic_reconfigure/Config]
 # * /move_base/local_costmap/obstacle_layer_footprint/footprint_stamped [geometry_msgs/PolygonStamped]
 # * /move_base/TrajectoryPlannerROS/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 #------------------------------------------------ * /rosout [rosgraph_msgs/Log]
 # * /move_base/local_costmap/obstacle_layer/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 # * /move_base/global_costmap/obstacle_layer_footprint/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 # * /move_base/local_costmap/obstacle_layer/parameter_updates [dynamic_reconfigure/Config]
 # * /move_base/local_costmap/obstacle_layer/clearing_endpoints [sensor_msgs/PointCloud]
 #----------------- * /move_base/TrajectoryPlannerROS/local_plan [nav_msgs/Path]
 #------- * /move_base/TrajectoryPlannerROS/cost_cloud [sensor_msgs/PointCloud2]
 #----------------------- * /mobile_base/commands/velocity [geometry_msgs/Twist]
 # * /move_base/global_costmap/inflation_layer/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 # * /move_base/global_costmap/obstacle_layer/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 # * /move_base/TrajectoryPlannerROS/parameter_updates [dynamic_reconfigure/Config]
 #------------------------ * /move_base/goal [move_base_msgs/MoveBaseActionGoal]
 #---------------- * /move_base/TrajectoryPlannerROS/global_plan [nav_msgs/Path]
 # * /move_base/global_costmap/obstacle_layer_footprint/parameter_updates [dynamic_reconfigure/Config]
 # * /move_base/global_costmap/obstacle_layer/parameter_updates [dynamic_reconfigure/Config]
 # * /move_base/global_costmap/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
#------------------------------------------------------------------------------ 
#---------------------------------------------------------------- Subscriptions:
 #-------------------------- * /move_base/local_costmap/footprint [unknown type]
 #--------------------------------------------------- * /tf [tf2_msgs/TFMessage]
 #-------------------------------------------------- * /odom [nav_msgs/Odometry]
 #------------------------- * /move_base_simple/goal [geometry_msgs/PoseStamped]
 #-------------------------------------------------- * /tf_static [unknown type]
 #---------------------------------------------- * /map [nav_msgs/OccupancyGrid]
 #------------------------- * /move_base/global_costmap/footprint [unknown type]
 #------------------------ * /move_base/goal [move_base_msgs/MoveBaseActionGoal]
 #------------------------------------------- * /move_base/cancel [unknown type]
#------------------------------------------------------------------------------ 
#--------------------------------------------------------------------- Services:
 #---------------------- * /move_base/global_costmap/static_layer/set_parameters
 #----------------------------------------------------- * /move_base/get_loggers
 #---------------------------------------------- * /move_base/NavfnROS/make_plan
 #-------------------- * /move_base/global_costmap/obstacle_layer/set_parameters
 #------------------------------------ * /move_base/local_costmap/set_parameters
 #------------------------------------------------ * /move_base/set_logger_level
 #----------- * /move_base/local_costmap/obstacle_layer_footprint/set_parameters
 #--------------------- * /move_base/local_costmap/obstacle_layer/set_parameters
 #------------------- * /move_base/global_costmap/inflation_layer/set_parameters
 #----------------------------- * /move_base/TrajectoryPlannerROS/set_parameters
 #---------- * /move_base/global_costmap/obstacle_layer_footprint/set_parameters
 #-------------------------------------------------- * /move_base/clear_costmaps
 #----------------------------------- * /move_base/global_costmap/set_parameters
 #------------------------------------------------------- * /move_base/make_plan
 #-------------------- * /move_base/local_costmap/inflation_layer/set_parameters
 #-------------------------------------------------- * /move_base/set_parameters
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#--------------------------------------- contacting node http://LTS14:55315/ ...
#--------------------------------------------------------------------- Pid: 5137
#------------------------------------------------------------------ Connections:
 #------------------------------------------------------------- * topic: /rosout
    #------------------------------------------------------------- * to: /rosout
    #----------------------------------------------------- * direction: outbound
    #------------------------------------------------------- * transport: TCPROS
 #-------------------------------------- * topic: /mobile_base/commands/velocity
    #---------------------------------------- * to: /mobile_base_nodelet_manager
    #----------------------------------------------------- * direction: outbound
    #------------------------------------------------------- * transport: TCPROS
 #----------------------------------------------------- * topic: /move_base/goal
    #---------------------------------------------------------- * to: /move_base
    #----------------------------------------------------- * direction: outbound
    #------------------------------------------------- * transport: INTRAPROCESS
 #----------------------------------- * topic: /move_base/global_costmap/costmap
    #--------------------------------------------------------------- * to: /rviz
    #----------------------------------------------------- * direction: outbound
    #------------------------------------------------------- * transport: TCPROS
 #--------------------------- * topic: /move_base/global_costmap/costmap_updates
    #--------------------------------------------------------------- * to: /rviz
    #----------------------------------------------------- * direction: outbound
    #------------------------------------------------------- * transport: TCPROS
 #-------------------------------------------- * topic: /move_base/NavfnROS/plan
    #--------------------------------------------------------------- * to: /rviz
    #----------------------------------------------------- * direction: outbound
    #------------------------------------------------------- * transport: TCPROS
 #------------------------------------ * topic: /move_base/local_costmap/costmap
    #--------------------------------------------------------------- * to: /rviz
    #----------------------------------------------------- * direction: outbound
    #------------------------------------------------------- * transport: TCPROS
 #---------------------------- * topic: /move_base/local_costmap/costmap_updates
    #--------------------------------------------------------------- * to: /rviz
    #----------------------------------------------------- * direction: outbound
    #------------------------------------------------------- * transport: TCPROS
 #------------------------- * topic: /move_base/TrajectoryPlannerROS/global_plan
    #--------------------------------------------------------------- * to: /rviz
    #----------------------------------------------------- * direction: outbound
    #------------------------------------------------------- * transport: TCPROS
 #----------------------------------------------------------------- * topic: /tf
    #------------------ * to: /mobile_base_nodelet_manager (http://LTS14:38415/)
    #------------------------------------------------------ * direction: inbound
    #------------------------------------------------------- * transport: TCPROS
 #----------------------------------------------------------------- * topic: /tf
    #---------------------------- * to: /fake_localization (http://LTS14:35856/)
    #------------------------------------------------------ * direction: inbound
    #------------------------------------------------------- * transport: TCPROS
 #----------------------------------------------------------------- * topic: /tf
    #------------------------ * to: /robot_state_publisher (http://LTS14:53509/)
    #------------------------------------------------------ * direction: inbound
    #------------------------------------------------------- * transport: TCPROS
 #---------------------------------------------- * topic: /move_base_simple/goal
    #----------------------------------------- * to: /rviz (http://LTS14:33963/)
    #------------------------------------------------------ * direction: inbound
    #------------------------------------------------------- * transport: TCPROS
 #---------------------------------------------------------------- * topic: /map
    #----------------------------------- * to: /map_server (http://LTS14:52408/)
    #------------------------------------------------------ * direction: inbound
    #------------------------------------------------------- * transport: TCPROS
 #--------------------------------------------------------------- * topic: /odom
    #------------------ * to: /mobile_base_nodelet_manager (http://LTS14:38415/)
    #------------------------------------------------------ * direction: inbound
    #------------------------------------------------------- * transport: TCPROS
 #----------------------------------------------------- * topic: /move_base/goal
    #------------------------------------ * to: /move_base (http://LTS14:55315/)
    #------------------------------------------------------ * direction: inbound
    #------------------------------------------------- * transport: INTRAPROCESS



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


def myCoolFn(data):
    print("myCoolFn received: {}".format(data))
    nd.write('mobile_base/commands/velocity', data )
    
def alterVelocity(data):
    #print("myFn1 received: {}, sending it".format(data))
    #rostopic pub -1 /mobile_base/commands/velocity geometry_msgs/Twist '{linear:  {x: 1, y: 0.0, z: 5.5}, angular: {x: 0.0,y: 0.0,z: 0.5}}'

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
nd.new.subscribe(topic = "cmd_vel",handler = alterVelocity, msgType = Twist)
      .publish(topic = "mobile_base/commands/velocity", msgType = Twist)
}


#-------------------------- * /move_base/local_costmap/footprint [unknown type]
 #--------------------------------------------------- * /tf [tf2_msgs/TFMessage]
 #-------------------------------------------------- * /odom [nav_msgs/Odometry]
 #------------------------- * /move_base_simple/goal [geometry_msgs/PoseStamped]
 #-------------------------------------------------- * /tf_static [unknown type]
 #---------------------------------------------- * /map [nav_msgs/OccupancyGrid]
 #------------------------- * /move_base/global_costmap/footprint [unknown type]
 #------------------------ * /move_base/goal [move_base_msgs/MoveBaseActionGoal]
 #------------------------------------------- * /move_base/cancel [unknown type]


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