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

    def __init__(self, c_instance):
        """Initalization function for the BCFR2000 object"""
        ControlSurface.__init__(self, c_instance)
        
        self._bcf = BCF2000()
        self._bcr = BCR2000()
        self._ap = AbletonPlus(self,options['abletonplus'])

        #initalize the live objects needed
        self._mixer = MixerComponent(8,3)
        self._fx_strip = None #placeholder for the efx stuff
        self._enable_abletonplus()
        self._remap_track_mixer_controls()

    def _enable_abletonplus(self):
        self._ap
    def _remap_track_mixer_controls(self):
        """this function is called to remap the mixer controls to the new offsets"""
        current_coords = self._get_coords()
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

    def selcted_track_changed(self,event, **kwargs):
        """recieves and event from the master controller that a new track has been selected"""
        pass

    def coords_changed(self,event,**kwargs):
        """recieves an event from the master controller changing the coordinates"""
        pass

    def _get_coords(self, **kwargs):
        """get the coordinates from the master grid controller"""
        return self._ap.getter("master-grid-coords")

    def disconnect(self):
        """disconnect the instance"""
        self._ap.disable_abletonplus()
        self._disconnect_instance()

