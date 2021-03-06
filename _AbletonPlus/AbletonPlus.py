import Live
from _AbletonPlus.Master import Master
from _AbletonPlus.Options import Options

class AbletonPlus():

    _master = None
    _enabled_devices = []
    _master_track_offset = 0
    _master_scene_offset = 0
    
    def _connect_active_instances(caller):
        if(isinstance(caller._master, Master) and isinstance(AbletonPlus._master, NoneType)):
            for instance in AbletonPlus._enabled_devices:
                instance.notify_connect(caller)
            return None
        else:
            assert("duplicate master designations, please check your configs")
        
        
    _connect_active_instances = staticmethod(_connect_active_instances)
    
    def _disconnect_instance(self):
        i = AbletonPlus._enabled_devices.index(self)
        AbletonPlus._enabled_devices.pop(i)
        return None
    
    def __init__(self, options):
        #first lets read the options
        self._options = options
                
        if(self._options.has_key('Master')):
            if(self._options['Master']):
                self._master = True
                
            else:
                self._master = False
        else:
            self._master = False
            
        
        return None
    
    def _enable_abletonplus(self):
        assert("Virtual Method... did you forget to overload?")
        
    def configure_ableton_plus(self):
        assert("Virtual Method... overload this bitch!")
    
    def notify_connect(self, caller):
        assert("Virtual Method... we require more Overloads!")
        
    def notify_disconnect(self, caller):
        assert("Virtual Method... O V E R L O A D")
        
    def get_track_offset():
        return AbletonPlus._master_track_offset
    
    get_track_offset = staticmethod(get_track_offset)
        
    def get_scene_offset():
        return AbletonPlus._master_scene_offset
    
    get_scene_offset = staticmethod(get_scene_offset)
        
    def is_master(self):
        if(isinstance(self._master,Master)):
            return True
        else:
            return False
        
    def is_not_master(self):
        if(isinstance(self._master, Master)):
            return False
        else:
            return True
        
