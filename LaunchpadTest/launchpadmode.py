import Live

#mode identifiers
MODE_XY = 1
MODE_DRUM = 2 

#MODE BITS
#INIT_MODE = 0
#MODE_SESSION = 4
#MODE_USER1 = 8
#MODE_USER2 = 16
#MODE_MIXER = 32
#MODE_CONFIG = 64
#MODE_TRACK_SELECTOR = 128
#MODE_CLIP_SELECTOR  = 256

NO_MODES = -1
INIT_MODE = 0
SESSION_MODE = 1
USER_MODE_1 = 2
USER_MODE_2 = 4
MIXER_MODE  = 8
OPTIONS_MODE = 16

#MODE INDICIES
SESSION_MODE = 1


class Modes():
    """storage container for all the modes"""
    NO_MODES = -1
    INIT_MODE = 0
    SESSION_MODE = 1
    USER_MODE_1 = 2
    USER_MODE_2 = 4
    MIXER_MODE  = 8
    TRACK_MODE = 16
    CLIP_MODE = 32
    OPTIONS_MODE = 64
    
        

class LaunchpadMode():
    
    def __init__(self, momentary = False):
        self._enabled = False
        self._is_momentary = momentary
        self._oldmode = None

        self._activator_list = []
        return None
    
    def enable(self,oldmode):
        assert("Overload this bitch, yo: enabled")
        pass
    
    def disable(self,newmode):
        assert("Overload this bitch, yo: disabled")
        #self._enabled = False
        pass
    
    def on_enabled(self, callback):
        pass
    
    def remove_enabled_callback(self, callback):
        pass
    
    def get_old_mode(self):
        if self._oldmode is not None:
            return self._oldmode
        else:
            assert("oldmode should be set")

    def isenabled(self):
        return self._enabled

    def is_momentary(self):
        return self._is_momentary
    
    def activator(self):
        return self._activator_list
    
    def set_activator(self, activator_ids):
        if(type(activator_ids) == list):
            self._activator_list = activator_ids
    
    
