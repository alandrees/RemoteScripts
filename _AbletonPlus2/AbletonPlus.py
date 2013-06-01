#########################
#### Inter-Controller Communication Implementation
#### 2.0
#### Copyright 2013 Alan Drees
####
#### Purpose: Provides a way for all of the different script instances to notify eachother of events
####
#### Note: This library can be tested without involving live whatsoever, using the provided test environment
####       but it is designed for use with Ableton Live 8.3 Build 2012-03-29_4920da10f1.
####
#### This library is free software; you can redistribute it and/or modify it under the terms of the 
#### GNU Lesser General Public License as published by the Free Software Foundation; either version 
#### 2.1 of the License, or (at your option) any later version.
####
#### This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
#### without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
#### See the GNU Lesser General Public License for more details.
####
#### You should have received a copy of the GNU Lesser General Public License along with this library; if not, 
#### write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


import Live

class AbletonPlus():

    _master = None #class instance of the master (also exists in the _enabled_devices list)
    _enabled_devices = [] #provides a list of all abletonplus enabled controller scripts

    #dictionary list of events that can be fired and need to be updated on the other controllers
    #every implementation of abletonplus must have a valid ap_enabled, ap_disabled function
    _event_callbacks = {"ap_add":[],"ap_remove":[]}
    _getter_callbacks = dict() #dictionary list of getter functions that can be fired
    _setter_callbacks = dict() #dictionary list of setter functions that can be fired
    
    def _add_controller(caller,master = False):
        """this function adds an abletonplus instance to the list, and will add the master if neccicary"""
        if(caller != None):
            AbletonPlus._enabled_devices.append(caller)
            if master == True:
                if AbletonPlus._master == None:
                    AbletonPlus._master == caller
                else:
                    assert("duplicate master designations, please check your configs")

    _add_controller = staticmethod(_add_controller)

    def __init__(self,instance,options):
        self._instance = instance
        self._options = options
        return None  
    
    def enable_abletonplus(self):
        """instance: controller instance, options: options"""
        if self._instance not in AbletonPlus._enabled_devices:
            self.register_callbacks(self._options["callbacks"])
            AbletonPlus._add_controller(self._instance, self._options["master"])
            self.fire_event("ap_add",sender=self._instance,callbacks=self._options["callbacks"],ignore_self=True) #sends a notification that this controller has been enabled

    def disable_abletonplus(self):
        i = AbletonPlus._enabled_devices.index(self._instance)
        
        AbletonPlus._enabled_devices.pop(i)
        
    def register_callbacks(self,callbacks):
        #register event callbacks
        for event in callbacks[0]:
            if event in AbletonPlus._event_callbacks:
                if callbacks[0][event] not in AbletonPlus._event_callbacks[event]:
                    AbletonPlus._event_callbacks[event].append(callbacks[0][event])
            else:
                AbletonPlus._event_callbacks[event] = list()
                AbletonPlus._event_callbacks[event].append(callbacks[0][event])

        #register getter callbacks
        for getter in callbacks[1]:
            if getter in AbletonPlus._getter_callbacks:
                if callbacks[1][getter] not in AbletonPlus._getter_callbacks[getter]:
                    AbletonPlus._getter_callbacks[getter].append(callbacks[1][getter])
            else:
                AbletonPlus._getter_callbacks[getter] = list()
                AbletonPlus._getter_callbacks[getter].append(callbacks[1][getter])

        #register setter callbacks
        for setter in callbacks[2]:
            if setter in AbletonPlus._setter_callbacks:
                if callbacks[2][setter] not in AbletonPlus._setter_callbacks[setter]:
                    AbletonPlus._setter_callbacks[setter].append(callbacks[2][setter])
            else:
                AbletonPlus._setter_callbacks[setter] = list()
                AbletonPlus._setter_callbacks[setter].append(callbacks[2][setter])
    


    #EVENT FUNCTIONS
    def fire_event(self, event, **kwargs):
        """fires an event"""
        
        ignore_self = False #don't fire the callback if the function itself is in the callback list (default: 
        if "ignore_self" in kwargs: 
            ignore_self = kwargs["ignore_self"]
        
        if event in AbletonPlus._event_callbacks.keys():
            for cb in AbletonPlus._event_callbacks[event]:
                if hasattr(self._instance, cb.__name__) and ignore_self:
                    if cb != getattr(self._instance, cb.__name__):
                        cb( event, **kwargs)               
                else:
                    cb(event, **kwargs)                   
            return True
        else:
            return False

    ###GETTER FUNCTIONS
    def getter(self, getter, **kwargs):
        if getter in AbletonPlus._getter_callbacks.keys():
            return AbletonPlus._getter_callbacks[getter][0](self._instance,getter,**kwargs)
        else:
            assert("Assert.  Getter" + getter + " failed.  Script Halted.")  

    ###SETTER FUNCTIONS
    def setter(self, setter, **kwargs):
        ignore_self = True
        if "ignore_self" in kwargs: 
            ignore_self = kwargs["ignore_self"]
        if setter in AbletonPlus._setter_callbacks.keys():
            for cb in AbletonPlus._setter_callbacks[setter]:
                if hasattr(self._instance, cb.__name__) and ignore_self:
                    if cb != getattr(self._instance, cb.__name__):
                        cb(self._instance, setter, **kwargs)               
                else:
                    cb(self._instance, setter, **kwargs)
            return False
        else:
            return False
            
    #MISC FUNCTIONS
    def has_master(self):
        return False if AbletonPlus._master == None else True

    def is_master(self):
        return self._master
        
    def is_not_master(self):
        return not self._master


##utility functions for ableton plus
def ap_add_default_options(instance, options, add = None, remove = None, enable = None, disable = None):
    #add the onadd event
    if add == None:
        if hasattr(instance, "_ape_add"):
            options.update({'ap_add':instance._ape_add})
        else:
            assert("ableton plus add event is a requirement.  No function provided, and default not found.  Halting script.")
    else:
        options.update({'ap_add':add})

    #add the onremove event
    if remove == None:
        if hasattr(instance, "_ape_rem"):
            options.update({'ap_remove':instance._ape_rem})
        else:
            assert("ableton plus remove event is a requirement.  No function provided, and default not found.  Halting script.")
    else:
        options.update({'ap_remove':remove})

        #add the onenable event
    if enable == None:
        if hasattr(instance, "_ape_ena"):
            options.update({'ap_enable':instance._ape_ena})
        else:
            assert("ableton plus enable event is a requirement.  No function provided, and default not found.  Halting script.")
    else:
        options.update({'ap_enable':enable})

    #add the disable event
    if disable == None:
        if hasattr(instance, "_ape_dis"):
            options.update({'ap_disable':instance._ape_dis})
        else:
            assert("ableton plus add event is a requirement.  No function provided, and default not found.  Halting script.")
    else:
        options.update({'ap_disable':disable})
