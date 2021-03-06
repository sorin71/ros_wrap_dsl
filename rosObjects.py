# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 09:21:10 2014

@author: sorin
"""

#import sys
#import time
#sys.path.append("~/roswork_FRSC2014/src/EnhanceRosNode")

#import ~/roswork_FRSC2014/src/EnhanceRosNode/rosObjects

#execfile('/home/sorin/roswork_FRSC2014/src/EnhanceRosNode/rosObjects.py')

#AnyMsg deserialize serialize

import rospy



class subscriber():
    def __init__(self):
        self.subscribedTopic = ''
        self.subscribedMsgType = ''
        self.callBackFn = None
        
    def subscribeTo(self,topic,msgType):
        self.subscribedTopic = topic
        self.subscribedMsgType = msgType
        subsHnd = rospy.Subscriber(self.subscribedTopic, self.subscribedMsgType, self.callBackFn)
        return subsHnd
 
    def registerReadFn(self,fn):
        self.callBackFn = fn
        
    def updateSubscribeFn(self):
        if self.callBackFn != None:
            subsHnd = rospy.Subscriber(self.subscribedTopic, self.subscribedMsgType, self.callBackFn)
            return subsHnd
        else:
            print "A callback function must be registered first (use registerReadFn)"
    
#    def relayFn(self,data):
#        self.handler.write(data)

    
    #def unsubscribe(self):
        #rospy.Subscriber.unregister(self)
    
    def printSubs(self):
        print   "\nSubscribed topic : ", self.subscribedTopic, \
                "\nSubscribed msg type  : ", self.subscribedMsgType, \
                "\nCallback fn  : ", self.callBackFn, \
 
     
class publisher():
    def __init__(self, relayHandler = None):
        self.publishingTopic = ''
        self.publishingMsgType = ''
        self.handler = None  
        #self.relayHandler = relayHandler  
          
    def registerToPublish(self,topic,msgType): 
        self.publishingTopic = topic
        self.publishingMsgType = msgType
        self.handler = rospy.Publisher(self.publishingTopic, self.publishingMsgType, queue_size= 10)
        return self.handler
   
    def write(self,data):
        self.handler.publish(data)
        

    #def unsubscribe(self):
        #self.handler.unregister()
    def setRelayPublHandler(self,relayHandler):
        self.relayHandler = relayHandler

    def relayFn(self,data):
        #print "received data on topic ", self.publishingTopic, " sending it further..."
        self.write(data)
        #self.relayHandler.publish(data)
   
    #def relay(self):
    #    self.handler = self.registerToPublish(self.publishingTopic, self.publishingMsgType)

    def printPubl(self):
        print   "\nPublish to topic : ", self.publishingTopic, \
                "\nPublish msg type  : ", self.publishingMsgType, \
                "\nPublish handler  : ", self.handler, \

        
class node():
    def __init__(self):
         self.nodeRunFn = None    
         self.nodeName = ''
    
    def createNode(self,nodeName):
        rospy.init_node(nodeName, )
        
    def registerRunFn(self,fn):
        self.nodeRunFn = fn
 
    def printNode(self):
        print   "\nNode name : ", self.nodeName, \
       
    def loop(self):
      
        #self.createNode('test')
        while not rospy.is_shutdown():
            #if runFn:
            #    self.nodeRunFn = runFn
           
            self.nodeRunFn()
            #sys.stdout.flush()
         
            rospy.spin()
                
    def run(self):
            
        #t = threading.Thread(target=self.loop)
        #t.start()
        #if __name__ == '__main__':       
            #d = multiprocessing.Process(name='daemon', target=self.loop)
            #d.daemon = True
            #d.start()
            #d.terminate()
        pass

    
    
    