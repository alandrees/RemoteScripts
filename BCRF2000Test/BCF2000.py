import Live

#control surface components
from _Framework.EncoderElement import *
from _Framework.SliderElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement.py import *

MIDI_CHANNEL = 2

class BCF2000():
    __doc__ = "BCF2000 grouping and logic for the controls on the surface"

    def __init__(self):
        self.main_faders = []

        self.encoder_groups = []
        self.encoder_buttons = []
        self.buttons = []

        #we are going to input this manually, so that it is easy to update later on:

        ##FADERS##
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 32))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 33))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 34))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 35))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 36))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 37))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 38))
        self.main_faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 39))

        ##ENCODERS##
        #group 1, pan controls#
        self.encoder_groups.append([])
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 102))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 103))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 104))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 105))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 106))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 107))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 108))
        self.encoder_groups[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 109))
        
        #group 2, send A controls#
        self.encoder_groups.append([])
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 64))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 65))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 66))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 67))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 68))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 69))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 70))
        self.encoder_groups[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 71))

        #group 3, send B controls#
        self.encoder_groups.append([])
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 72))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 73))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 74))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 75))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 76))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 77))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 78))
        self.encoder_groups[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 79))

        #group 4, send C controls#
        self.encoder_groups.append([])
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 80))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 81))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 82))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 83))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 84))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 85))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 86))
        self.encoder_groups[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 87))

        ##BUTTONS##
        
        #encoder buttons, all control groups, record buttons#
        self.encoder_buttons.append([])
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 56))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 57))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 58))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 59))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 60))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 61))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 62))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 63))
        self.encoder_buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 64))

        #top row buttons, Track Enable Buttons#
        self.buttons.append([])
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 40))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 41))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 42))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 43))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 44))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 45))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 46))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 47))

        #bottom row buttons, Record Buttons#
        self.buttons.append([])
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 48))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 49))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 50))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 51))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 52))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 53))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 54))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 55))
        
        #bottom buttons, purpose TBD#
        self.buttons.append([])
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 89))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 90))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 91))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 92))


        def get_encoder_group(self,group):
            #this returns a list of encoderelements
            return self.encoder_groups[group -1]
        
        def get_faders(self):
            #this returns a list of faderelements
            return self.main_faders
        
        def get_buttons(self):
            #this returns a list of lists of button elements
            return self.buttons
        
        def get_encoder_buttons(self):
            #this returns a list of lists of button elements
            return self.encoder_buttons

        def get_midi_channel(self):
            #this returns the MIDI channel for the BCF2000
            return MIDI_CHANNEL

        
