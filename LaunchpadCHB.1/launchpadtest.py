import Live


from _Framework.ControlSurface import ControlSurface
#from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _AbletonPlus.Master import Master
from _AbletonPlus.AbletonPlus import *

from launchpadsessionmode import *

#from launchpadmodeselectorcomponent import LaunchpadModeSelectorComponent
#from launchpadbuttoncomponent import LaunchpadButtonComponent
from launchpadsessionmanager import LaunchpadSessionManager
#from launchpadbuttonmatrix import LaunchpadButtonMatrix

class LPT(ControlSurface, AbletonPlus):
    __doc__ = "Launchpad Source Built from the ground up"
    
    def __init__(self,c_instance):
        ControlSurface.__init__(self, c_instance)
        #AbletonPlus.__init__(self, options)
        
        #setup the navigation controls
        #self._enable_abletonplus()
        self._session = LaunchpadSessionManager()

        return None
        
    def disconnect(self):
        self._session = None
        self._send_midi((176,0,0))
        ControlSurface.disconnect(self)
            
    def _enable_abletonplus(self):
        if(self not in AbletonPlus._enabled_devices):
            AbletonPlus._enabled_devices.append(self)
            AbletonPlus._connect_active_instances(self)