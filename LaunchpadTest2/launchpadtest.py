import Live

#import Launchpad
from _Framework.ControlSurface import ControlSurface
from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _AbletonPlus.Master import Master
from _AbletonPlus.AbletonPlus import *

from launchpadoptions import *
from launchpadsessionmode import *
from launchpadbuttonmatrix import LaunchpadButtonMatrix
from launchpadmodeselectorcomponent import LaunchpadModeSelectorComponent
from launchpaduser1mode import LaunchpadUser1Mode
from launchpaduser2mode import LaunchpadUser2Mode
from launchpadmixermode import LaunchpadMixerMode

UP_BUTTON = 0x68
DOWN_BUTTON = 0x69
LEFT_BUTTON = 0x6A
RIGHT_BUTTON = 0x6B
SESSION_BUTTON = 0x6C
USER_1_BUTTON = 0x6D
USER_2_BUTTON = 0x6E
MIXER_BUTTON = 0x6F

class LPT(ControlSurface, AbletonPlus):
    __doc__ = "Launchpad Source Built from the ground up"
    
    def __init__(self,c_instance):
        ControlSurface.__init__(self, c_instance)
        AbletonPlus.__init__(self, options)
        
        #setup the navigation controls
        self.setup_nav()
        self._nav.add_offset_listener(self.offset_modify)

        #setup the switchable button matrix
        self._buttonmatrix = LaunchpadButtonMatrix(options['width'], options['height'], options['hold'], options['defaultgridmode'])

        #setup the mode selector, and put it into mode 0 (init mode)
        self._mode = LaunchpadModeSelectorComponent()        
        
        #setup and add the sessionmode to the mode selector
        self.init_session_mode()
                
        #setup and add the user1 mode to the mode selector
        self.init_user1_mode()
        
        #setup and add the user2 mode to the mode selector
        self.init_user2_mode()
       
        #setup and add the user2 mode to the mode selector
        self.init_mixer_mode()
        
        #user2_mode_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,0x6E)
        #user2_mode_button.set_on_off_values(60,28)
        
        self._mode.set_mode(options['defaultmode'])
        
        #enable abletonplus last, so that any information it needs to pass along has already been initialized!
        self._enable_abletonplus()
               
        return None
        
    def disconnect(self):
        self._send_midi((176,0,0))
        #self._configmode = None
        #self._mixermode = None
        #self._user2mode = None
        self._user1mode = None
        #self._mode.destroy_modes()
        self._mode = None
        self._sessionmode = None
        self._buttonmatrix = None
        self._nav = None
        #self.shutdown_sequence()
        ControlSurface.disconnect(self)
            
    def _enable_abletonplus(self):
        if(self not in AbletonPlus._enabled_devices):
            AbletonPlus._enabled_devices.append(self)
            AbletonPlus._connect_active_instances(self)
    
    def offset_modify(self):
        AbletonPlus._master_track_offset = self._nav.track_offset()
        AbletonPlus._master_scene_offset = self._nav.scene_offset()
        self.notify_slaves()
    
    def notify_slaves(self):
        for device in self._enabled_devices:
            if(device.is_master() is not True and device is not self):
                device.offset_update()
        return None
    
    def setup_nav(self):
        self._nav = LaunchpadSessionComponent(options['width'],options['height'],options['constrain'])
        ControlSurface._send_midi(self,(176,0,BIT_0 + BIT_3 + BIT_5))
        ControlSurface._send_midi(self,(176,0,BIT_0 + BIT_3 + BIT_5))
        
        right_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,RIGHT_BUTTON)
        right_button.set_on_off_values(60,28)
        
        left_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,LEFT_BUTTON)
        left_button.set_on_off_values(60,28)
        
        down_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,DOWN_BUTTON)
        down_button.set_on_off_values(60,28)
        
        up_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,UP_BUTTON)
        up_button.set_on_off_values(60,28)
        
        self._nav.set_track_bank_buttons(right_button, left_button)
        self._nav.set_scene_bank_buttons(down_button, up_button)
        
        return None
    
    def init_session_mode(self):
        session_mode_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,SESSION_BUTTON)
        session_mode_button.set_on_off_values(63,4)

        self._sessionmode = LaunchpadSessionMode(self._nav, self._buttonmatrix)
        self._sessionmode.set_activator([SESSION_BUTTON])

        
        self._mode.bind_mode(self._sessionmode, session_mode_button, SESSION_MODE, 0)
        return None
    
    def init_user1_mode(self):
        user1_mode_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,USER_1_BUTTON)
        user1_mode_button.set_on_off_values(63,4)
        
        self._user1mode = LaunchpadUser1Mode(self._buttonmatrix)
        self._user1mode.set_activator([USER_1_BUTTON])
        
        self._mode.bind_mode(self._user1mode, user1_mode_button, USER_MODE_1, 0)
        return None
    
    def init_user2_mode(self):
        user2_mode_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,USER_2_BUTTON)
        user2_mode_button.set_on_off_values(63,4)
        
        self._user2mode = LaunchpadUser2Mode(self._buttonmatrix)
        self._user2mode.set_activator([USER_2_BUTTON])
        
        self._mode.bind_mode(self._user2mode, user2_mode_button, USER_MODE_2, 0)
        return None
    
    def init_mixer_mode(self):
        mixer_mode_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,MIXER_BUTTON)
        mixer_mode_button.set_on_off_values(63,4)
        
        self._mixermode = LaunchpadMixerMode(self._nav, self._buttonmatrix, mixer_mode_button)
        self._mixermode.set_activator([MIXER_BUTTON])
        
        self._mode.bind_mode(self._mixermode, mixer_mode_button, MIXER_MODE, 0)
        return None
    
    def shutdown_sequence(self):
        #todo: cool shutdown animation :P
        return None
    
    def startup_sequence(self):
        #todo: cool startup animation :P
        return None