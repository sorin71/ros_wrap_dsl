# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 17:44:42 2014

@author: sorin
"""
#execfile('/home/sorin/roswork_FRSC2014/src/EnhanceRosNode/DSLtest.py')

import sys
sys.path.append("/home/sorin/roswork_FRSC2014/src/EnhanceRosNode")

#print sys.path

from RosNode import rosNode
#reload(rosNode)

from std_msgs.msg import String

nd = rosNode("NewNode")

def myCoolFn(data):
    msg = 'from the cool fn: ' + data
    print("myCoolFn received: {} but sending: {}".format(data,msg))
    nd.write('onTopic1', msg )
    
def myFn1(data):
    print("myFn1 received: {}, sending it".format(data))
    nd.write('onTopic1',data)
    
def myFn2(data):
    print("myFn2 received: {}, sending it".format(data))
    nd.write('onTopic2',data)   


nd.basePackage("NodePackage")\
  .baseNode("BaseNode") 
  
{
nd.reuse.subscribe(topic = "irTopic1",msgType = String)
        .subscribe(topic = "irTopic2",msgType = String)
        .publish(topic = "orTopic1",msgType = String)
        .publish(topic = "orTopic2",msgType = String)
}

{
nd.new.subscribe(topic = "inTopic1",handler = myFn1, msgType = String)
      .subscribe(topic = "inTopic2",handler = myFn2, msgType = String)
      .publish(topic = "onTopic1", msgType = String)
      .publish(topic = "onTopic2", msgType = String)
}

nd.create()

variable = raw_input("press enter for unsubscribe from inTopic1")

#replace a subscribed topic handler
nd.unsubscribe("inTopic1")

variable = raw_input("press enter for changing the handler function for inTopic1")
nd.new.subscribe(topic = "inTopic1",handler = myCoolFn, msgType = String)

print "myCoolFn is active for inTopic1"
#nd.onTopic("onTopic1").publish("test message")
  
#nd.printNode()