import Live

import launchpadbuttoncomponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement

'''
todo:
    sub mode management
'''

from launchpadsessioncomponent import LaunchpadSessionComponent
from launchpadbuttoncomponent import LaunchpadButtonComponent
from launchpadmode import LaunchpadMode
from launchpadmixercomponent import LaunchpadMixerComponent
from launchpadbuttonslidercomponent import LaunchpadButtonSliderElement

from launchpadmixerlut import *

#used for bitfields of the commands to be sent to the launchpad
MIXER_BUTTON = 0x6F


MIXER_STATE_INIT = 0
MIXER_STATE_MAIN = 1

MIXER_STATE_VOL  = 2
MIXER_STATE_PAN  = 3
MIXER_STATE_SEND_A = 4
MIXER_STATE_SEND_B = 5
MIXER_STATE_SEND_C = 6
MIXER_STATE_SEND_D = 7
MIXER_STATE_MASTER = 8

ONED = 1
TWOD = 2
BAR  = 3
SPRD = 4
PAN  = 5
QUAL = 6
CUT  = 7
DAMP = 8
SING = 9

class LaunchpadMixerMode(LaunchpadMode):
    
    def __init__(self, nav, layout, mode_reset_button=None):
        LaunchpadMode.__init__(self)
        self._layout = layout
        self._nav = nav
        self._state = MIXER_STATE_INIT
        self._enable = False
        self._mixer = LaunchpadMixerComponent(8, 4)
        self._current_tracks = None
        self._channel_volume = []
        self._channel_pan = []
        self._channel_send = []
        self._senda = []
        self._sendb = []
        self._sendc = []
        self._sendd = []
        self._master_volume = None
        self._cue = None
        self._master = self._mixer.master_strip()
        self._nav.add_offset_listener(self.update_track_offset)
        self._function_mappings = {MIXER_STATE_INIT   : (None,None),
                                   MIXER_STATE_MAIN   : (self.create_main,self.destroy_main),
                                   MIXER_STATE_VOL    : (self.create_vol,self.destroy_vol),
                                   MIXER_STATE_PAN    : (self.create_pan,self.destroy_pan),
                                   MIXER_STATE_SEND_A : (self.create_sda,self.destroy_sda),
                                   MIXER_STATE_SEND_B : (self.create_sdb,self.destroy_sdb),
                                   MIXER_STATE_SEND_C : (self.create_sdc,self.destroy_sdc),
                                   MIXER_STATE_SEND_D : (self.create_sdd,self.destroy_sdd),
                                   MIXER_STATE_MASTER : (self.create_master,self.destroy_master)}
        self._mode_reset_button = mode_reset_button
        if self._mode_reset_button != None:
            self._mode_reset_button.add_value_listener(self.mode_reset_caller)
        
    def mode_reset_caller(self,value):
        if self._enable == True:
            self.set_state(MIXER_STATE_MAIN)
        
    def enable(self, buttons):
        self._layout.set_grid_mapping_mode(1)
        self.update_track_offset(True)
        self._current_tracks = self._mixer.get_channel_strips()
        self.mode_change_buttons()
        self.set_state(MIXER_STATE_MAIN)
        self._enable = True        
        for i in range(len(buttons)):
            buttons[i].turn_on()
        return None
    
    def disable(self, buttons):
        layout = self._layout.get_active_mapping_array()
        self.set_state(MIXER_STATE_INIT)
        
        self._enable = False
        
        for i in range(len(buttons)):
            buttons[i].turn_off()
        return None
            
    def update_track_offset(self,init=False):
        if((self._enable == True ) or (init)):
            offset = self._nav.get_offsets()
            self._mixer.set_track_offset(offset[0])
    
    def disconnnect():
        for i in range(8):
            for j in range(8):
                layout[i][j].turn_off()
                
        for i in range(len(self._current_tracks)):
            self._current_tracks[i].disconnect()
        
        self._nav.remove_offset_listener(self.update_track_offset)
        return None

    def set_state(self, state):
        #first cleanup the old state
            if state != self._state:
                func = self._function_mappings[self._state][1]
                if (func != None):
                    func()
            self._state = state
            self.update_mode_change_buttons()
            func = self._function_mappings[self._state][0]
            if (func != None):
                func()
            
    
    def create_main(self):
        self.main_vol_mode()
        self.main_pan_mode()
        self.main_snd_mode()
        self.main_buttons()
        return None
    
    def destroy_main(self):
        layout = self._layout.get_active_mapping_array()
        
        for i in range(len(self._current_tracks)):
            if(self._current_tracks[i]._volume_control != None):
                self._current_tracks[i]._volume_control.release_parameter()
                self._current_tracks[i]._volume_control = None
            if(self._current_tracks[i]._pan_control != None):
                self._current_tracks[i]._pan_control.release_parameter()
                self._current_tracks[i]._pan_control = None
            if(self._current_tracks[i]._send_controls != None):    
                for button in self._current_tracks[i]._send_controls:
                    button.release_parameter()
                self._current_tracks[i]._send_controls = None
            if (self._current_tracks[i]._mute_button != None): 
                self._current_tracks[i]._mute_button.remove_value_listener(self._current_tracks[i]._mute_value) 
                self._current_tracks[i]._mute_button.set_on_off_values()
                self._current_tracks[i]._mute_button = None 
            if (self._current_tracks[i]._solo_button != None): 
                self._current_tracks[i]._solo_button.remove_value_listener(self._current_tracks[i]._solo_value) 
                self._current_tracks[i]._solo_button.set_on_off_values()
                self._current_tracks[i]._solo_button = None 
            if (self._current_tracks[i]._arm_button != None): 
                self._current_tracks[i]._arm_button.remove_value_listener(self._current_tracks[i]._arm_value) 
                self._current_tracks[i]._arm_button.set_on_off_values()
                self._current_tracks[i]._arm_button = None
            if (self._current_tracks[i]._stopall_button != None):
                self._current_tracks[i].remove_stopall_button()
                self._current_tracks[i]._stopall_button.set_on_off_values()
                self._current_tracks[i]._stopall_button = None
                
        #f =
    
        #remove master stopall
        self._mixer.remove_master_stopall_button(layout[4][8])
        self._mixer.remove_master_mute_button(layout[5][8])
        self._mixer.remove_master_solo_button(layout[6][8])
        self._mixer.remove_master_arm_button(layout[7][8])

        #for row in range(len(layout)):
        #    for column in range(len(layout[row])):
        #        if row in range (4) and column == 8:
        #            pass
        #        else:
        #            layout[row][column].send_value(4)
                    
    def create_vol(self):
        self.vol_mode()
    
    def destroy_vol(self):
        pass
        
    
    def create_pan(self):
        pass
    
    def destroy_pan(self):
        pass
    
    
    def create_sda(self):
        pass
    
    def destroy_sda(self):
        pass
    
    
    def create_sdb(self):
        pass
    
    def destroy_sdb(self):
        pass
    
    
    def create_sdc(self):
        pass
    
    def destroy_sdc(self):
        pass
    
    
    def create_sdd(self):
        pass
    
    def destroy_sdd(self):
        pass
    
    
    def create_master(self):
        pass
    
    def destroy_master(self):
        pass
        
    def main_vol_mode(self):
        buttons = self._layout.get_mapping_mode(1)
        
        if len(self._current_tracks) > 0:
            for i in range(len(self._current_tracks)):
                sbs = LaunchpadButtonSliderElement((buttons[0][i],),SING,SING_VOL_LUT,False,60,28)
                self._channel_volume.append(sbs)
                self._current_tracks[i].set_volume_control(self._channel_volume[i])
   
    def main_pan_mode(self):
        buttons = self._layout.get_mapping_mode(1)
        
        for i in range(len(self._current_tracks)):
            sbs = LaunchpadButtonSliderElement((buttons[1][i],),SING,SING_PAN_LUT,False,60,28)
            self._channel_pan.append(sbs)
            self._current_tracks[i].set_pan_control(self._channel_pan[i])
    
    def main_snd_mode(self):
        buttons = self._layout.get_mapping_mode(1)
        for i in range(len(self._current_tracks)):
            senda = LaunchpadButtonSliderElement((buttons[2][i],),SING,SING_SEND_LUT,False,60,28)
            sendb = LaunchpadButtonSliderElement((buttons[3][i],),SING,SING_SEND_LUT,False,60,28)
            sbs = (senda,sendb)
            self._channel_send.append(sbs)
            self._current_tracks[i].set_send_controls(self._channel_send[-1])
                
    def main_buttons(self):
        buttons = self._layout.get_mapping_mode(1)
        
        for i in range(len(self._current_tracks)):
            buttons[4][i].set_on_off_values(15,63)
            self._current_tracks[i].set_stopall_button(buttons[4][i]) #stopall buttons
            
            buttons[5][i].set_on_off_values(29,63)
            self._current_tracks[i].set_mute_button(buttons[5][i])  #mute button
                
            buttons[6][i].set_on_off_values(15,13)
            self._current_tracks[i].set_solo_button(buttons[6][i])  #solo buttons
                
            buttons[7][i].set_on_off_values(15,13)
            self._current_tracks[i].set_arm_button(buttons[7][i])   #arm buttons
    
        #set the 4 mass-default buttons (stop trkon solo and arm)
        buttons[4][8].set_on_off_values(13,4)
        self._mixer.set_master_stopall_button(buttons[4][8])
        
        buttons[5][8].set_on_off_values(63,4)
        self._mixer.set_master_mute_button(buttons[5][8])
        
        buttons[6][8].set_on_off_values(13,4)
        self._mixer.set_master_solo_button(buttons[6][8])
        
        buttons[7][8].set_on_off_values(13,4)
        self._mixer.set_master_arm_button(buttons[7][8])
              
    def mode_change_buttons(self):
        buttons = self._layout.get_mapping_mode(1)

        buttons[0][8].add_value_listener(lambda x:self.set_state(MIXER_STATE_VOL))
        buttons[0][8].send_value(28)
        
        buttons[1][8].add_value_listener(lambda x:self.set_state(MIXER_STATE_PAN))
        buttons[1][8].send_value(28)
        
        buttons[2][8].add_value_listener(lambda x:self.set_state(MIXER_STATE_SEND_A))
        buttons[2][8].send_value(28)
        
        buttons[3][8].add_value_listener(lambda x:self.set_state(MIXER_STATE_SEND_B))
        buttons[3][8].send_value(28)
                
    def update_mode_change_buttons(self):
        buttons = self._layout.get_mapping_mode(1)
        if self._state == MIXER_STATE_MAIN:
            buttons[0][8].send_value(28)
            buttons[1][8].send_value(28)
            buttons[2][8].send_value(28)
            buttons[3][8].send_value(28)
        if self._state == MIXER_STATE_VOL:
            buttons[0][8].send_value(60)
            buttons[1][8].send_value(28)
            buttons[2][8].send_value(28)
            buttons[3][8].send_value(28)
        if self._state == MIXER_STATE_PAN:
            buttons[0][8].send_value(28)
            buttons[1][8].send_value(60)
            buttons[2][8].send_value(28)
            buttons[3][8].send_value(28)
        if self._state == MIXER_STATE_SEND_A:
            buttons[0][8].send_value(28)
            buttons[1][8].send_value(28)
            buttons[2][8].send_value(60)
            buttons[3][8].send_value(28)
        if self._state == MIXER_STATE_SEND_B:
            buttons[0][8].send_value(28)
            buttons[1][8].send_value(28)
            buttons[2][8].send_value(28)
            buttons[3][8].send_value(60)

#MIXER_STATE_SEND_B = 5
#MIXER_STATE_SEND_C = 6
#MIXER_STATE_SEND_D = 7
#MIXER_STATE_MASTER = 8
    
    def vol_mode(self):
        buttons = self._layout.get_mapping_mode(1)
        #first set up the 1 button vol/pan/send/send controls
        self._channel_volume = []
        for i in range(len(self._current_tracks)):
            vertical_button_slider = []
            for j in range(len(buttons)):
                vertical_button_slider.append(buttons[j][i])
            vertical_button_slider.reverse()
            c_v = LaunchpadButtonSliderElement(tuple(vertical_button_slider),BAR,VOLUME_LUT, False)
            self._channel_volume.append(c_v)
            self._current_tracks[i].set_volume_control(self._channel_volume[i])
                
        f = open("C:\log", "a")
        f.write("vol_mode_activated")
        f.close()
    def pan_mode(self):
        buttons = self._layout.get_mapping_mode(1)
        
        if(self._channel_pan == []):
            for i in range(len(self._current_tracks)):
                vertical_button_slider = []
                for j in range(len(buttons)):
                    vertical_button_slider.append(buttons[j][i])
                vertical_button_slider.reverse()
                c_v = LaunchpadButtonSliderElement(tuple(vertical_button_slider),PAN,PAN_LUT,False,63)
                self._channel_pan.append(c_v)
                self._current_tracks[i].set_pan_control(self._channel_pan[i])
       
    def snda_mode(self):
        buttons = self._layout.get_mapping_mode(1)
        #first set up the 1 button vol/pan/send/send controls
        if(self._senda != []):
            self._senda = []
        for i in range(len(self._current_tracks)):
            vertical_button_slider = []
            for j in range(len(buttons)):
                vertical_button_slider.append(buttons[j][i])
            vertical_button_slider.reverse()
            c_v = LaunchpadButtonSliderElement(tuple(vertical_button_slider),BAR,SEND_LUT,False,15)
            self._senda.append(c_v)
            self._current_tracks[i].set_send_controls((self._senda[i],None,None,None))
    
    def sndb_mode(self):
        buttons = self._layout.get_mapping_mode(1)
        #first set up the 1 button vol/pan/send/send controls
        if(self._sendb != []):
            self._sendb = []
        for i in range(len(self._current_tracks)):
            vertical_button_slider = []
            for j in range(len(buttons)):
                vertical_button_slider.append(buttons[j][i])
            vertical_button_slider.reverse()
            c_v = LaunchpadButtonSliderElement(tuple(vertical_button_slider),BAR,SEND_LUT,False,15)
            self._sendb.append(c_v)
            self._current_tracks[i].set_send_controls((None,self._sendb[i],None,None))
    
    def sndc_mode(self):
        buttons = self._layout.get_mapping_mode(1)
        #first set up the 1 button vol/pan/send/send controls
        if(self._senda != []):
            self._senda = []
        for i in range(len(self._current_tracks)):
            vertical_button_slider = []
            for j in range(len(buttons)):
                vertical_button_slider.append(buttons[j][i])
            vertical_button_slider.reverse()
            c_v = LaunchpadButtonSliderElement(tuple(vertical_button_slider),BAR,SEND_LUT,False,15)
            self._senda.append(c_v)
            self._current_tracks[i].set_send_controls((None, None, self._senda[i],None))
    
    def sndd_mode(self):
        buttons = self._layout.get_mapping_mode(1)
        #first set up the 1 button vol/pan/send/send controls
        if(self._sendd != []):
            self._sendd = []
        for i in range(len(self._current_tracks)):
            vertical_button_slider = []
            for j in range(len(buttons)):
                vertical_button_slider.append(buttons[j][i])
            vertical_button_slider.reverse()
            c_v = LaunchpadButtonSliderElement(tuple(vertical_button_slider),BAR,SEND_LUT,False,15)
            self._sendd.append(c_v)
            self._current_tracks[i].set_send_controls((None,None,None,self._sendd[i]))
    
    def master_mode(self):
        pass
