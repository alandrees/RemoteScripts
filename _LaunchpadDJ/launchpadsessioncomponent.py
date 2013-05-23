import Live
from _Framework.SessionComponent import SessionComponent
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent 
from _Framework.ButtonElement import *
from launchpadscenecomponent import LaunchpadSceneComponent

class LaunchpadSessionComponent(SessionComponent):
    __doc__ = "Class Extension of the Sesion Component to utilize the Launchpad"
    
    def __init__(self, x, y, constrain):
        SessionComponent.__init__(self, x, y)
        self._contstrain = constrain
        return None
    
    def _update_banking_buttons(self, track_offset, scene_offset):
        if self.is_enabled():
            scenes = self.song().scenes
            tracks = self.tracks_to_use()
            selected_scene = self.song().view.selected_scene
                
            if (self._bank_down_button != None):
                if (scene_offset > 0 and (self.height() - scene_offset) < self.height()):
                    self._bank_down_button.turn_on()
                else:
                    self._bank_down_button.turn_off()
            if (self._bank_up_button != None):
                if (len(scenes) + 1 > (scene_offset + self.height()) ):
                    self._bank_up_button.turn_on()
                else:
                    self._bank_up_button.turn_off()
                
            if (self._bank_left_button != None):
                if (track_offset > 0 and (track_offset - self.width() < self.width())):
                    self._bank_left_button.turn_on()
                else:
                    self._bank_left_button.turn_off()
            if (self._bank_right_button != None):
                if (len(tracks) + 1 > (track_offset + self.width())):
                    self._bank_right_button.turn_on()
                else:
                    self._bank_right_button.turn_off()
        
            if (self._next_scene_button != None):
                if (selected_scene != self.song().scenes[-1]):
                    self._next_scene_button.turn_on()
                else:
                    self._next_scene_button.turn_off()
        
            if (self._prev_scene_button != None):
                if (selected_scene != self.song().scenes[0]):
                    self._prev_scene_button.turn_on()
                else:
                    self._prev_scene_button.turn_off()
                
    def update(self):
        if self._allow_updates:
            if self.is_enabled():
                if self._is_linked():
                    self._update_banking_buttons(SessionComponent._minimal_track_offset, SessionComponent._minimal_scene_offset)
                else:
                    self._update_banking_buttons(self.track_offset(), self.scene_offset())
            else:
                for button in (self._bank_up_button, self._bank_down_button, self._bank_right_button, self._bank_left_button, self._prev_scene_button, self._next_scene_button):
                    if (button != None):
                        button.turn_off()
        else:
            self._update_requests += 1
        return None
    
    def set_offsets(self, track_offset, scene_offset):
        assert (track_offset >= 0)
        assert (scene_offset >= 0)
        track_increment = 0
        scene_increment = 0
        if self._is_linked():
            SessionComponent._perform_offset_change((track_offset - self._track_offset), (scene_offset - self._scene_offset)) 
        else:
            if (len(self.tracks_to_use()) > track_offset + self.width() - 1):
                track_increment = track_offset - self._track_offset  #modified
            if (len(self.song().scenes) > scene_offset + self.height() - 1):
                scene_increment = scene_offset - self._scene_offset #modified
            self._change_offsets(track_increment, scene_increment)
        self.update()
            
    def _create_scene(self, num_tracks):
        return LaunchpadSceneComponent(num_tracks, self.tracks_to_use)
        
    def get_offsets(self):
        return (self._track_offset,self._scene_offset)
        
    def _stop_track_value(self, value, sender):
        assert (self._stop_track_clip_buttons != None)
        assert (list(self._stop_track_clip_buttons).count(sender) == 1)
        assert (value in range(128))
        if self.is_enabled():
            if ((value is not 0) or (not sender.is_momentary())):
                tracks = self.tracks_to_use()
                track_index = (list(self._stop_track_clip_buttons).index(sender) + self.track_offset())
                if (track_index in range(len(tracks))) and (tracks[track_index] in self.song().tracks):
                    tracks[track_index].stop_all_clips()
                                    
    def _on_fired_slot_index_changed(self, index):
        if (self._stop_track_clip_buttons != None):
            if ((index in range(len(self._tracks_and_listeners))) and (self._tracks_and_listeners[index][0] in self.song().tracks) and (self._tracks_and_listeners[index][0].fired_slot_index == -2)):
                self._stop_track_clip_buttons[index].send_value(self._stop_track_clip_value)
            else:
                self._stop_track_clip_buttons[index].turn_off()