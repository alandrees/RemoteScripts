import Live 
from _Framework.ButtonElement import *

class LaunchpadButtonComponent(ButtonElement):
    ' Special button class that can be configured with custom on- and off-values '
    
    def __init__(self, is_momentary, msg_type, channel, identifier):
        ButtonElement.__init__(self, is_momentary, msg_type, channel, identifier)
        self._on_value = 60
        self._off_value = 4
        self._is_enabled = True
        self._is_notifying = False
        self._force_next_value = False
        self._pending_listeners = []

    def set_on_off_values(self, on_value=60, off_value=4):
        if (on_value in range(128)) and (off_value in range(128)):
            self._on_value = on_value
            self._off_value = off_value
        
    def turn_on(self):
        self.send_value(self._on_value, True)
        
    def turn_off(self):
        self.send_value(self._off_value, True)
        
    #def send_value(self,value, force_send = False):
    #    ButtonElement.send_value(self, value, True)
        
    def on_value(self):
        return self._on_value
    
    def off_value(self):
        return self._off_value
    
    def update(self):
        return None
    
    def send_value(self, value, force_send = False):
        assert (value != None)
        assert isinstance(value, int)
        assert (value in range(128))
        data_byte1 = self._original_identifier
        data_byte2 = value
        status_byte = self._original_channel
        if (self._msg_type == MIDI_NOTE_TYPE):
            status_byte += MIDI_NOTE_ON_STATUS
        elif (self._msg_type == MIDI_CC_TYPE):
            status_byte += MIDI_CC_STATUS
        else:
            return
        if self.send_midi((status_byte, data_byte1, data_byte2)): #modified; added if
            if self._report_output:
                is_input = True
                self._report_value(value, (not is_input))
                
    def remove_all_listeners(self):
        self._value_notifications = {}