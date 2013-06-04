import Live

#mode identifiers
MODE_XY = 1
MODE_DRUM = 2 

INIT_MODE = 0
MODE_SESSION = 4
MODE_USER1 = 8
MODE_USER2 = 16
MODE_MIXER = 32
MODE_CONFIG = 64

MODE_TRACK_SELECTOR = 128
MODE_CLIP_SELECTOR  = 256

class LaunchpadMode():
    
    def __init__(self):
        self._enabled = False
        self._activator_list = []
        return None
    
    def enable(self):
        assert("Overload this bitch, yo: enabled")
        pass
    
    def disable(self):
        assert("Overload this bitch, yo: disabled")
        #self._enabled = False
        pass
    
    def on_enabled(self, callback):
        pass
    
    def remove_enabled_callback(self, callback):
        pass
    
    def isenabled(self):
        return self._enabled
    
    def activator(self):
        return self._activator_list
    
    def set_activator(self, activator_ids):
        if(type(activator_ids) == list):
            self._activator_list = activator_ids
    
    
