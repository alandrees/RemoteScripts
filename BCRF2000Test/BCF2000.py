import Live

#control surface components
from _Framework.EncoderElement import *
from _Framework.SliderElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *

class BCF2000():
    __doc__ = "BCF2000 grouping and logic for the controls on the surface"


    def __init__(self):

        self._midi_channel = 1
        self.main_faders = []
        self.encoder_groups = []
        self.encoder_buttons = []
        self.buttons = []

        #we are going to input this manually, so that it is easy to update later on:

        ##FADERS##
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, self._midi_channel, 32))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, self._midi_channel, 33))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, self._midi_channel, 34))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, self._midi_channel, 35))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, self._midi_channel, 36))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, self._midi_channel, 37))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, self._midi_channel, 38))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, self._midi_channel, 39))

        ##ENCODERS##
        #group 1, pan controls#
        self.encoder_groups.append([])
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 102,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 103,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 104,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 105,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 106,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 107,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 108,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 109,Live.MidiMap.MapMode.absolute))
      
        #group 2, send A controls#
        self.encoder_groups.append([])
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 64,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 65,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 66,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 67,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 68,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 69,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 70,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 71,Live.MidiMap.MapMode.absolute))

        #group 3, send B controls#
        self.encoder_groups.append([])
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 72,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 73,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 74,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 75,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 76,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 77,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 78,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 79,Live.MidiMap.MapMode.absolute))
        
    #group 4, send C controls#
        self.encoder_groups.append([])
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 80,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 81,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 82,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 83,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 84,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 85,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 86,Live.MidiMap.MapMode.absolute))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, self._midi_channel, 87,Live.MidiMap.MapMode.absolute))

    ##BUTTONS##
        
    #encoder buttons, all control groups, record buttons#
        self.encoder_buttons.append([])
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, self._midi_channel, 56))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, self._midi_channel, 57))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, self._midi_channel, 58))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, self._midi_channel, 59))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, self._midi_channel, 60))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, self._midi_channel, 61))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, self._midi_channel, 62))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, self._midi_channel, 63))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, self._midi_channel, 64))

    #top row buttons, Track Enable Buttons#
        self.buttons.append([])
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 40))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 41))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 42))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 43))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 44))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 45))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 46))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, self._midi_channel, 47))

    #bottom row self.buttons, Record Self.Buttons#
        self.buttons.append([])
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 48))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 49))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 50))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 51))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 52))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 53))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 54))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 55))
        
    #bottom self.buttons, purpose TBD#
        self.buttons.append([])
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 89))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 90))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 91))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, self._midi_channel, 92))

    def get_encoder_group(self,group):
       #this returns a list of encoderelements
        return self.encoder_groups[group -1]
        
    def get_faders(self):
       #this returns a list of faderelements
        return self.main_faders
        
    def get_buttons():
       #this returns a list of lists of button elements
        return self.buttons
         
    def get_encoder_buttons():
       #this returns a list of lists of button elements
        return self.encoder_buttons

    def get_midi_channel():
       #this returns the MIDI channel for the BCF2000
        return self._midi_channel

        
