import Live

from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ChannelStripComponent import ChannelStripComponent
from _Framework.ButtonElement import *

class LaunchpadChannelStripComponent(ChannelStripComponent):
    
    def __init__(self):
        ChannelStripComponent.__init__(self)
        self._stopall_button = None
        
    def get_track(self):
        if(self._track != None):
            return self._track
        else:
            return None
    def sends_count(self):
        return len(self._track.mixer_device.sends)
    
    def set_stopall_button(self, button):
        if (button != self._stopall_button): 
            if (self._stopall_button != None): 
                self._stopall_button.remove_value_listener(self._stopall_value)
                self._track.remove_fired_slot_index_listener(self._on_stopall_changed)
                self._track.remove_playing_slot_index_listener(self._on_stopall_changed)
                self._stopall_button.reset()
                self._stopall_pressed = False #added 
            self._stopall_button = button 
            if (self._stopall_button != None): 
                self._stopall_button.add_value_listener(self._stopall_value)
                self._track.add_fired_slot_index_listener(self._on_stopall_changed)
                self._track.add_playing_slot_index_listener(self._on_stopall_changed)
            self.update()

    def _stopall_value(self,value):
        self._track.stop_all_clips()
        self.update()

    def remove_stopall_button(self):
        if (self._stopall_button != None): 
                self._stopall_button.remove_value_listener(self._stopall_value)
                self._track.remove_fired_slot_index_listener(self._on_stopall_changed)
                self._track.remove_playing_slot_index_listener(self._on_stopall_changed)
                self._stopall_pressed = False #added
                
    def _on_stopall_changed(self):
        if ((self._track != None) and hasattr(self._track, 'fired_slot_index') and hasattr(self._track, 'fired_slot_index')):
            if self._stopall_button != None:
                if self._track.fired_slot_index == -2:
                    self._stopall_button.send_value(59)
                    return None
                if self._track.playing_slot_index >= 0:
                    self._stopall_button.send_value(29,True)
                else:
                    self._stopall_button.send_value(13,True)
    
    def set_track(self, track):
        #assert isinstance(track, type(None), Live.Track.Track)
        assert ((track == None) or isinstance(track, Live.Track.Track))
        if (self._track != None):
            if (self._track != self.song().master_track):
                if self._track.mixer_device.sends_has_listener(self._on_sends_changed):
                    self._track.mixer_device.remove_sends_listener(self._on_sends_changed)
                if self._track.mute_has_listener(self._on_mute_changed):
                    self._track.remove_mute_listener(self._on_mute_changed)
                if self._track.name_has_listener(self._on_track_name_changed):
                    self._track.remove_name_listener(self._on_track_name_changed)
                if self._track.solo_has_listener(self._on_solo_changed):
                    self._track.remove_solo_listener(self._on_solo_changed)
                if self._track.mixer_device.crossfade_assign_has_listener(self._on_cf_assign_changed):
                    self._track.mixer_device.remove_crossfade_assign_listener(self._on_cf_assign_changed)
                if (self._track not in self.song().return_tracks):
                    if (self._track.can_be_armed and self._track.arm_has_listener(self._on_arm_changed)):
                        self._track.remove_arm_listener(self._on_arm_changed)
                    if self._track.current_input_routing_has_listener(self._on_input_routing_changed):
                        self._track.remove_current_input_routing_listener(self._on_input_routing_changed)
        if (self._pan_control != None):
            self._pan_control.release_parameter()
        if (self._volume_control != None):
            self._volume_control.release_parameter()
        if (self._send_controls != None):
            for send_control in self._send_controls:
                if (send_control != None):
                    send_control.release_parameter()
        self._track = track
        if (self._track != None):
            assert isinstance(self._track, Live.Track.Track)
            assert (self._track in ((self.song().tracks + self.song().return_tracks) + (self.song().master_track,)))
            if (self._track != self.song().master_track):
                self._track.add_solo_listener(self._on_solo_changed)
                self._track.mixer_device.add_sends_listener(self._on_sends_changed)
                self._track.add_mute_listener(self._on_mute_changed)
                self._track.add_name_listener(self._on_track_name_changed)
                self._track.mixer_device.add_crossfade_assign_listener(self._on_cf_assign_changed)
                if (self._track not in self.song().return_tracks):
                    if self._track.can_be_armed:
                        self._track.add_arm_listener(self._on_arm_changed)
                    self._track.add_current_input_routing_listener(self._on_input_routing_changed)
            if (self._track_name_data_source != None):
                self._track_name_data_source.set_display_string(self._track.name)
        else:
            if (self._track_name_data_source != None):
                self._track_name_data_source.set_display_string(' - ')
            for button in [self._select_button, self._mute_button, self._solo_button, self._arm_button, self._crossfade_toggle]: #added
                if button != None: #added
                    button.turn_off() #added
        self.update()
    
    def update(self):
        if self._allow_updates:
            if self.is_enabled():
                if (self._track != None):
                    if (self._pan_control != None):
                        self._pan_control.connect_to(self._track.mixer_device.panning)
                    if (self._volume_control != None):
                        self._volume_control.connect_to(self._track.mixer_device.volume)
                    if (self._send_controls != None):
                        index = 0
                        for send_control in self._send_controls:
                            if (send_control != None):
                                if (index < len(self._track.mixer_device.sends)):
                                    send_control.connect_to(self._track.mixer_device.sends[index])
                                else:
                                    send_control.release_parameter()
                            index += 1
                #self._request_rebuild_callback()
                self.on_selected_track_changed()
                self._on_mute_changed()
                self._on_solo_changed()
                self._on_arm_changed()
                self._on_cf_assign_changed()
                self._on_stopall_changed()
                
            else:
                if (self._track != None):
                    if (self._pan_control != None):
                        self._pan_control.release_parameter()
                    if (self._volume_control != None):
                        self._volume_control.release_parameter()
                    if (self._send_controls != None):
                        for send_control in self._send_controls:
                            if (send_control != None):
                                send_control.release_parameter()

                #ControlSurfaceComponent._request_rebuild_callback(self)
        else:
            self._update_requests += 1
            
    def remove_send_controls(self):
        for send_control in self._send_controls:
            send_control.release_parameter()
        self._send_controls = None
                        
    def remove_volume_control(self):
        f = open("C:\log","a")
        
        self._volume_control.release_parameter()
        
        f.write("\n")
        self._volume_control = None
        
        f.close()
            