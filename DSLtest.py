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

from std_msgs.msg import String

nd = rosNode("NewNode")

def myFn(data):
    print("received: {}, sending it".format(data))
    nd.write(data)
    
def myFn1(data):
    print("received: {}, sending it".format(data))
    nd.write(data)
    
def myFn2(data):
    print("received: {}, sending it".format(data))
    nd.write(data)

    
def myRunFn():
    nd.read()
    print "run "
        
def myNewRun():
    print "new"


nd.basePackage("NodePackage")\
  .baseNode("BaseNode") 
  
{
nd.reuse.subscribe(topic = "irTopic1")
        .subscribe(topic = "irTopic2")
        .publish(topic = "orTopic1")
        .publish(topic = "orTopic2")
}

{
nd.new.subscribe(topic = "inTopic1",handler = myFn1,msgType = String)
      .subscribe(topic = "inTopic2",handler = myFn2,msgType = String)
      .publish(topic = "onTopic1", msgType = String)
      .publish(topic = "onTopic2", msgType = String)
}

nd.create()

#nd.onTopic("onTopic1").publish("test message")
  
nd.printNode()