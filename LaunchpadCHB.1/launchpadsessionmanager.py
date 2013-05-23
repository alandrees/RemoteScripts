import Live
from _Framework.SessionComponent import SessionComponent
from launchpadscenecomponent import LaunchpadSceneComponent
from launchpadsessioncomponent import LaunchpadSessionComponent
from launchpadbuttoncomponent import *
from launchpadbuttonmatrix import LaunchpadButtonMatrix

UP_BUTTON = 0x68
DOWN_BUTTON = 0x69
LEFT_BUTTON = 0x6A
RIGHT_BUTTON = 0x6B
SESSION_BUTTON = 0x6C
USER_1_BUTTON = 0x6D
USER_2_BUTTON = 0x6E
MIXER_BUTTON = 0x6F

BIT_0 = int(1)
BIT_1 = int(2)
BIT_2 = int(4)
BIT_3 = int(8)
BIT_4 = int(16)
BIT_5 = int(32)

class LaunchpadSessionManager():
    
    _ch_b = None
    
    def __init__(self):
        #set the left, right and unlock both buttons
        matrix = LaunchpadButtonMatrix(9,8,True,1)
        
        #right_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,RIGHT_BUTTON)
        #right_button.set_on_off_values(60,28)
        
        #left_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,LEFT_BUTTON)
        #left_button.set_on_off_values(60,28)
        
        #down_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,DOWN_BUTTON)
        #down_button.set_on_off_values(60,28)

        #up_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,UP_BUTTON)
        #up_button.set_on_off_values(60,28)
        
        #self._ch_a_nav = LaunchpadSessionComponent(1,7,True)
        
        
        self._ch_b_nav = LaunchpadSessionComponent(1,7,True)
        self._ch_b_nav.set_offsets(7,0)
        
        #self._ch_a_nav.set_show_highlight(True)
        
        layout = matrix.get_mapping_mode(1)
        
        for scene_index in range(7):
            scene = self._ch_b_nav.scene(scene_index)
            scene.name = 'Scene_' + str(scene_index)
            scene.set_triggered_value(BIT_4 + BIT_5 + BIT_3)
            track_index = 0
            clip_slot = scene.clip_slot(track_index)
            clip_slot.name = str(track_index) + '_Clip_Slot_' + str(scene_index)
            clip_slot.set_triggered_to_play_value(BIT_4 + BIT_5 + BIT_3)
            clip_slot.set_stopped_value(BIT_4 + BIT_5 + BIT_1 + BIT_0 + BIT_3 + BIT_2)
            clip_slot.set_started_value(BIT_4 + BIT_5 + BIT_3 + BIT_2)
            clip_slot.set_noclip_value(BIT_2 + BIT_3)
            clip_slot.set_launch_button(layout[scene_index][7])
            layout[scene_index][track_index + 1].set_on_off_values(BIT_4 + BIT_5 + BIT_3,BIT_2 + BIT_3)
        self._ch_b_nav.set_stop_track_clip_buttons((layout[7][7],))
        
        layout[7][7].set_on_off_values(60,15)
        layout[7][7].turn_off()
        self._ch_b_nav.set_enabled(False)
        
        LaunchpadSessionManager._ch_b = self
        
        