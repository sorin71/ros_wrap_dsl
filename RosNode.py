#!/usr/bin/python
 
import types

from rospy.msg import AnyMsg
#import threading
#from std_msgs.msg import String
 
from rosObjects import subscriber, publisher, node
from subprocess import call
from os import environ
#from subprocess import Popen, PIPE
#from subprocess import communicate
#from subprocess import wait
#reload(subscriber)
#reload(publisher)
#reload(node)

class topicHandler:
    
    def __init__(self, type):
        self.subscribeTopics = []
        self.publishTopics = []
        self.updateNode = False
        #self.relayHandler = None
        self.subsDict = {'name': None,'msg': None,'type':type,'fn': None, 'hdl': None}
        self.publDict = {'name': None,'msg': None,'type':type,'hdl': None}

        if type == 'reuse' or type == 'new':
            self.subsDict['type'] = type
        else:
            print ("error: the node type could only be '''new''' or '''reuse'''; passed: '''{}'''".format(type)) 

    def delayedUpdate(self,delayed):
        self.updateNode = not delayed
        
    def __createSubscriber(self,item):
        topic = item['name']
        fn = item['fn']
        msg = item['msg']
        
        subs = subscriber()
        subs.registerReadFn(fn)
        hndl = subs.subscribeTo(topic, msg)
        item['hdl'] = hndl                               
        
    def subscribe(self,topic,handler = None, msgType = None ):   

        if self.updateNode is True:
            i=0
            item = None
            for item in self.subscribeTopics:
                if item['name'] is topic:
                    break
                i=i+1
            
            if item is not None:   
                self.subscribeTopics.pop(i)
 
       
        self.subsDict['name']=topic
        self.subsDict['fn']= handler
        self.subsDict['msg']=msgType
        
        if self.subsDict['type']=='reuse':
            #if msgType is not None or handler is not None:
            if  handler is not None:
                print ("error: subscribe reuse should have a handler and a msgType provided: ")       
                print "topic: ", topic
            #self.subsDict['msg']=AnyMsg #prepare message for relaying
               
        elif msgType is None or handler is None:
            print ("error: subscribe new has no handler or msgType; provided: {} {}".format(handler, msgType ))       
            print "topic: ", topic
            
        if self.updateNode is True:
            subs = subscriber()
            subs.registerReadFn(handler)
            hndl = subs.subscribeTo(topic, msgType)
            self.subsDict['hdl'] = hndl                               

        elem = self.subsDict.copy()
        self.subscribeTopics.append(elem)


        return self   
  
    def publish(self,topic, msgType = None):
              
        self.publDict['name']=topic
        self.publDict['msg']=msgType
        
        if self.publDict['type']=='new':
            
            if msgType == None:
                print ("error: publish new should have a msgType provided: ")       
            
        #else: 
            #if msgType is not None:
            #    print ("error: publish reuse has no msgType; provided: {} ".format(msgType))       
            #self.publDict['msg'] = AnyMsg
            
        elem = self.publDict.copy()
        self.publishTopics.append(elem)

        return self

def externalNodeLaunch(cmdLine):
    call(cmdLine , shell=True)
    #call("rosrun turtlesim turtlesim_node" , shell=True)
    
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
        #self.publHandler = {'Topic': None,'Handler': None}
        self.node = node()   
        self.created = False
        

    def __init__(self, newRosNodeName):
        self.varInit()   
        self.newRosNodeName = newRosNodeName
    
    def basePackage(self, baseRosPackage):
        self.baseRosPackage = baseRosPackage
        return self
    
    def baseNode(self, baseRosNodeName):
        self.baseRosNodeName = baseRosNodeName
        return self 
    
    #def read(self,topic): #not needed, the callback function is doing that
    #    pass
    
    def write(self,topic,data):
        for item in self.new.publishTopics:
            if item['name'] is topic:
                break
        handler = item['hdl'] 
        handler.publish(data)
        
    def update(self,topic):
        for item in self.new.subscribeTopics:
            if item['name'] is topic:
                break
        self.__createSubscriber(item)
        
    def unsubscribe(self,topic):
        i=0
        for item in self.new.subscribeTopics:
            if item['name'] is topic:
                break
            i=i+1
            
        handler = item['hdl'] 
        self.new.subscribeTopics.pop(i)
        
        handler.unregister()
        
    
    def __genRelayTopic(self,topic):
        return 'relay_' + topic
  
    def __relay(self, subscribingTo, pubishingTo, msgType):                               
        subs = subscriber()
        publ = publisher()
                         
        publTopic = pubishingTo
        subsTopic = subscribingTo
        msg = msgType
        fn = publ.relayFn
        #fn = publ.write
        
        publHandler = publ.registerToPublish(publTopic, msg)
        subs.registerReadFn(fn)
        #print "debug: ", publTopic, msg, fn
        hndl = subs.subscribeTo(subsTopic, msg)
        
        
        dictItems = {'subscriber':hndl,'in_topic':subsTopic, 'out_topic':publTopic} 
        self.subscriber.append(dictItems) 
        
        return hndl                                  
     

     
    def __createNewPublishers(self):
        for item in self.new.publishTopics:
            if item is None:
                print"error: empty list of new publishers"
                return
            
            topic = item['name']
            msgType = item['msg']
            #print "topic", topic
            pub = publisher()
            hnd = pub.registerToPublish(topic,msgType)
            pub.pub= hnd
            item['hdl'] = hnd
            #pair = {'publisher':pub,'topic':topic}
            #self.publisher.append(pair) 
  
    def __createSubscriber(self,item):
        topic = item['name']
        fn = item['fn']
        msg = item['msg']
        
        subs = subscriber()
        subs.registerReadFn(fn)
        hndl = subs.subscribeTo(topic, msg)
        item['hdl'] = hndl                                      
    
    def __createNewSubscribers(self):
        for item in self.new.subscribeTopics:
            if item == None:
                print"error: empty list of new subscribers"
                return
            self.__createSubscriber(item)
            
            
            #pair = {'subscriber':subs,'topic':topic} 
            #self.subscriber.append(pair)    
            
    def __relayPublishers(self):
        for item in self.reuse.publishTopics:
            #print item
            publTopic = item['name']
            subsTopic = self.__genRelayTopic(publTopic)
            msg = item['msg']
            hndl = self.__relay(subsTopic, publTopic, msg) 
            item['hdl'] = hndl                             
            
    def __relaySubscribers(self):
        for item in self.reuse.subscribeTopics:
            #print item
            subsTopic = item['name']
            publTopic = self.__genRelayTopic(subsTopic)
            msg = item['msg']
            hndl = self.__relay(subsTopic, publTopic, msg) 
            item['hdl'] = hndl      
            
    def __generateCmdLine(self):
        #rosrun <package> <executable>
        #rename __name:=new_name
        #cmdLine = '"'
        cmdLine = ''
        cmdLine += 'rosrun ' + self.baseRosPackage + " " + self.baseRosNodeName + " "     
        #remap the publishing topics
        for item in self.reuse.publishTopics:
            topic = item['name']
            renamed = self.__genRelayTopic(topic)       
            cmdLine += topic + ":=" + renamed + " "
        #remap the subscribe topics
        for item in self.reuse.subscribeTopics:
            topic = item['name']
            renamed = self.__genRelayTopic(topic)
            cmdLine += topic + ":=" + renamed + " " 
        #cmdLine += ' "'
        print cmdLine
        return cmdLine
  
    def __launchBaseNode(self):     
        rosCmdLine = self.__generateCmdLine()
        
        #the below trick requires to include the following code at the end of ~/.bashrc:
        #    eval "$BASH_POST_RC"
        
        #termCmdLine = '"'+"BASH_POST_RC=\''sdu;" + rosCmdLine + "'\''; exec bash'" + '"'
        
        #termCmdLine = "'BASH_POST_RC=\''sdu; rosrun rospy_tutorials talker chatter:=/relay_chatter '\''; exec bash''"
        
        
        environ["BASH_POST_RC"] = 'sdu'
        print environ["BASH_POST_RC"]
        
        #cmd = "rosrun rospy_tutorials talker chatter:=/relay_chatter "
        #call(['gnome-terminal', '-x', 'sh', '-c', rosCmdLine])

        
        print rosCmdLine
        call(['gnome-terminal', '-x', 'sh', '-c',rosCmdLine])
        
        #call(['gnome-terminal', '-x', 'sh', '-c', "BASH_POST_RC=\''sdu; rosrun turtlesim turtlesim_node '\''; exec bash'"])
        #call(['gnome-terminal', '-x', 'sh', '-c', string(termCmdLine]))
        #call(['gnome-terminal', '-x', 'sh', '-c', "BASH_POST_RC=\''sdu; rosrun rospy_tutorials talker chatter:=/relay_chatter '\''; exec bash'"])
        #rosrun rospy_tutorials talker chatter:=/wg/chatter
        #call(['gnome-terminal', '-x', 'sh', '-c', "BASH_POST_RC=\''sdu;rosrun turtlesim turtlesim_node turtle1/color_sensor := relay_turtle1/color_sensor turtle1/pose := relay_turtle1/pose turtle1/cmd_vel := relay_turtle1/cmd_vel '\''; exec bash'"])
        #externalNodeLaunch(cmdLine)
        
        #call(cmdLine , shell=True)
        #p = Popen("/home/sorin/roswork_FRSC2014/devel/setup.sh", shell=True, stdin=PIPE)
        #p.communicate(cmdLine)
        #t = threading.Thread(target=self.__cmdLineFn, shell=True)
        #t.start()
                
    def create(self):
        self.node.createNode(self.newRosNodeName)         
        self.__createNewPublishers()   
        self.__createNewSubscribers()
        self.__relayPublishers()
        self.__relaySubscribers() 
        if self.baseRosNodeName is not None:
            self.__launchBaseNode()
        #from now on, any new topic change will take effect right away
        #self.new.updateNode = True
        self.new.delayedUpdate(False)

        
               

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

