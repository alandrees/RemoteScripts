import Live

from _Framework.ButtonElement import *
from _Framework.ButtonMatrixElement import ButtonMatrixElement

from launchpadsessioncomponent import LaunchpadSessionComponent
from launchpadbuttoncomponent import LaunchpadButtonComponent
from launchpadmode import LaunchpadMode

#used for bitfields of the commands to be sent to the launchpad
USER_2_BUTTON = 0x6E

class LaunchpadUser2Mode(LaunchpadMode):
    
    def __init__(self,layout):
        LaunchpadMode.__init__(self)
        self._layout = layout

    def enable(self, buttons, oldmode):
        self._enable = True
        self._layout.set_grid_mapping_mode(2)
        for i in range(len(buttons)):
            buttons[i].turn_on()
        return None
    
    def disable(self, buttons,newmode):
        self._enable = False
        for i in range(len(buttons)):
            buttons[i].turn_off()
        return None
