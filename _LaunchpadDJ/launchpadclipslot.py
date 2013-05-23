import Live 
from _Framework.ClipSlotComponent import ClipSlotComponent

class LaunchpadClipSlot(ClipSlotComponent):
    
    """ Custom ClipSlot component to make it so that the off values are not
        TRUE off values, but the lights are off, noone is home
        and the copy bit is set :P
    """
    highlighted_button = None
    
    def __init__(self):
        ClipSlotComponent.__init__(self)
        self._noclip_value = 4
        self.set_allow_update(True)
        self._highlight_clip_button = None
        
    def set_noclip_value(self, value):
        if(value != None):
            self._noclip_value = value
  
    def update(self):
        if self._allow_updates:
            if (self._launch_button != None):
                value_to_send = -1
                if (self._clip_slot != None):
                    if self.has_clip():
                        value_to_send = self._stopped_value
                        if self._clip_slot.clip.is_triggered:
                            if self._clip_slot.clip.will_record_on_start:
                                value_to_send = self._triggered_to_record_value
                            else:
                                value_to_send = self._triggered_to_play_value
                        if self._clip_slot.clip.is_playing:
                            if self._clip_slot.clip.is_recording:
                                value_to_send = self._recording_value
                            else:
                                value_to_send = self._started_value
                        if self._clip_slot.clip.is_triggered:
                            if self._clip_slot.clip.will_record_on_start:
                                value_to_send = self._triggered_to_record_value
                            else:
                                value_to_send = self._triggered_to_play_value
                        if self._clip_slot.clip.is_playing:
                            if self._clip_slot.clip.is_recording:
                               value_to_send = self._recording_value
                            else:
                                value_to_send = self._started_value
                        if self._clip_slot.controls_other_clips:
                                value_to_send = self._stopped_value
                    else:    
                        value_to_send = self._noclip_value
                    
                    if (value_to_send in range(128)):
                        self._launch_button.send_value(value_to_send,False)
                    self.update_highlight_button()
        else:
            self._update_requests += 1
        return None
    
    def set_highlight_button(self, button):
        if button != self._highlight_clip_button:
            if self._highlight_clip_button != None:
                self._highlight_clip_button.remove_value_listener(self._highlight_clip)
            self._highlight_clip_button = button
            if self._highlight_clip_button != None:
                self._highlight_clip_button.add_value_listener(self._highlight_clip)
            self.update()
        return None
    
    def update_highlight_button(self):
        if (self.song().view.highlighted_clip_slot == self._clip_slot) and (self._highlight_clip_button != None):
            self._highlight_clip(1)
        else:
            if (self._highlight_clip_button != None) and (self.song().view.highlighted_clip_slot != self._clip_slot):
                self._highlight_clip_button.turn_off()
                
    
    def _highlight_clip(self, value):
        if value == 1:
            if self.has_clip():
                if LaunchpadClipSlot.highlighted_button != None:
                    LaunchpadClipSlot.highlighted_button.turn_off()
                self.song().view.highlighted_clip_slot = self._clip_slot
                self._highlight_clip_button.turn_on()
                LaunchpadClipSlot.highlighted_button = self._highlight_clip_button
        return None
    
    def _launch_value(self, value):
        if (self._launch_button != None) and (value in range(128)):
            if self._clip_slot != None and self.is_enabled():
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
        return None