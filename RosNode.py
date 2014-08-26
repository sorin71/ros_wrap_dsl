#!/usr/bin/python
 
import types
 
from rosObjects import subscriber, publisher, node
#execfile('/home/sorin/roswork_FRSC2014/src/EnhanceRosNode/rosObjects.py')



class topicHandler:
    
    def __init__(self, type):
        self.subscribeTopics = []
        self.publishTopics = []
        self.subsDict = {'name': None,'fn': None,'msg':None,'type':type}
        self.publDict = {'name': None,'msg': None,'type':type}

        if type == 'reuse' or type == 'new':
            self.subsDict['type'] = type
        else:
            print ("error: the node type could only be '''new''' or '''reuse'''; passed: '''{}'''".format(type))
 
    def correctArgs(self,allowedParams, args ):
        correct_param = True
        if len(args) == len(allowedParams):
            for k in allowedParams:
                if k not in args:
                    correct_param = False
            if correct_param is False :
                print "error: incorrect parameters provided for subscribe, expected: ", allowedParams

        else:
            print "error: incorrect number of parameters provided for subscribe"
            correct_param = False
        
        return correct_param
        
    #the only function
    #def subscribe(self, **kwargs):
        #print "subscribe"
        
     #   if self.subsDict['type']=='reuse':
     #       allowedParams = ['topic']
     #   else: #'new'
     #       allowedParams = ['topic', 'handler', 'msgType']
        
     #   if self.correctArgs(allowedParams, kwargs):
            
     #       topic = kwargs['topic']
     #       handler = kwargs['handler']
     #       msgType = kwargs['msgType']

    def subscribe(self,topic,handler = None, msgType = None):    
       
        self.subsDict['name']=topic
        self.subsDict['fn']= handler
        self.subsDict['msg']=msgType
        
        if self.subsDict['type']=='reuse':
            if msgType is not None or handler is not None:
                print ("error: subscribe reuse should have a handler and a msgType provided: ")       
                print "topic: ", topic
            
        else:
       
            if msgType is None or handler is None:
                print ("error: subscribe new has no handler or msgType; provided: {} {}".format(handler, msgType ))       
                print "topic: ", topic

        elem = self.subsDict.copy()
        self.subscribeTopics.append(elem)

        return self   
  
    #the only function
    def publish(self,topic, msgType = None):
              
        self.publDict['name']=topic
        self.publDict['msg']=msgType
        
        if self.publDict['type']=='new':
            
            if msgType == None:
                print ("error: publish new should have a msgType provided: ")       
            
        else: 
            if msgType is not None:
                print ("error: publish reuse has no msgType; provided: {} ".format(msgType))       

        elem = self.publDict.copy()
        self.publishTopics.append(elem)

        return self


class rosNode:
    'Common base class for ROS node and sub-node'
          
    def varInit(self):
        self.newRosNodeName = None
        self.baseRosPackage = None
        self.baseRosNodeName = None
        self.reuse = topicHandler('reuse')
        self.new = topicHandler('new')
        self.publisher = []
        self.subscriber = []
        self.publHandler = {'Topic': None,'Handler': None}
        self.node = node()        
        

    def __init__(self, newRosNodeName):
        self.varInit()   
        self.newRosNodeName = newRosNodeName
    
    def basePackage(self, baseRosPackage):
        self.baseRosPackage = baseRosPackage
        return self
    
    def baseNode(self, baseRosNodeName):
        self.baseRosNodeName = baseRosNodeName
        return self 
     
    def __createNewPublishers(self):
        for item in self.new.publishTopics:
            #print item
            if item is None:
                print"error: empty list of new publishers"
                return
            
            topic = item['name']
            msgType = item['msg']
            print "topic", topic
            pub = publisher()
            hnd = pub.registerToPublish(topic,msgType)
            pub.pub= hnd
            pair = {'publisher':pub,'topic':topic}
            self.publisher.append(pair) 
                       
        #self.publHandler = {'Topic': None,'Handler': None}
            
    
    def __createNewSubscribers(self):
        for item in self.new.subscribeTopics:
            #print item
            if item == None:
                print"error: empty list of new publishers"
                return
            
            topic = item['name']
            fn = item['fn']
            msg = item['msg']
            
            subs = subscriber()
            subs.registerReadFn(fn)
            subs.subscribeTo(topic, msg)
            
            pair = {'subscriber':subs,'topic':topic} 
            self.subscriber.append(pair)                                   
            #self.subsDict = {'name': None,'fn': None,'type':type}       
    
    def __relayPublishers(self):
        for i in self.reuse.publishTopics:
            print i
    
    def __relaySubscribers(self):
        for i in self.reuse.subscribeTopics:
            print i
    
    def create(self):
        self.node.createNode(self.newRosNodeName)         
        self.__createNewPublishers()   
        self.__createNewSubscribers()
        self.__relayPublishers()
        self.__relaySubscribers() 
               

    def printNode(self): 
        print   "\nNew node name : ", self.newRosNodeName, \
                "\nBase package  : ", self.baseRosPackage, \
                "\nBase node     : ", self.baseRosNodeName, \
                "\n           reuse topic(s):", \
                "\nsubscribe topics : ", self.reuse.subscribeTopics, \
                "\npublish topics   : ", self.reuse.publishTopics, \
                "\n           new topic(s):", \
                "\nsubscribe topics : ", self.new.subscribeTopics, \
                "\npublish topics   : ", self.new.publishTopics, \
                "\nPublish topics handlers   : ", self.publisher, \
                "\nSubscribe topics    : ", self.subscriber, \


  


#call(["rosrun " + NewNode.baseRosPackage + " " + NewNode.baseRosNodeName, ""])

