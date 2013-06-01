import Live

from _Framework.ButtonElement import *
from _Framework.ButtonMatrixElement import ButtonMatrixElement

from launchpadsessioncomponent import LaunchpadSessionComponent
from launchpadbuttoncomponent import LaunchpadButtonComponent
from launchpadmode import LaunchpadMode

#used for bitfields of the commands to be sent to the launchpad
BIT_0 = int(1)
BIT_1 = int(2)
BIT_2 = int(4)
BIT_3 = int(8)
BIT_4 = int(16)
BIT_5 = int(32)

SESSION_BUTTON = 0x6C

SESSION_MODE = 1
class LaunchpadSessionMode(LaunchpadMode):
    
    def __init__(self, nav, layout):
        LaunchpadMode.__init__(self)
        self._nav = nav
        self._layout = layout

    def enable(self, buttons):
        self._enable = True
        self._layout.set_grid_mapping_mode(1)
        layout = self._layout.get_active_mapping_array()
        for scene_index in range(self._nav.height()):
            scene = self._nav.scene(scene_index)
            scene.name = 'Scene_' + str(scene_index)
            scene.set_triggered_value(BIT_4 + BIT_5 + BIT_3)
            for track_index in range(self._nav.width()):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.name = str(track_index) + '_Clip_Slot_' + str(scene_index)
                clip_slot.set_triggered_to_play_value(BIT_4 + BIT_5 + BIT_3)
                clip_slot.set_stopped_value(BIT_4 + BIT_5 + BIT_1 + BIT_0 + BIT_3 + BIT_2)
                clip_slot.set_started_value(BIT_4 + BIT_5 + BIT_3 + BIT_2)
                clip_slot.set_noclip_value(BIT_2 + BIT_3)
                clip_slot.set_launch_button(layout[scene_index][track_index])
            scene.set_launch_button(layout[scene_index][track_index + 1])
        for i in range(len(buttons)):
            buttons[i].turn_on()
        
        
        
        return None
    
    def disable(self, buttons):
        self._enable = False
        layout = self._layout.get_active_mapping_array()
        for scene_index in range(self._nav.height()):
            scene = self._nav.scene(scene_index)
            for track_index in range(self._nav.width()):
                clip_slot = scene.clip_slot(track_index)
                clip_slot._launch_button.remove_value_listener(clip_slot._launch_value)
                clip_slot._launch_button = None
            scene._launch_button.remove_value_listener(scene._launch_value)
            scene._launch_button = None
                
        layout = self._layout.get_active_mapping_array()
        
        for i in range(8):
            for j in range(8):
                layout[i][j].turn_off()
                
        for i in range(len(buttons)):
            buttons[i].turn_off()
            
        #self._nav.set_enabled(False)
        return None
