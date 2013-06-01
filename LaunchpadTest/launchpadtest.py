import Live

##FRAMEWORK CLASSES
from _Framework.ControlSurface import ControlSurface
from _Framework.ModeSelectorComponent import ModeSelectorComponent

##ABLETONPLUS2 CLASSES
from _AbletonPlus2.AbletonPlus import *
from _AbletonPlus2.abletonlog import *

##CUSTOM LAUNCHPAD COMPONENTS
from launchpadmode import *
from launchpadoptions import options
from launchpadsessionmode import *
from launchpadbuttonmatrix import LaunchpadButtonMatrix
from launchpadmodeselectorcomponent import LaunchpadModeSelectorComponent

#from launchpaduser1mode import LaunchpadUser1Mode
#from launchpaduser2mode import LaunchpadUser2Mode
#from launchpadmixermode import LaunchpadMixerMode

UP_BUTTON = 0x68
DOWN_BUTTON = 0x69
LEFT_BUTTON = 0x6A
RIGHT_BUTTON = 0x6B
SESSION_BUTTON = 0x6C
USER_1_BUTTON = 0x6D
USER_2_BUTTON = 0x6E
MIXER_BUTTON = 0x6F


####ableton plus events:
##Events:
##'master_grid_coords': kwargs['coords'] = (track,scene) [top left corner,tuple]
##'master_track_update': kwargs['offset'] = track_offset_integer [selected track,integer, only fired when the track changes
##
##Getters:
##'master_grid_offset': returns tuple (track, scene) self.master_grid_offset()
##'master_selected_track': returns integer track self.master_selected_track()
##
##Setters:
##None


#write_log(str(dir()))
class LPT(ControlSurface):
    """Launchpad Source Built from the ground up"""
    
    def __init__(self,c_instance):
        ControlSurface.__init__(self, c_instance)
        
        #setup the navigation controls
        self.setup_nav()
        self._nav.add_offset_listener(self._ape_master_grid_coords_fire)
        self._ap = AbletonPlus(self, options['abletonplus'])

        #setup the switchable button matrix
        self._buttonmatrix = LaunchpadButtonMatrix(options['width'], options['height'], options['hold'], options['defaultgridmode'])

        #setup the mode selector, and put it into mode 0 (init mode)
        self._mode = LaunchpadModeSelectorComponent()
        
        #setup and add the sessionmode to the mode selector
        self.init_session_mode()
        
        #setup the abletonplus callback array
        self._setup_ap_options()
        
        ###GENERIC OFFICAL IMPLEMENTATION OF THE LAUNCHPAD MODES###
        #setup and add the user1 mode to the mode selector
        #self.init_user1_mode()
        
        #setup and add the user2 mode to the mode selector
        #self.init_user2_mode()
       
        #setup and add the user2 mode to the mode selector
        #self.init_mixer_mode()
        
        #user2_mode_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,0x6E)
        #user2_mode_button.set_on_off_values(60,28)
        
        #write_log(str(dir(self._nav)))
        self._mode.set_mode(options['defaultmode'])
                
        self._ap.enable_abletonplus()
               
                   
    def _enable_abletonplus(self):
        self._ap.enable_abletonplus()

    def _setup_ap_options(self):
        ap_options = options['abletonplus']

        #EVENTS
        #write_log(str(options['abletonplus'].keys()))
        #listeners
        ##always need to add a handler for controller add and remove
        ap_add_default_options(self, ap_options['callbacks'][0])

        #ap_options['callbacks'][0].update({'ap_add':self._ape_add,'ap_remove':self._ape_rem, 'ap_enable':self._ape_enable,'ap_disable':self._ape_dis})

        #GETTERS

        #setup the getters
        ap_options['callbacks'][1].update({'master_grid_offset':self._apg_master_grid_offset,'master_selected_track':self._apg_master_selected_track})

        #SETTERS

    ####event listeners
    def _ape_add(self,event, **kwargs):
        """this event handler is fired when a controller gets added"""
        pass

    def _ape_rem(self, event, **kwargs): 
        """this event handler is fired when a controller gets removed"""
        pass

    def _ape_enable(self, event, **kwargs):
        """this event handler is fired when a controller gets disabled"""
        pass

    def _ape_dis(self, event, **kwargs):
        """this event handler is fired when a controller gets disabled"""
        pass

    ####event fire-ers
    def _ape_master_grid_coords_fire(self):
        """this function fires an update of grid coordinates"""
        #write_log(str(self._nav.get_offsets()))
        self._ap.fire_event('update_master_grid_coords',coords=self._nav.get_offsets())
        pass

    def _ape_master_track_update_fire(self):
        """this function fires an update of the selected track"""
        pass
    
    ####getter handlers
    def _apg_master_grid_offset(self, sender, getter, **kwargs):
        return self._nav.get_offsets()

    def _apg_master_selected_track(self, sender, getter, **kwargs):
        pass

    ####setter handlers

    def disconnect(self):
        self._send_midi((176,0,0))
        #self._configmode = None
        #self._mixermode = None
        #self._user2mode = None
        #self._user1mode = None
        #self._mode.destroy_modes()
        self._mode = None
        self._sessionmode = None
        self._buttonmatrix = None
        self._nav = None
        #self.shutdown_sequence()
        ControlSurface.disconnect(self)

    def setup_nav(self):
        
        self._nav = LaunchpadSessionComponent(8,8,True)
        
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
        
    

    def init_session_mode(self):
        """initalize the session mode component"""
        session_mode_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,SESSION_BUTTON)
        session_mode_button.set_on_off_values(63,4)

        self._sessionmode = LaunchpadSessionMode(self._nav, self._buttonmatrix)
        self._sessionmode.set_activator([SESSION_BUTTON])
       
        self._mode.bind_mode(self._sessionmode, session_mode_button, SESSION_MODE, 0)
    
    def init_user1_mode(self):
        user1_mode_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,USER_1_BUTTON)
        user1_mode_button.set_on_off_values(63,4)
        
        self._user1mode = LaunchpadUser1Mode(self._buttonmatrix)
        self._user1mode.set_activator([USER_1_BUTTON])
        
        self._mode.bind_mode(self._user1mode, user1_mode_button, USER_MODE_1, 0)
    
    def init_user2_mode(self):
        user2_mode_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,USER_2_BUTTON)
        user2_mode_button.set_on_off_values(63,4)
        
        self._user2mode = LaunchpadUser2Mode(self._buttonmatrix)
        self._user2mode.set_activator([USER_2_BUTTON])
        
        self._mode.bind_mode(self._user2mode, user2_mode_button, USER_MODE_2, 0)
    
    def init_mixer_mode(self):
        mixer_mode_button = LaunchpadButtonComponent(options['hold'], MIDI_CC_TYPE,0,MIXER_BUTTON)
        mixer_mode_button.set_on_off_values(63,4)
        
        self._mixermode = LaunchpadMixerMode(self._nav, self._buttonmatrix, mixer_mode_button)
        self._mixermode.set_activator([MIXER_BUTTON])
        
        self._mode.bind_mode(self._mixermode, mixer_mode_button, MIXER_MODE, 0)
    
    def shutdown_sequence(self):
        #todo: cool shutdown animation :P
        pass
    
    def startup_sequence(self):
        #todo: cool startup animation :P
        pass
