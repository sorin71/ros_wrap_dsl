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

        self.nextValidCall = None
        self.passedData = None
        #re-mapping method calls to variables
        self.Publish = self.publish()
        self.Subscribe = self.subscribe()
        if type == 'reuse' or type == 'new':
            self.subsDict['type'] = type
        else:
            print ("error: the node type could only be '''new''' or '''reuse'''; passed: '''{}'''".format(type))
            
    
    #aid method used to force a specific call after
    def setNext(self,nextValidCall,data = None):
        self.nextValidCall = nextValidCall
        self.passedData = data
    
    #aid method used to force a specific call after    
    def isValidCall(self,crtCall):
        isValid = (self.nextValidCall == crtCall)
        if not isValid:
            print ('error: expected previous call {} instead of {}'.format(self.nextValidCall, crtCall))
        self.nextValidCall = None  #reset variable, function called
        return isValid
    
    def subscribe(self):
        self.setNext("topic","subscribe")
        #print "subscribe"
        return self
    
    def handler(self,fn):
        
        self.subsDict['fn']=fn
        #if self.subsDict['type']=='new':
        #    elem = self.subsDict.copy()
        #    self.subscribeTopics.append(elem)
        #else:
        #    print("error: register a handler available only for '''new''', not for ''''{}'''".format(self.subsDict['type']) )

        return self
    
    def msgType(self,msg):

        self.publDict['msg']=msg
        if self.publDict['type']=='new':
            elem = self.publDict.copy()
            self.publishTopics.append(elem)
        else:
            print("error: register a message type available only for '''new''', not for ''''{}'''".format(self.publDict['type']) )

        return self
    
    def publish(self):
        self.setNext("topic","publish")
        return self
    
    def topic(self, topicName):
        if not self.isValidCall("topic"):
            return self
        
        if self.passedData == "subscribe":
            self.subsDict['name']=topicName
            if self.subsDict['type']=='reuse':
                elem = self.subsDict.copy()
                self.subscribeTopics.append(elem)
        elif self.passedData == "publish":
            self.publDict['name']=topicName
            if self.publDict['type']=='reuse':
                elem = self.publDict.copy()
                self.publishTopics.append(elem)
        else: 
            print ("error: expected topic passed data subscribe or published but received {} ".format(self.passedData))
        self.passedData = None
        
        return self

 #     "\n(next val. call)   : ", self.nextValidCall, \
 #     "\n(passed data)      : ", self.passedData 


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
        #remapping method calls to variables
        #self.Publish = self.publish()
        #self.Subscribe = self.subscribe()
         
        

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
            if item == None:
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

