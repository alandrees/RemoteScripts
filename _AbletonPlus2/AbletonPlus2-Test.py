from AbletonPlus import *
class testclass():
   
    def __init__(self):
        #print "init"
        self.ap = AbletonPlus(self,{"master": False,"callbacks": [{"ap_add":self.ap_add,"ap_remove":self.ap_rem,"event1":self.event1,"event2":self.event2, "event22":self.event22,"testevent":self.testevent1},{"get1":self.get1},{"set1":self.set1}]})

    def ap_add(self,sender, event, **kwargs):
        #this function gets called when an object gets enabled
        #print sender
        #print event
        #print kwargs
        print "testclass1, event recieved, AbletonPlus enabled for a new object"

    def ap_rem(self, sender, event, **kwargs):
        #this function gets called when an object gets 
        #print sender
        #print event
        #print kwargs
        print "testclass1, event recieved, AbletonPlus disabled for an existing object\n\n"

    def event1(self,sender, event, **kwargs):
        print "event1"

    def event2(self,sender, event, **kwargs):
        print "event2"

    def event22(self,sender, event, **kwargs):
        print "event22 - testclass"

    def testevent1(self,sender,event,**kwargs):
        print "testevent1"

    def get1(self, sender, getter, **kwargs):
        return "testclass getter get 1 reporting for duty"

    def set1(self, sender, setter, **kwargs):
        print "set1"

class testclass2():
    def __init__(self):
        #print "init2"
        self.ap = AbletonPlus(self,{"master": False,"callbacks": [{"ap_add":self.ap_add,"ap_remove":self.ap_rem,"event21":self.event21,"event22":self.event22,"testevent":self.testevent2},{"get2":self.get21},{"set1":self.set21}]})

    def ap_add(self,sender, event, **kwargs):
        #this function gets called when an object gets enabled
        #print sender
        #print event
        #print kwargs
        print "testclass2, event recieved, AbletonPlus enabled for a new object"

    def ap_rem(self,sender,event, **kwargs):
        #this function gets called when an object gets 
#        print sender
#        print event
#        print kwargs
        print "testclass2, event recieved, AbletonPlus disabled for an existing object\n\n"

    def event21(self,sender, event, **kwargs):
        print "event2-1"

    def event22(self,sender, event, **kwargs):
        print "event22 -testclass 2"

    def testevent2(self,sender,event,**kwargs):
        print "testevent2"

    def get21(self, sender, getter, **kwargs):
        return "testclass2 getter get 1 reporting for duty"

    def set21(self, sender, setter, **kwargs):
        print "set2-1"

class testclass3():
    def __init__(self):
        #print "init2"
        self.ap = AbletonPlus(self,{"master": False,"callbacks": [{"ap_add":self.ap_add,"ap_remove":self.ap_rem,"event31":self.event31,"event22":self.event22,"testevent":self.testevent3},{"get3":self.get31},{"set1":self.set31}]})

    def ap_add(self,sender, event, **kwargs):
        #this function gets called when an object gets enabled
        #print sender
        #print event
        #print kwargs
        print "testclass3, event recieved, AbletonPlus enabled for a new object"

    def ap_rem(self,sender,event, **kwargs):
        #this function gets called when an object gets 
        print sender
        print event
        print kwargs
        print "testclass3, event recieved, AbletonPlus disabled for an existing object\n\n"

    def event31(self,sender, event, **kwargs):
        print "event3-1"

    def event22(self,sender, event, **kwargs):
        print "event22 - testclass3"

    def testevent3(self,sender,event,**kwargs):
        print "testevent3"

    def get31(self, sender, getter, **kwargs):
        return "testclass3 getter get 1 reporting for duty"
    
    def set31(self, sender, setter, **kwargs):
        print "set3-1"


a = testclass()       
b = testclass2()
c = testclass3()
def inita():
    a.ap.enable_abletonplus()

def initb():
    b.ap.enable_abletonplus()

def initc():
    c.ap.enable_abletonplus()

inita()
initb()
initc()
