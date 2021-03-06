import Live


from _Framework.ControlSurface import ControlSurface
#from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _AbletonPlus.Master import Master
from _AbletonPlus.AbletonPlus import *

#from launchpadsessionmode import *

#from launchpadmodeselectorcomponent import LaunchpadModeSelectorComponent
#from launchpadbuttoncomponent import LaunchpadButtonComponent
from launchpadsessionmanager import LaunchpadSessionManager
#from launchpadbuttonmatrix import LaunchpadButtonMatrix

BIT_0 = int(1)
BIT_1 = int(2)
BIT_2 = int(4)
BIT_3 = int(8)
BIT_4 = int(16)
BIT_5 = int(32)

class LaunchpadDJ(ControlSurface, AbletonPlus):
    __doc__ = "Launchpad DJ Script for my custom setup"
    
    def __init__(self,c_instance, channel):
        ControlSurface.__init__(self, c_instance)
        #AbletonPlus.__init__(self,{})
        
        #setup the navigation controls
        self._session = LaunchpadSessionManager(channel)
        
        #self._enable_abletonplus()
    
        return None
        
    def disconnect(self):
        
        self._session = None
        #self._disconnect_instance()
        self._send_midi((176,0,0))
        ControlSurface.disconnect(self)
            
    def _enable_abletonplus(self):
        if(self not in AbletonPlus._enabled_devices):
            AbletonPlus.add_device(self)

    def notify_connect(self, caller):
        if isinstance(caller, LPT):
            self._session._ch_b_nav = caller._session
    
    def notify_disconnect(self, caller):
        pass

    def connect_script_instances(self, instances):
        ControlSurface._send_midi(self,(176,0,BIT_0 + BIT_3 + BIT_5))
        ControlSurface._send_midi(self,(176,0,BIT_0 + BIT_3 + BIT_5))