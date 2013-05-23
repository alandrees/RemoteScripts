import Live


from launchpadbuttoncomponent import LaunchpadButtonComponent

class LaunchpadCueControl():
    
    def __init__(self, cue_buttons, offset=0,cue_tracks=None):
        from launchpadmixercomponent import LaunchpadMixerComponent
        self._buttons = cue_buttons
        self._track_offset = offset
        self._cue_tracks = []
        self._cue_state = -1
        if cue_tracks != None:
            self._cue_tracks = cue_tracks
        
        self._cue_mixer = LaunchpadMixerComponent(len(cue_buttons)+offset)
        
        for i in range(len(cue_buttons)):
            self._cue_tracks.append(self._cue_mixer.channel_strip(self._track_offset + i))
            
        for j in xrange(len(cue_buttons)):
            x = self._generate_lambda(j)
            self._buttons[j].add_value_listener(x)            
    
    def cue_state_change(self, state, value):
        if value != 0:
            if self._cue_state == state:
                state = -1
            for i in range(len(self._cue_tracks)):
                if i == state:
                    self._cue_tracks[i].external_solo_trigger(127)
                    self._buttons[i].turn_on()
                else:
                    self._cue_tracks[i].external_solo_trigger(0)
                    self._buttons[i].turn_off()
                self._cue_state = state
        pass
        
    def _generate_lambda(self,state):
        return lambda value: self.cue_state_change(state, value)
        
        