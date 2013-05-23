import Live
from launchpadsessioncomponent import LaunchpadSessionComponent
from launchpadbuttoncomponent import *
from launchpadbuttonmatrix import LaunchpadButtonMatrix
from launchpadcuecontrol import LaunchpadCueControl

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

class LaunchpadSessionManager(object):
    
    _ch_b = None
    matrix = None
    
    def __init__(self,channel):
        
        self.unlock_last_state = None
        
        if LaunchpadSessionManager.matrix == None:
            LaunchpadSessionManager.matrix = LaunchpadButtonMatrix(9,8,True,1)

        if channel == 0:
            self.setup_channel_a()
        elif channel == 1:
            self.setup_channel_b()
            
        self.setup_cue_buttons()
        self.setup_beatcounter_toggle()
        
    def setup_channel_a(self):
        self.active_channel = 0
        
        self.unlock_button = LaunchpadButtonComponent(True,MIDI_CC_TYPE,0,SESSION_BUTTON)
        self.unlock_button.set_on_off_values(11,13)
                
        self.right_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,RIGHT_BUTTON)
        self.right_button.set_on_off_values(60,28)
        
        self.left_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,LEFT_BUTTON)
        self.left_button.set_on_off_values(60,28)
        
        self.down_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,DOWN_BUTTON)
        self.down_button.set_on_off_values(60,28)

        self.up_button = LaunchpadButtonComponent(True, MIDI_CC_TYPE,0,UP_BUTTON)
        self.up_button.set_on_off_values(60,28)
        
        self._ch_a_nav = LaunchpadSessionComponent(1,7,True)
                
        layout = LaunchpadSessionManager.matrix.get_mapping_mode(1)
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
                clip_slot.set_highlight_button(layout[scene_index][track_index + 1])
            
        layout[7][0].set_on_off_values(11 ,15)
        self._ch_a_nav.set_stop_track_clip_buttons((layout[7][0],))
        self._ch_a_nav.set_stop_track_clip_value(11)
        
        self.left_button.add_value_listener(self.left_button_trigger)
        self.left_button.turn_on()
        
        self.right_button.add_value_listener(self.right_button_trigger)
        self.right_button.turn_off()
        
        self.up_button.add_value_listener(self.up_button_trigger)
        self.up_button.turn_off()
        
        self.down_button.add_value_listener(self.down_button_trigger)
        self.down_button.turn_on()
    
        self.unlock_button.add_value_listener(self.unlock_button_trigger)
        self.unlock_button.turn_off()
        
        
    def setup_channel_b(self):
        self._ch_b_nav = LaunchpadSessionComponent(1,7,True)
        self._ch_b_nav.set_offsets(7,0)
        
        layout = LaunchpadSessionManager.matrix.get_mapping_mode(1)
        
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
            clip_slot.set_highlight_button(layout[scene_index][6])
        
        self._ch_b_nav.set_stop_track_clip_buttons((layout[7][7],))
        layout[7][7].set_on_off_values(11,15)
        layout[7][7].turn_off()
        self._ch_b_nav.set_stop_track_clip_value(11)
        
        self._ch_b_nav.set_enabled(False)
        
        LaunchpadSessionManager._ch_b = self
        
    def setup_cue_buttons(self):
        layout = LaunchpadSessionManager.matrix.get_mapping_mode(1)
        self._a_cue = LaunchpadCueControl([layout[7][1],layout[7][2],layout[7][3]], 1)
        self._a_cue = LaunchpadCueControl([layout[7][4],layout[7][5],layout[7][6]], 4)

    def setup_beatcounter_toggle(self):
        pass
        
    def left_button_trigger(self,value):
        if value != 0:
            if self.active_channel != 0:
                self.active_channel = 0
                self.left_button.turn_on()
                self.right_button.turn_off()
                self.unlock_button.turn_off()
                self._ch_a_nav.set_enabled(True)
                if LaunchpadSessionManager._ch_b != None:
                    LaunchpadSessionManager._ch_b._ch_b_nav.set_enabled(False)
                self.unlock_last_state = None
            self.update_nav_buttons(127)
    
    def right_button_trigger(self,value):
        if value != 0:
            if self.active_channel != 1:
                self.active_channel = 1
                self.right_button.turn_on()
                self.left_button.turn_off()
                self.unlock_button.turn_off()
                self._ch_a_nav.set_enabled(False)
                if LaunchpadSessionManager._ch_b != None:
                    LaunchpadSessionManager._ch_b._ch_b_nav.set_enabled(True)
                self.unlock_last_state = None
            self.update_nav_buttons(127)
    
    def unlock_button_trigger(self, value):
        if value != 0:
            if self.active_channel != -1:
                self.unlock_last_state = self.active_channel
                self.active_channel = -1
                self.right_button.send_value(13)
                self.left_button.send_value(13)
                self.unlock_button.turn_on()
                self._ch_a_nav.set_enabled(True)
                if LaunchpadSessionManager._ch_b != None:
                        LaunchpadSessionManager._ch_b._ch_b_nav.set_enabled(True)
            elif self.active_channel == -1:
                if self.unlock_last_state == 0:
                    self.left_button_trigger(127)
                elif self.unlock_last_state == 1:
                    self.right_button_trigger(127)
                
    def up_button_trigger(self,value):
        if value != 0:
            if self.active_channel == 0:
                offsets = self._ch_a_nav.get_offsets()
                if offsets[1] - 1 >= 0:
                    self._ch_a_nav.set_offsets(offsets[0],offsets[1] - 1)
            elif self.active_channel == 1:
                if LaunchpadSessionManager._ch_b != None:
                    offsets = LaunchpadSessionManager._ch_b._ch_b_nav.get_offsets()
                    if offsets[1] - 1 >= 0:
                        LaunchpadSessionManager._ch_b._ch_b_nav.set_offsets(offsets[0],offsets[1] - 1)
            self.update_nav_buttons(value)
        
    def down_button_trigger(self,value):
        if value != 0:
            if self.active_channel == 0:
                offsets = self._ch_a_nav.get_offsets()
                self._ch_a_nav.set_offsets(offsets[0],offsets[1] + 1)
            elif self.active_channel == 1:
                if LaunchpadSessionManager._ch_b != None:
                    offsets = LaunchpadSessionManager._ch_b._ch_b_nav.get_offsets()
                    LaunchpadSessionManager._ch_b._ch_b_nav.set_offsets(offsets[0],offsets[1] + 1)
        self.update_nav_buttons(value)
        
    def update_nav_buttons(self,value):
        if value != 0:
            if self.active_channel == 0:
                offsets = self._ch_a_nav.get_offsets()
                scenes = self._ch_a_nav.song().scenes
                track_offset = offsets[0]
                scene_offset = offsets[1]
                if (scene_offset > 0 and (self._ch_a_nav.height() - scene_offset) < self._ch_a_nav.height()):
                    self.up_button.turn_on()
                else:
                    self.up_button.turn_off()
                
                if (len(scenes) > (scene_offset + 7)):
                    self.down_button.turn_on()
                else:
                    self.down_button.turn_off()
            
            elif self.active_channel == 1:
                if LaunchpadSessionManager._ch_b != None:
                    offsets = LaunchpadSessionManager._ch_b._ch_b_nav.get_offsets()
                    scenes = LaunchpadSessionManager._ch_b._ch_b_nav.song().scenes
                    track_offset = offsets[0]
                    scene_offset = offsets[1]
                    if (scene_offset > 0 and (LaunchpadSessionManager._ch_b._ch_b_nav.height() - scene_offset) < LaunchpadSessionManager._ch_b._ch_b_nav.height()):
                        self.up_button.turn_on()
                    else:
                        self.up_button.turn_off()
                
                    if (len(scenes) > (scene_offset + 7)):
                        self.down_button.turn_on()
                    else:
                        self.down_button.turn_off()
