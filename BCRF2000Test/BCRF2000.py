import Live

from _Framework.ControlSurface import ControlSurface
from _Framework.ChannelStripComponent import ChannelStripComponent
from _AbletonPlus.AbletonPlus import *
from _AbletonPlus.abletonlog import *
from _Framework.MixerComponent import *
from _Framework.SliderElement import *
from BCRF2000Options import options
from _AbletonPlus.Master import Master
from BCR2000 import BCR2000
from BCF2000 import BCF2000

class BCRF2000(ControlSurface,AbletonPlus):
    """BCFR Control Surface Class"""

    def __init__(self, c_instance):
        """Initalization function for the BCRF2000 object"""
        ControlSurface.__init__(self, c_instance)
        AbletonPlus.__init__(self,options)
        
        self._bcf = BCF2000()
        self._bcr = BCR2000()

        self._mixer = MixerComponent(8)
        self._remap_track_mixer_controls()
        self._enable_abletonplus()

    def _enable_abletonplus(self):
        """this function enables AbletonPlus"""
        if(self not in AbletonPlus._enabled_devices):
            AbletonPlus._enabled_devices.append(self)
            AbletonPlus._connect_active_instances(self)
            
    def _remap_track_mixer_controls(self):
        """this function is called to remap the mixer controls when AbletonPlus pushes a coordinate update"""
        self._mixer.set_track_offset(AbletonPlus.get_track_offset())
        for index in range(8):
            strip = self._mixer.channel_strip(index)
            strip.set_volume_control(self._bcf.main_faders[index])
            strip.set_pan_control(self._bcf.encoder_groups[0][index])
            strip.set_mute_button(self._bcf.buttons[0][index])
            strip.set_arm_button(self._bcf.buttons[1][index])
            strip.set_send_controls((self._bcf.encoder_groups[1][index],self._bcf.encoder_groups[2][index],self._bcf.encoder_groups[3][index]))

    def offset_update(self):
        """update the offset"""
        self._remap_track_mixer_controls()
        return None

    def selected_change(self):
        """update the offset"""
        self._remap_selected_track_devices()
        return None

    def disconnect(self):
        """disconnect the instance"""
        self._disconnect_instance()
