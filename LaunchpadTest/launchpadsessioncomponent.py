import Live
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonElement import *
from launchpadscenecomponent import LaunchpadSceneComponent
from abletonlog import write_log

class LaunchpadSessionComponent(SessionComponent):
    """Class Extension of the Sesion Component to utilize the Launchpad"""
    
    def __init__(self, x, y, constrain):
        SessionComponent.__init__(self, x, y)
        self._contstrain = constrain
        self.set_offsets(0,0)
        
        return None
    
    def _update_banking_buttons(self, track_offset, scene_offset):
        assert (self.is_enabled())
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
    
    #set the offsets to the specified x,y coords on the grid
    def set_offsets(self, track_offset, scene_offset):
        assert (track_offset >= 0)
        assert (scene_offset >= 0)
        track_increment = 0
        scene_increment = 0
        if self._is_linked():
            SessionComponent._perform_offset_change((track_offset - self._track_offset), (scene_offset - self._scene_offset)) 
        else:
            if ((len(self.tracks_to_use()) > track_offset + self.width() - 1) or track_offset == 0):
                track_increment = track_offset - self._track_offset  #modified
            if ((len(self.song().scenes) > scene_offset + self.height() - 1) or track_offset == 0):
                scene_increment = scene_offset - self._scene_offset #modified

            self._change_offsets(track_increment, scene_increment)
      
    def _change_offsets(self, track_increment, scene_increment):
        offsets_changed = (track_increment != 0) or (scene_increment != 0)
        if offsets_changed:
            self._track_offset += track_increment
            self._scene_offset += scene_increment
            assert (self._track_offset >= 0)
            assert (self._scene_offset >= 0)
            if (self._mixer != None):
                self._mixer.set_track_offset(self.track_offset())
        self._reassign_tracks()
        if offsets_changed:
            self._reassign_scenes()
            for callback in self._offset_callbacks:
                callback()
            if ((self.width() > 0) and (self.height() > 0)):
                self._do_show_highlight()
    
    def _create_scene(self, num_tracks):
        return LaunchpadSceneComponent(num_tracks, self.tracks_to_use)

    def get_offsets(self):
        return (self._track_offset,self._scene_offset)
