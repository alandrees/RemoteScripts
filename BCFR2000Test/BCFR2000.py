import Live

from _Framework.ControlSurface import ControlSurface
from _Framework.ChannelStripComponent import ChannelStripComponent
from _AbletonPlus2.AbletonPlus import *
from _AbletonPlus2.abletonlog import *
from _Framework.MixerComponent import *
from _Framework.SliderElement import *

from BCFR2000Options import options
from BCR2000 import BCR2000
from BCF2000 import BCF2000

class BCFR2000(ControlSurface):
    """BCFR Control Surface Class"""

    ####PRIVATE METHODS
    def __init__(self, c_instance):
        """Initalization function for the BCFR2000 object"""
        ControlSurface.__init__(self, c_instance)
        
        self._bcf = BCF2000()
        self._bcr = BCR2000()
        self._master_coords = (0,0)

        self._ap = AbletonPlus(self,options['abletonplus'])
        self._setup_ap_options()

        #initalize the live objects needed
        self._mixer = MixerComponent(8,3)
        self._fx_strip = None #placeholder for the efx stuff
        self._enable_abletonplus()
        self._remap_track_mixer_controls()

    def _remap_track_mixer_controls(self):
        """this function is called to remap the mixer controls to the new offsets"""
        self._mixer.set_track_offset(self._master_coords[0])
        for index in range(8):
            strip = self._mixer.channel_strip(index)
            strip.set_volume_control(self._bcf.main_faders[index])
            strip.set_pan_control(self._bcf.encoder_groups[0][index])
            strip.set_mute_button(self._bcf.buttons[0][index])
            strip.set_arm_button(self._bcf.buttons[1][index])
            strip.set_send_controls((self._bcf.encoder_groups[1][index],self._bcf.encoder_groups[2][index],self._bcf.encoder_groups[3][index]))

    def __remap_sfx_controls(self):
        """remaps  the sfx controls when the controls are changed"""
        pass

    def _get_coords(self):
        """get the coordinates from the master grid controller.  master-grid-coords returns a tuple to be treated like an x-y coordinate"""
        
        return self._ap.getter("master_grid_offset")

    def _ape_add(self, sender, event, **kwargs):
        """this event handler is fired when a controller gets added"""
        pass

    def _ape_rem(self, sender, event, **kwargs):
        pass

    def _ape_ena(self, sender, event, **kwargs):
        pass

    def _ape_dis(self, sender, event, **kwargs):
        pass

    def _ape_update_master_grid_coords(self,event,**kwargs):
        """recieves an event from the master controller changing the coordinates, forces update"""
        write_log(event)
        if event == 'update_master_grid_coords':
            if "coords" in kwargs:
                self._master_coords = kwargs['coords']
                self._remap_track_mixer_controls()

    def _ape_update_master_selected_track(self,event,**kwargs):
        """receives an event from the master controller changing the selected track"""
        if event == 'update_master_selected_track':
            if 'track' in kwargs:
                #do track getting stuff here, from the track in kwargs
                #remap the track controls
                pass
    def _ape_update_bcf2000_mappings(self,event,**kwargs):
        """recieves a message to force re-updating the control mappings"""
        if event == 'update_bcf2000_mappings':
            self._remap_track_mixer_controls(-1,-1)


    def _setup_ap_options(self):
        ap_options = options['abletonplus']
        
        #EVENTS
        #listeners
        ##always need to add a handler for controller add, remove, enable, disable... so we use the helper function to do that
        ap_add_default_options(self, ap_options['callbacks'][0])

        ap_options['callbacks'][0].update({'update_master_grid_coords':self._ape_update_master_grid_coords,
                                           'update_master_selected_track':self._ape_update_master_selected_track,
                                           'update_bcf2000_mappings':self._ape_update_bcf2000_mappings})



        #ap_options['callbacks'][0].update('ap_add':self._ape_add,'ap_remove':self._ape_rem,'ap_enable':self._ape_ena,'ap_disable':self._ape_dis

    def _enable_abletonplus(self):
        self._ap.enable_abletonplus()

    def selcted_track_changed(self,event, **kwargs):
        """recieves and event from the master controller that a new track has been selected"""
        pass

    def update_master_coords(self,coords = None):
        if coords == None:
            master_coords = self._get_coords()
            if (master_coords[0] != self._master_coords[0]) or (master_coords[1] != self._master_coords[1]):
                self._master_coords = master_coords
                update
            


    def disconnect(self):
        """disconnect the instance"""
        self._ap.disable_abletonplus()
        self._disconnect_instance()

