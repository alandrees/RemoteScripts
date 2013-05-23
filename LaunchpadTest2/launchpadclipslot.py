import Live 
from _Framework.ClipSlotComponent import ClipSlotComponent

class LaunchpadClipSlot(ClipSlotComponent):
    
    """ Custom ClipSlot component to make it so that the off values are not
        TRUE off values, but the lights are off, noone is home
        and the copy bit is set :P
    """
    
    def __init__(self):
        ClipSlotComponent.__init__(self)
        self._noclip_value = 4
        self.set_allow_update(True)
        
    def set_noclip_value(self, value):
        if(value != None):
            self._noclip_value = value
  
    def _launch_value(self, value): #possibly some odd things in here...
        assert (self._launch_button != None)
        assert (value in range(128))
        if self.is_enabled() and self._clip_slot != None:
            object_to_launch = self._clip_slot
            launch_pressed = (value != 0) or not (self._launch_button.is_momentary())
            if self.has_clip():
                object_to_launch = self._clip_slot.clip
            else:
                self._has_fired_slot = True
            if self._launch_button.is_momentary():
                object_to_launch.set_fire_button_state(value != 0)
            elif value != 0:
                object_to_launch.fire()
            if launch_pressed and self.has_clip() and self.song().select_on_launch and 1 == 2:
                self.song().view.highlighted_clip_slot = self._clip_slot
        return None
    
    def update(self): #needs to be re-checked...
        self._has_fired_slot = False
        if self._allow_updates:
            if (self.is_enabled() and (self._launch_button != None)):
                value_to_send = -1
                if (self._clip_slot != None):
                    if self.has_clip():
                        value_to_send = self._stopped_value
                        if self._clip_slot.clip.is_triggered:
                            if self._clip_slot.clip.will_record_on_start:
                                value_to_send = self._triggered_to_record_value
                            else:
                                value_to_send = self._triggered_to_play_value
                        elif self._clip_slot.clip.is_playing:
                            if self._clip_slot.clip.is_recording:
                                value_to_send = self._recording_value
                            else:
                                value_to_send = self._started_value
                    elif self._clip_slot.is_triggered:
                        if self._clip_slot.will_record_on_start:
                            value_to_send = self._triggered_to_record_value
                        else:
                            value_to_send = self._triggered_to_play_value
                    elif self._clip_slot.is_playing:
                        if self._clip_slot.is_recording:
                            value_to_send = self._recording_value
                        else:
                            value_to_send = self._started_value
                    elif self._clip_slot.controls_other_clips:
                        value_to_send = self._stopped_value
                if (value_to_send in range(128)):
                    self._launch_button.send_value(value_to_send,True)
                else:
                    self._launch_button.turn_off()
        else:
            self._update_requests += 1
        return None