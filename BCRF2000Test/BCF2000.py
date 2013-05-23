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
        self.encoders = []
        self.buttons = []
        self.faders = []

        #we are going to input this manually, so that it is easy to update later on:

        ##FADERS##
        self.faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 32))
        self.faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 33))
        self.faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 34))
        self.faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 35))
        self.faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 36))
        self.faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 37))
        self.faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 38))
        self.faders.append(SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 39))

        ##ENCODERS##
        #group 1, pan controls#
        self.encoders.append([])
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 102))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 103))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 104))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 105))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 106))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 107))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 108))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 109))
        
        #group 2, send A controls#
        self.encoders.append([])
        self.encoder[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 64))
        self.encoder[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 65))
        self.encoder[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 66))
        self.encoder[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 67))
        self.encoder[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 68))
        self.encoder[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 69))
        self.encoder[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 70))
        self.encoder[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 71))

        #group 3, send B controls#
        self.encoders.append([])
        self.encoder[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 72))
        self.encoder[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 73))
        self.encoder[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 74))
        self.encoder[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 75))
        self.encoder[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 76))
        self.encoder[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 77))
        self.encoder[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 78))
        self.encoder[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 79))

        #group 4, send C controls#
        self.encoders.append([])
        self.encoder[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 80))
        self.encoder[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 81))
        self.encoder[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 82))
        self.encoder[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 83))
        self.encoder[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 84))
        self.encoder[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 85))
        self.encoder[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 86))
        self.encoder[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 87))

        ##BUTTONS##
        
        #encoder buttons, all control groups, record buttons#
        self.buttons.append([])
        self.buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 56))
        self.buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 57))
        self.buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 58))
        self.buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 59))
        self.buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 60))
        self.buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 61))
        self.buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 62))
        self.buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 63))
        self.buttons[0].append(ButtonElement(True,MIDI_CC_TYPE, MIDI_CHANNEL, 64))

        #top row buttons, Track Enable Buttons#
        self.buttons.append([])
        self.buttons[1].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 40))
        self.buttons[1].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 41))
        self.buttons[1].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 42))
        self.buttons[1].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 43))
        self.buttons[1].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 44))
        self.buttons[1].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 45))
        self.buttons[1].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 46))
        self.buttons[1].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 47))

        #bottom row buttons, Record Buttons#
        self.buttons.append([])
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 48))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 49))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 50))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 51))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 52))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 53))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 54))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 55))
        
        #bottom buttons, purpose TBD#
        self.buttons.append([])
        self.buttons[3].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 89))
        self.buttons[3].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 90))
        self.buttons[3].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 91))
        self.buttons[3].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 92))
