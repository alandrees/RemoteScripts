#########################
#### AbletonPlus Implementation
#### Version 2
####
#### Just provides the communication protocol and standards to use this system, leaves the actual implementation up to the controller (client) scripts
#### Removes inheritence dependence, and makes use of class composition instead.

import Live
from _AbletonPlus.Master import Master
from _AbletonPlus.Options import Options

class AbletonPlus():

    _master = None #class instance of a 
    _enabled_devices = [] #provides a list of all abletonplus enabled controller scripts
    _event_callbacks = dict() #dictionary list of events that can be fired and need to be updated on the other controllers
    _getter_callbacks = dict() #dictionary list of getter functions that can be fired
    _setter_callbacks = dict() #dictionary list of setter functions that can be fired
    _master_track_offset = 0 #depreciated, used for poc
    _master_scene_offset = 0 #depreciated, used for poc
    


    def _connect_active_instances(caller,master = False):
        """this function adds an abletonplus instance to the list, and will add the master if neccicary"""
        if(caller != None):
            _enabled_devices.append(caller)
            if master == True:
                if AbletonPlus._master == None:
                    AbletonPlus._master == caller
                else:
                    assert"duplicate master designations, please check your configs")

    _connect_active_instances = staticmethod(_connect_active_instances)        

#        if(isinstance(caller._master, Master) and isinstance(AbletonPlus._master, NoneType)):
#            for instance in AbletonPlus._enabled_devices:
#                instance.notify_connect(caller)
#            return None
#        else:
#            assert("duplicate master designations, please check your configs")
        
        

    
#    def _disconnect_instance(self):
#        i = AbletonPlus._enabled_devices.index(self)
#        AbletonPlus._enabled_devices.pop(i)
#        return None
    
    def __init__(self,instance,options,callbacks):
        self._instance = instance
        self._options = options
        return None

    
    
    def enable_abletonplus(self):
        """instance: controller instance, options: options"""
        AbletonPlus._connect_active_instances(self.instance, self._options["master"])
        self.register_callbacks(self._options.callbacks)

    def disable_abletonplus(self):
        i = AbletonPlus._enabled_devices.index(self)
        AbletonPlus._enabled_devices.pop(i)
        
    def register_callbacks(self,callbacks):
        for event in callbacks[0]:
            for k in event:
                if k in AbletonPlus._event_callbacks:
                    AbletonPlus._event_callbacks[k].append(event[k])
                else:
                    AbletonPlus._event_callbacks.append[k]
                    AbletonPlus._event_callbacks.append[k].append(event[k])
        for getters in callbacks[1]:
            for k in getters:
                if k in AbletonPlus._getter_callbacks:
                    AbletonPlus._getter_callbacks[k].append(getters[k])
                else:
                    AbletonPlus._getter_callbacks.append[k]
                    AbletonPlus._getter_callbacks.append[k].append(getters[k])

        for setters in callbacks[2]:
            for k in setters:
                if k in AbletonPlus._setter_callbacks:
                    AbletonPlus._setter_callbacks[k].append(setters[k])
                else:
                    AbletonPlus._setter_callbacks.append[k]
                    AbletonPlus._setter_callbacks.append[k].append(setters[k])

            
    def configure_ableton_plus(self):
        assert("Virtual Method... overload this bitch!")
   
    def notify_connect(self, caller):
        assert("Virtual Method... we require more Overloads!")
        
    def notify_disconnect(self, caller):
        assert("Virtual Method... O V E R L O A D")


        #depreciated for poc#
    def get_track_offset():
        return AbletonPlus._master_track_offset
    
    get_track_offset = staticmethod(get_track_offset)
        
    def get_scene_offset():
        return AbletonPlus._master_scene_offset
    
    get_scene_offset = staticmethod(get_scene_offset)
        ######################

    def is_master(self):
        return self._master
        
    def is_not_master(self):
        return not self._master
        
