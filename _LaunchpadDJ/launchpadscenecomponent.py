import Live
from _Framework.SceneComponent import SceneComponent
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from launchpadclipslot import LaunchpadClipSlot


class LaunchpadSceneComponent(SceneComponent):
    
    def __init__(self,num_tracks, tracks_to_use):
        SceneComponent.__init__(self, num_tracks, tracks_to_use)
        self.set_allow_update(True)
        return None
    
    def _create_clip_slot(self):
        return LaunchpadClipSlot()
    
    def update(self):
        if self._scene != None and self.is_enabled():
            clip_index = self._track_offset
            
            tracks = self.song().tracks
            
            clip_slots = self._scene.clip_slots
            
            if self._track_offset > 0:
                real_offset = 0
                visible_tracks = 0
                while visible_tracks < self._track_offset and len(tracks) > real_offset:
                    if tracks[real_offset].is_visible:
                        visible_tracks += 1
                    real_offset += 1
                clip_index = real_offset
            
            for slot in self._clip_slots:
                
                while len(tracks) > clip_index and not tracks[clip_index].is_visible:
                    clip_index += 1
                if len(clip_slots) > clip_index:
                    slot.set_clip_slot(clip_slots[clip_index])
                else:
                    slot.set_clip_slot(None)
                clip_index += 1
            
            self._on_is_triggered_changed()
        else:
            if self._scene != None and (self.is_enabled() == False):
                for slot in self._clip_slots:
                    slot.update()
            else:
                
                for slot in self._clip_slots:
                    slot.set_clip_slot(None)
                if self.is_enabled() and self._launch_button != None:
                    self._launch_button.turn_off()
        return None