import Live
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonElement import *


class SpecialSessionComponent(SessionComponent):
    __doc__ = "Class Extension of the Sesion Component to utilize the Launchpad"
    
    def __init__(self, x, y):
        SessionComponent.__init__(self, x, y)
        return None
    
    #def nav_button(self,button,state):
    #    if state == 1:
    #        self.midi_send((176,button,60))
    #    elif state == 0:
    #        self.midi_send((176,button,28))
    #    return None

