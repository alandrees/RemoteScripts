import Live
import math

from _Framework.SliderElement import SliderElement
from _Framework.InputControlElement import *
from _Framework.ButtonElement import ButtonElement

ONED = 1
TWOD = 2
BAR  = 3
SPRD = 4
PAN  = 5
QUAL = 6
CUT  = 7
DAMP = 8
SING = 9

#todo non-lut scaling functions for floating point calculations

class LaunchpadButtonSliderElement(SliderElement):

    ''' Class representing a set of buttons used as a slider, also supports  '''

    def __init__(self, buttons, type=BAR, lut=None, lut_high_res=False, on_value=60, off_value=4):
        assert (buttons != None)
        assert isinstance(buttons, tuple)
        SliderElement.__init__(self, MIDI_CC_TYPE, 0, 0)
        self._buttons = buttons
        self._last_button_lit = -1
        self._control_type = type
        self._on_value = on_value
        self._off_value = off_value
        if lut != None:
            if lut_high_res:
                self._lut = lut
                self._lut.reverse()
            else:
                self._lut = [lut[0]]
                self._lut.extend(lut[2::2])
                if(self._lut[-1] != 0.0):
                    self._lut.append(lut[-1])
                self._lut.reverse()
        else:
            self._lut = None
            
        if type == PAN:
            #calculate the center
            if (len(self._buttons) % 2) == 0:
                self._center = ( (len(self._buttons) / 2), (len(self._buttons) / 2) - 1)
            else:
                self._center = ((len(self._buttons) / 2),)            
        
        identify_sender = True
        
        if(len(self._buttons) == 1):
            self._control_type = SING
        
        for new_button in self._buttons:
            assert (new_button != None)
            assert isinstance(new_button, ButtonElement)
            new_button.add_value_listener(self._button_value, identify_sender)

    def disconnect(self):
        if (self._parameter_to_map_to != None):
            self._parameter_to_map_to.remove_value_listener(self._on_parameter_changed)
            SliderElement.disconnect(self)
        self._buttons = None


    def message_type(self):
        debug_print('message_type() should not be called directly on ButtonSliderElement')
        assert False


    def message_channel(self):
        debug_print('message_channel() should not be called directly on ButtonSliderElement')
        assert False


    def message_identifier(self):
        debug_print('message_identifier() should not be called directly on ButtonSliderElement')
        assert False


    def message_map_mode(self):
        debug_print('message_map_mode() should not be called directly on ButtonSliderElement')
        assert False


    def install_connections(self):
        pass


    def connect_to(self, parameter):
        if (self._parameter_to_map_to != None):
            self._parameter_to_map_to.remove_value_listener(self._on_parameter_changed)
        InputControlElement.connect_to(self, parameter)
        if (self._parameter_to_map_to != None):
            self._parameter_to_map_to.add_value_listener(self._on_parameter_changed)
            self._on_parameter_changed()


    def release_parameter(self):
        if (self._parameter_to_map_to != None):
            self._parameter_to_map_to.remove_value_listener(self._on_parameter_changed)
        InputControlElement.release_parameter(self)


    def status_byte(self):
        debug_print('status_byte() should not be called directly on ButtonSliderElement')
        assert False


    def send_value(self, value):
        if(self._control_type == ONED):
            self._send_oned(value)
        elif(self._control_type == TWOD):
            self._send_twod(value)
        elif(self._control_type == BAR):
            self._send_bar(value)
        elif(self._control_type == SPRD):
            self._send_(value)
        elif(self._control_type == PAN):
            self._send_pan(value)
        elif(self._control_type == QUAL):
            self._send_cut(value)
        elif(self._control_type == DAMP):
            self._send_damp(value)
        elif(self._control_type == SING):
            self._send_sing(value)
            
    def _send_bar(self, value):
        index_to_light = -1
        
        #another way to solve the bar mapping problem is set ranges for each value based on the LUT...
        #as it's mathematically derived and fairly linear when it doesn't use the LUT, it's not really an issue
        #but when using a non linear LUT set, map ranges to each button, and if it falls within a certain range, then set the index_to_light equal to that
        #should work fairly well (did that for the pan controls)
        
        if (value > 0):
            index_to_light = int((((len(self._buttons)) * value) / 127))
        for index in range(len(self._buttons)):
            if (index <= index_to_light):
                self._buttons[index].send_value(self._on_value, True)
            else:
                self._buttons[index].send_value(self._off_value, True)
        self._last_button_lit = index_to_light
    
    def _send_pan(self, value):
        #do the pan thing
       
        number_of_values = (len(self._buttons) - len(self._center)) / 2
        
        range_per_value = int(127 / number_of_values)
        number_of_buttons = 0
        
        j = 0
        if (value > 0):
            for i in range(1, number_of_values + 1):
                if abs(range_per_value * (i) - value) <= 5:
                    break
            number_of_buttons = i
            
            if(self._parameter_to_map_to.value > 0.0):
                on_values = [self._center[1]]
                for j in range(number_of_buttons):
                    on_values.append(self._center[1] - (j + 1))
            else:
                on_values = [self._center[0]]
                for j in range(number_of_buttons):
                    on_values.append(self._center[0] + (j + 1))
        else:
            on_values = self._center
        
        for index in range(len(self._buttons)):
            if index in on_values:
                self._buttons[index].send_value(self._on_value,True)
            else:
                self._buttons[index].send_value(self._off_value,True)
    
    def _send_sing(self, value):
        if(value == 0):
            self._buttons[0].send_value(self._off_value,True)
        else:
            self._buttons[0].send_value(self._on_value,True)
            
    def _send_oned(self, value):
        pass
    
    def _send_twod(self, value):
        pass

    def _send_sprd(self, value):
        pass
    
    def _send_qual(self, value):
        pass
    
    def _send_cut(self,value):
        pass
    
    def _send_damp(self,value):
        pass
            
    def _value_bar(self,value, sender):
        index_of_sender = list(self._buttons).index(sender)
            
        midi_value = int((127 * ((index_of_sender) / (len(self._buttons) - 1))))
        
        
        if (self._parameter_to_map_to != None) and self._parameter_to_map_to.is_enabled:
                
            if(self._lut != None):
                if(len(self._buttons) == len(self._lut)):
                    param_value = self._lut[index_of_sender]
                else:
                    position = round(index_of_sender / len(self._buttons), 0) * (len(self._buttons) / len(self._lut))
                    if position in range(len(self._lut)):
                        param_value = self._lut[int(position)]
            else:
                
                param_range = (self._parameter_to_map_to.max - self._parameter_to_map_to.min)
                temp = param_range / len(self._buttons)
                param_value = temp * index_of_sender + self._parameter_to_map_to.min
                if (index_of_sender > 0):
                
                    param_value += param_range / (len(self._buttons)**2)
                                       
                    if ( (param_value > self._parameter_to_map_to.max) or (list(self._buttons).index(sender) == ( len(self._buttons) - 1 )) ):
                        param_value = self._parameter_to_map_to.max
                    else:
                        param_value = 0
                                      
        return (param_value,midi_value)
    
    def _value_pan(self, value, sender):
        
        index_of_sender = list(self._buttons).index(sender)
        midi_value = int((127 * ((index_of_sender) / (len(self._buttons) - 1))))
        #f = open("C:\log","a")
        

        param_value = 0                
                
        if (self._parameter_to_map_to != None) and self._parameter_to_map_to.is_enabled:
                
            if(self._lut != None):
                if index_of_sender in self._center:
                    param_value = self._lut[0]
                else:
                    if(len(self._center) == 2):
                        if max(index_of_sender,self._center[0],self._center[1]) == index_of_sender:
                            #f.write(str(self._lut[0]) + " " + str(index_of_sender) + " " + str(self._center[0]))
                            param_value = self._lut[0] - self._lut[abs(index_of_sender - self._center[0])]
                                       
                        if max(index_of_sender,self._center[0],self._center[1]) != index_of_sender:
                            #f.write(str(self._lut[0]) + " " + str(self._center[1]) + " " + str(index_of_sender))
                            param_value = self._lut[0] + self._lut[abs(self._center[1] - index_of_sender)]
                    else:
                        if max(index_of_sender,self._center[0]) == index_of_sender:
                            param_value = self._lut[0] - self._lut[index_of_sender - self._center[0]]
                        if max(index_of_sender,self._center[0]) != index_of_sender:
                            param_value = self._lut[0] + self._lut[abs(index_of_sender - self._center[0])]
            else:
                a = 0
                
        #f.close()                
        return (param_value, midi_value)
    
    def _value_sing(self, value, sender):
        return (self._lut[0],127)
    
    def _button_value(self, value, sender):
        
        self._last_sent_value = -1
        
        if ((value != 0) or (not sender.is_momentary())):
            
            if(self._control_type == BAR):
                param_value = self._value_bar(value,sender)
            elif(self._control_type == PAN):
                param_value = self._value_pan(value, sender)
            elif(self._control_type == SING):
                param_value = self._value_sing(value, sender)
            
            if(self._parameter_to_map_to != None):
                self._parameter_to_map_to.value = param_value[0]
                
            
                
            #self._last_button_lit = index_of_sender
            
            for notification in self._value_notifications:
                callback = notification['Callback']
                if notification['Identify']:
                    callback(param_value[1], self)
                else:
                    callback(param_value[1])

    def _on_parameter_changed(self):
        assert (self._parameter_to_map_to != None)
        midi_value = None
        
        if(self._control_type == ONED):
            pass
        elif(self._control_type == TWOD):
            pass
        elif(self._control_type == BAR):
            param_range = abs((self._parameter_to_map_to.max - self._parameter_to_map_to.min)) 
            midi_value = int(((127 * abs((self._parameter_to_map_to.value - self._parameter_to_map_to.min))) / param_range))       
        elif(self._control_type == SPRD):
            pass
        elif(self._control_type == PAN):
            param_range = abs((self._parameter_to_map_to.max - self._parameter_to_map_to.min)) 
            midi_value = int(((127 * abs((self._parameter_to_map_to.value )))))
        elif(self._control_type == QUAL):
            pass
        elif(self._control_type == DAMP):
            pass
        elif(self._control_type == SING):
            param_range = abs((self._parameter_to_map_to.max - self._parameter_to_map_to.min))
            if(self._lut != None):
                if(abs(self._parameter_to_map_to.value - self._lut[0]) < 0.001):
                    midi_value = 0
                else:
                    midi_value = 127

        if(midi_value != None):
            self.send_value(midi_value)
            return True
        
        return False


    
        
#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
