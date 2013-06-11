import Live

from _Framework.ButtonElement import *
from _Framework.ButtonMatrixElement import ButtonMatrixElement

from launchpadsessioncomponent import LaunchpadSessionComponent
from launchpadbuttoncomponent import LaunchpadButtonComponent
from launchpadmode import LaunchpadMode, Modes

#used for bitfields of the commands to be sent to the launchpadUSER_1_BUTTON = 0x6D

class LaunchpadUser1Mode(LaunchpadMode):
    
    def __init__(self, layout):
        LaunchpadMode.__init__(self)
        self._layout = layout
        
    def enable(self, buttons,oldmode):
        self._enable = True
        self._layout.set_grid_mapping_mode(1)
        for i in range(len(buttons)):
            buttons[i].turn_on()
        return None
    
    def disable(self, buttons,oldmode):
        self._enable = False
        for i in range(len(buttons)):
            buttons[i].turn_off()
        return None

class LaunchpadUser1ModeMod(LaunchpadMode):
    
    def __init__(self, layout):
        LaunchpadMode.__init__(self, True)
        self._old_mode = None
        self._layout = layout
        
    def enable(self, buttons, oldmode):
        self._enable = True
        self._layout.set_grid_mapping_mode(1)
        for i in range(len(buttons)):
            buttons[i].turn_on()
        self._old_mode = oldmode
        
    
    def disable(self, buttons,newmode):
        self._enable = False
        for i in range(len(buttons)):
            buttons[i].turn_off()
        return None

    def get_old_mode(self):
        if self._old_mode is not None:
            return self._old_mode
