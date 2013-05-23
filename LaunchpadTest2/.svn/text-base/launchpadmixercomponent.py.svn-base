import Live

from _Framework.MixerComponent import MixerComponent

from launchpadchannelstripcomponent import LaunchpadChannelStripComponent

class LaunchpadMixerComponent(MixerComponent):
    '''Add some additional functionality to the mixer component'''
    
    def __init__(self, num_tracks, num_returns=0, with_eqs=False, with_filters=False):
        MixerComponent.__init__(self, num_tracks, num_returns,with_eqs,with_filters)
        
        self._master_stopall_button = None
        self._master_stopall_pressed = None
        
        self._master_mute_button = None
        self._master_mute_pressed = None
        
        self._master_solo_button = None
        self._master_solo_pressed = None
        
        self._master_arm_button = None
        self._master_armg_pressed = None
    
    def get_channel_strips(self):
        return self._channel_strips

    def get_return_strips(self):
        return self._return_strips

    def track_eq(self, index):
        return self._track_eqs[index]

    def track_filter(self, index):
        return self._track_filters
    
    def _create_strip(self):
        return LaunchpadChannelStripComponent()
        
    def remove_button(self, button, listener):
        if button != None and button.value_has_listener(listener):
            button.remove_value_listener(listener)
            button.set_on_off_values()
            return True
        else:
            return False
        
    def set_master_stopall_button(self, button):
        
        if (button != self._master_stopall_button): 
            if (self._master_stopall_button != None): 
                self.remove_master_stopall_button(self._master_stopall_button)
            self._master_stopall_button = button 
            if (self._master_stopall_button != None): 
                self._master_stopall_button.add_value_listener(self._master_stopall_value)
                self._master_stopall_button.turn_on()
            
            self.update()
            
    def _master_stopall_value(self,value):
        self._song.stop_all_clips()

    def remove_master_stopall_button(self, button):
        if(button != None):
            self.remove_button(button, self._master_stopall_value)
            if(button == self._master_stopall_button):
                self._master_stopall_pressed = False #added
                self._master_stopall_button.set_on_off_values()
                self._master_stopall_button = None
                
        self.update()    
    
    def set_master_mute_button(self, button):
        if (button != self._master_mute_button): 
            if (self._master_mute_button != None): 
                self.remove_button(button, self._master_mute_value)
            self._master_mute_button = button 
            if (self._master_mute_button != None): 
                self._master_mute_button.add_value_listener(self._master_mute_value)
                self._master_mute_button.turn_on()
            self.update()
        
    def _master_mute_value(self, value):
        tracks = self._song.tracks
        for track in tracks:
            track.mute = 0
    
    def remove_master_mute_button(self,button):
        if(button != None):
            self.remove_button(button, self._master_mute_value)
            if(button == self._master_mute_button):
                self._master_mute_pressed = False
                self._master_mute_button.set_on_off_values()
                self._master_mute_button = None
        self.update()
    
   
    def set_master_solo_button(self, button):
        if (button != self._master_solo_button): 
            if (self._master_solo_button != None): 
                self.remove_master_solo_button(button)
            self._master_solo_button = button 
            if (self._master_solo_button != None): 
                self._master_solo_button.add_value_listener(self._master_solo_value)
                self._master_solo_button.turn_on()
            self.update()
            
    def _master_solo_value(self, value):
        tracks = self._song.tracks
        for track in tracks:
            track.solo = 0
    
    def remove_master_solo_button(self, button):
        if (button != None): 
            self.remove_button(button,self._master_solo_value)
            if(button == self._master_solo_button):
                self._master_solo_pressed = False #added
                self._master_solo_button.set_on_off_values()
                self._master_solo_button = None
        self.update()
                     
    def set_master_arm_button(self, button):
        if (button != self._master_arm_button): 
            if (self._master_arm_button != None): 
                self._master_arm_button.remove_value_listener(self._master_arm_value)
                self._master_arm_button.reset()
                self._master_arm_pressed = False #added 
            self._master_arm_button = button 
            if (self._master_arm_button != None): 
                self._master_arm_button.add_value_listener(self._master_arm_value)
                self._master_arm_button.turn_on()
            self.update()
            
    def _master_arm_value(self, value):
        tracks = self._song.tracks
        for track in tracks:
            track.arm = 0
    
    def remove_master_arm_button(self, button):
        if (button != None): 
            self.remove_button(button,self._master_arm_value)
            if(button == self._master_arm_button):
                self._master_arm_pressed = False #added
                self._master_arm_button.set_on_off_values()
                self._master_arm_button = None
        self.update()