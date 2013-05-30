import Live

#control surface components
from _Framework.EncoderElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *

class BCR2000():
    """encapsulates the BCR2000 controller"""
    
    def __init__(self):
        """initializer for the BCR2000 controller->object mappings"""
        self._midi_channel = 0
        self.main_encoders = [] 
        self.buttons = [] 
        self.encoder_groups = []
        self.encoder_buttons = []

    #Column 1 (Left)
        self.main_encoders.append([])
        self.main_encoders[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 81,Live.MidiMap.MapMode.absolute))
        self.main_encoders[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 89,Live.MidiMap.MapMode.absolute))
        self.main_encoders[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 97,Live.MidiMap.MapMode.absolute))
        
    #Column 2
        self.main_encoders.append([])
        self.main_encoders[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 82,Live.MidiMap.MapMode.absolute))
        self.main_encoders[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 90,Live.MidiMap.MapMode.absolute))
        self.main_encoders[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 98,Live.MidiMap.MapMode.absolute))

    #Column 3
        self.main_encoders.append([])
        self.main_encoders[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 83,Live.MidiMap.MapMode.absolute))
        self.main_encoders[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 91,Live.MidiMap.MapMode.absolute))
        self.main_encoders[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 99,Live.MidiMap.MapMode.absolute))

    #Column 4
        self.main_encoders.append([])
        self.main_encoders[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 84,Live.MidiMap.MapMode.absolute))
        self.main_encoders[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 92,Live.MidiMap.MapMode.absolute))
        self.main_encoders[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 100,Live.MidiMap.MapMode.absolute))

    #Column 5
        self.main_encoders.append([])
        self.main_encoders[4].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 85,Live.MidiMap.MapMode.absolute))
        self.main_encoders[4].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 93,Live.MidiMap.MapMode.absolute))
        self.main_encoders[4].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 101,Live.MidiMap.MapMode.absolute))
        
    #Column 6
        self.main_encoders.append([])
        self.main_encoders[5].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 86,Live.MidiMap.MapMode.absolute))
        self.main_encoders[5].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 94,Live.MidiMap.MapMode.absolute))
        self.main_encoders[5].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 102,Live.MidiMap.MapMode.absolute))
        
    #Column 7
        self.main_encoders.append([])
        self.main_encoders[6].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 87,Live.MidiMap.MapMode.absolute))
        self.main_encoders[6].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 95,Live.MidiMap.MapMode.absolute))
        self.main_encoders[6].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 103,Live.MidiMap.MapMode.absolute))

    #Column 8
        self.main_encoders.append([])
        self.main_encoders[7].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 88,Live.MidiMap.MapMode.absolute))
        self.main_encoders[7].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 96,Live.MidiMap.MapMode.absolute))
        self.main_encoders[7].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 104,Live.MidiMap.MapMode.absolute))
        
    #top row self.buttons
        self.buttons.append([])
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 65))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 66))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 67))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 68))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 69))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 70))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 71))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 72))

    #bottom row self.buttons
        self.buttons.append([])
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 73))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 74))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 75))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 76))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 77))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 78))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 79))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 80))

    #bottom self.buttons
        self.buttons.append([])
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 105))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 106))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 107))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 108))
    
    #first encoder group
        self.encoder_groups.append([])
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 1,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 2,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 3,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 4,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 5,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 6,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 7,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 8,Live.MidiMap.MapMode.absolute))

    #second encoder group
        self.encoder_groups.append([])
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 9,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 10,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 11,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 12,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 13,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 14,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 15,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 16,Live.MidiMap.MapMode.absolute))
        
    #third encoder group
        self.encoder_groups.append([])
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 17,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 18,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 19,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 20,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 21,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 22,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 23,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 24,Live.MidiMap.MapMode.absolute))

    #fourth encoder group
        self.encoder_groups.append([])
        self.encoder_groups.append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 17,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 18,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 19,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 20,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 21,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 22,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 23,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 24,Live.MidiMap.MapMode.absolute))

    ##ENCODER SELF.BUTTONS##
    #group one
        self.encoder_buttons.append([])
        self.encoder_buttons[0].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,33))
        self.encoder_buttons[0].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,34))
        self.encoder_buttons[0].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,35))
        self.encoder_buttons[0].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,36))
        self.encoder_buttons[0].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,37))
        self.encoder_buttons[0].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,38))
        self.encoder_buttons[0].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,39))
        self.encoder_buttons[0].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,40))

    #group two
        self.encoder_buttons.append([])
        self.encoder_buttons[1].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,41))
        self.encoder_buttons[1].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,42))
        self.encoder_buttons[1].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,43))
        self.encoder_buttons[1].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,44))
        self.encoder_buttons[1].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,45))
        self.encoder_buttons[1].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,46))
        self.encoder_buttons[1].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,47))
        self.encoder_buttons[1].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,48))

    #group three
        self.encoder_buttons.append([])
        self.encoder_buttons[2].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,49))
        self.encoder_buttons[2].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,50))
        self.encoder_buttons[2].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,51))
        self.encoder_buttons[2].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,52))
        self.encoder_buttons[2].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,53))
        self.encoder_buttons[2].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,54))
        self.encoder_buttons[2].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,55))
        self.encoder_buttons[2].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,56))

    #group four
        self.encoder_buttons.append([])
        self.encoder_buttons[3].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,57))
        self.encoder_buttons[3].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,58))
        self.encoder_buttons[3].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,59))
        self.encoder_buttons[3].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,60))
        self.encoder_buttons[3].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,61))
        self.encoder_buttons[3].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,62))
        self.encoder_buttons[3].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,63))
        self.encoder_buttons[3].append(ButtonElement(False,MIDI_CC_TYPE,self._midi_channel,64))

    def get_encoder_group(self,group):
       """this returns a list of encoder elements"""
       return self.encoder_groups[group -1]
        
    def get_encoders(self,row=-1):
       """this returns a list of fader elements"""
       if row == -1:
           return self.main_encoders
       else:
           return self.main_encoders[row]
        
    def get_buttons(self):
       """this returns a list of lists of button elements"""
       return self.buttons
       
    def get_encoder_buttons(self):
       """this returns a list of lists of button elements"""
       return self.encoder_buttons

    def get_midi_channel(self):
       """this returns the MIDI channel for the BCR2000"""
       return self._midi_channel
