import Live
from _Framework.SessionComponent import SessionComponent
from launchpadscenecomponent import LaunchpadSceneComponent
from launchpadsessioncomponent import LaunchpadSessionComponent
from launchpadbuttoncomponent import *
from launchpadbuttonmatrix import LaunchpadButtonMatrix
from _SharedComponents.

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
    
    def __init__(self):
        self.active_channel = 0
        #set the left, right and unlock both buttons
        self._ch_b_nav = None
        matrix = LaunchpadButtonMatrix(9,8,True,1)
        
        self.right_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,RIGHT_BUTTON)
        self.right_button.set_on_off_values(60,28)
        
        self.left_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,LEFT_BUTTON)
        self.left_button.set_on_off_values(60,28)
        
        self.down_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,DOWN_BUTTON)
        self.down_button.set_on_off_values(60,28)

        self.up_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,UP_BUTTON)
        self.up_button.set_on_off_values(60,28)
        
        self._ch_a_nav = LaunchpadSessionComponent(1,7,True)
                
        layout = matrix.get_mapping_mode(1)
        for scene_index in range(self._ch_a_nav.height()):
            scene = self._ch_a_nav.scene(scene_index)
            scene.name = 'Scene_' + str(scene_index)
            scene.set_triggered_value(BIT_4 + BIT_5 + BIT_3)
            for track_index in range(self._ch_a_nav.width()):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.name = str(track_index) + '_Clip_Slot_' + str(scene_index)
                clip_slot.set_triggered_to_play_value(BIT_4 + BIT_5 + BIT_3)
                clip_slot.set_stopped_value(BIT_4 + BIT_5 + BIT_1 + BIT_0 + BIT_3 + BIT_2)
                clip_slot.set_started_value(BIT_4 + BIT_5 + BIT_3 + BIT_2)
                clip_slot.set_noclip_value(BIT_2 + BIT_3)
                clip_slot.set_launch_button(layout[scene_index][track_index])
            layout[scene_index][track_index + 1].set_on_off_values(BIT_4 + BIT_5 + BIT_3,BIT_2 + BIT_3)
            
        self._ch_a_nav.set_stop_track_clip_buttons((layout[7][0],))
        layout[7][0].set_on_off_values(56 ,15)
        layout[7][0].turn_off()
        
        self.left_button.add_value_listener(self.left_button_trigger)
        self.left_button.turn_on()
        self.right_button.add_value_listener(self.right_button_trigger)
        self.right_button.turn_off()
        
        self.up_button.add_value_listener(self.up_button_trigger)
        self.down_button.add_value_listener(self.down_button_trigger)
        
    def left_button_trigger(self,index):
        if index == 127:
            if self.active_channel == 1:
                self.active_channel = 0
                self.left_button.turn_on()
                self.right_button.turn_off()
                self._ch_a_nav.set_enabled(True)
                if LaunchpadSessionManager._ch_b != None:
                    LaunchpadSessionManager._ch_b._ch_b_nav.set_enabled(False)
    
    def right_button_trigger(self,index):
        f = open("C:\log","a")
        f.write(str(LaunchpadSessionManager))
        f.close()
        if index == 127:
            if self.active_channel == 0:
                self.active_channel = 1
                self.right_button.turn_on()
                self.left_button.turn_off()
                self._ch_a_nav.set_enabled(False)
                if LaunchpadSessionManager._ch_b != None:
                    LaunchpadSessionManager._ch_b._ch_b_nav.set_enabled(True)
                
    def up_button_trigger(self,index):
        if index == 127:
            if self.active_channel == 0:
                offsets = self._ch_a_nav.get_offsets()
                if offsets[1] - 1 >= 0:
                    self._ch_a_nav.set_offsets(offsets[0],offsets[1] - 1)
            elif self.active_channel == 1:
                if LaunchpadSessionManager._ch_b != None:
                    offsets = LaunchpadSessionManager._ch_b._ch_b_nav.get_offsets()
                    if offsets[1] - 1 >= 0:
                        LaunchpadSessionManager._ch_b._ch_b_nav.set_offsets(offsets[0],offsets[1] - 1)
        
    def down_button_trigger(self,index):
        if index == 127:
            if self.active_channel == 0:
                offsets = self._ch_a_nav.get_offsets()
                self._ch_a_nav.set_offsets(offsets[0],offsets[1] + 1)
            elif self.active_channel == 1:
                if LaunchpadSessionManager._ch_b != None:
                    offsets = LaunchpadSessionManager._ch_b._ch_b_nav.get_offsets()
                    LaunchpadSessionManager._ch_b._ch_b_nav.set_offsets(offsets[0],offsets[1] + 1)