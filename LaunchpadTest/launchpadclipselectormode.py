import Live

#framework classes
from _Framework.ButtonElement import *
from _Framework.ButtonMatrixElement import *

#launchpad classes
from launchpadbuttoncomponent import LaunchpadButtonComponent
from launchpadmode import LaunchpadMode

from _AbletonPlus2.abletonlog import write_log

TRACK_BUTTON = 0x6D

class LaunchpadClipSelectionMode(LaunchpadMode):
    """implements the enabling/disabling of the features regarding track selection for the novation launchpad"""

    def __init__(self, layout, ap, song):
        """initalize the LaunchpadTrackSelectionMode.  index_mode = 0 is where you have 8 selections, index_mode = 1 is where you have 64 options"""
        LaunchpadMode.__init__(self, True)
        self._ap = ap
        self._layout = layout
        self._lambdas = []
        self._song = song
        self._offset = None
        self.clips = []
        for i in range(64):
            self._lambdas.append(lambda value,x=i: self.select_clip(value,x))


    def enable(self, buttons, oldmode):
        """this code is executed when this mode is enabled"""
        self._enable = True
        self._layout.set_grid_mapping_mode(1)
        
        layout = self._layout.get_active_mapping_array()
           
        for row in range(8):
            for column in range(8): 
                layout[row][column].add_value_listener(self._lambdas[((row * 8) + column)])
        
        for i in range(len(buttons)):
            buttons[i].turn_on()
        
        self._oldmode = oldmode

        #setup the clip calculation objects
        self._offset = self._ap.getter('master_grid_offset')

        

        for track in self._song.tracks[(self._offset[0]):(self._offset[0] + 8)]:
            self.clips.append(track.clip_slots[(self._offset[1]):(self._offset[1] + 8)])
        return True
                

    def select_clip(self, value, track_index):
        """select the clip slot, even if empty"""
        track = None
        if value == 1:
            #index mode 0 is the 8-track selection
            if (track_index == 0) or ((track_index % 8) == 0):
                track = 0
            elif (track_index == 1) or ((track_index % 8) - 1 == 0):
                track = 1
            elif (track_index == 2) or ((track_index % 8) - 2 == 0):
                track = 2
            elif (track_index == 3) or ((track_index % 8) - 3 == 0):
                track = 3
            elif (track_index == 4) or ((track_index % 8) - 4 == 0):
                track = 4
            elif (track_index == 5) or ((track_index % 8) - 5 == 0):
                track = 5
            elif (track_index == 6) or ((track_index % 8) - 6 == 0):
                track = 6
            elif (track_index == 7) or ((track_index % 8) - 7 == 0):
                track = 7

            
            #write_log(str(track) + " " + str(track_index / 8))
            self._song.view.highlighted_clip_slot = self.clips[track][track_index / 8]
    
    def disable(self, buttons, newmode):
        """this code is executed when this mode is disabled"""
        #make sure to remove the the track selection lambdas
        layout = self._layout.get_active_mapping_array()

        for row in range(8):
            for column in range(8): 
                layout[row][column].remove_value_listener(self._lambdas[((row * 8) + column)])          
        
                
        self._clips = []        
        for i in range(len(buttons)):
            buttons[i].turn_off()
        self._enable = False
        

