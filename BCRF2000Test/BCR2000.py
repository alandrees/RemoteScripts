import Live

#control surface components

from _Framework.EncoderElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *

MIDI_CHANNEL = 1
class BCR2000():
    
    def __init__(self):
        self.main_encoders = [] #main encoders, not grouped
        self.buttons = []
        self.encoder_groups = []
        self.encoder_buttons = []

        #Column 1 (Left)
        self.main_encoders.append([])
        self.main_encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 81))
        self.main_encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 89))
        self.main_encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 97))
        
        #Column 2
        self.main_encoders.append([])
        self.main_encoders[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 82))
        self.main_encoders[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 90))
        self.main_encoders[1].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 98))

        #Column 3
        self.main_encoders.append([])
        self.main_encoders[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 83))
        self.main_encoders[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 91))
        self.main_encoders[2].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 99))

        #Column 4
        self.main_encoders.append([])
        self.main_encoders[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 84))
        self.main_encoders[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 92))
        self.main_encoders[3].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 100))

        #Column 5
        self.main_encoders.append([])
        self.main_encoders[4].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 85))
        self.main_encoders[4].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 93))
        self.main_encoders[4].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 101))
        
        #Column 6
        self.main_encoders.append([])
        self.main_encoders[5].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 86))
        self.main_encoders[5].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 94))
        self.main_encoders[5].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 102))
        
        #Column 7
        self.main_encoders.append([])
        self.main_encoders[6].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 87))
        self.main_encoders[6].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 95))
        self.main_encoders[6].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 103))

        #Column 8
        self.main_encoders.append([])
        self.main_encoders[7].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 88))
        self.main_encoders[7].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 96))
        self.main_encoders[7].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 104))
        
        #top row buttons
        self.buttons.append([])
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 65))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 66))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 67))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 68))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 69))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 70))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 71))
        self.buttons[0].append(ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, 72))

        #bottom row buttons
        self.buttons.append([])
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 73))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 74))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 75))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 76))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 77))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 78))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 79))
        self.buttons[1].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 80))

        #bottom buttons
        self.buttons.append([])
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 105))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 106))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 107))
        self.buttons[2].append(ButtonElement(True, MIDI_CC_TYPE, MIDI_CHANNEL, 108))
    
        #first encoder group
        self.encoders.append([])
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 1))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 2))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 3))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 4))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 5))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 6))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 7))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 8))

        #second encoder group
        self.encoders.append([])
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 9))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 10))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 11))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 12))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 13))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 14))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 15))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 16))
        
        #third encoder group
        self.encoders.append([])
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 17))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 18))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 19))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 20))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 21))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 22))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 23))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 24))

        #fourth encoder group
        self.encoders.append([])
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 17))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 18))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 19))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 20))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 21))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 22))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 23))
        self.encoders[0].append(EncoderElement(MIDI_CC_TYPE, MIDI_CHANNEL, 24))

        ##ENCODER BUTTONS##
        #group one
        self.encoder_buttons.append([])
        self.encoder_buttons[0].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,33))
        self.encoder_buttons[0].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,34))
        self.encoder_buttons[0].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,35))
        self.encoder_buttons[0].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,36))
        self.encoder_buttons[0].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,37))
        self.encoder_buttons[0].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,38))
        self.encoder_buttons[0].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,39))
        self.encoder_buttons[0].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,40))

        #group two
        self.encoder_buttons.append([])
        self.encoder_buttons[1].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,41))
        self.encoder_buttons[1].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,42))
        self.encoder_buttons[1].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,43))
        self.encoder_buttons[1].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,44))
        self.encoder_buttons[1].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,45))
        self.encoder_buttons[1].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,46))
        self.encoder_buttons[1].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,47))
        self.encoder_buttons[1].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,48))

        #group three
        self.encoder_buttons.append([])
        self.encoder_buttons[2].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,49))
        self.encoder_buttons[2].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,50))
        self.encoder_buttons[2].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,51))
        self.encoder_buttons[2].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,52))
        self.encoder_buttons[2].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,53))
        self.encoder_buttons[2].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,54))
        self.encoder_buttons[2].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,55))
        self.encoder_buttons[2].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,56))

        #group three
        self.encoder_buttons.append([])
        self.encoder_buttons[3].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,57))
        self.encoder_buttons[3].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,58))
        self.encoder_buttons[3].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,59))
        self.encoder_buttons[3].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,60))
        self.encoder_buttons[3].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,61))
        self.encoder_buttons[3].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,62))
        self.encoder_buttons[3].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,63))
        self.encoder_buttons[3].append(ButtonElement(MIDI_CC_TYPE,MIDI_CHANNEL,64))

        def get_encoder_group(self,group):
            #this returns a list of encoderelements
            return self.encoder_groups[group -1]
        
        def get_encoders(self):
            #this returns a list of faderelements
            return self.main_encoders
        
        def get_buttons(self):
            #this returns a list of lists of button elements
            return self.buttons
        
        def get_encoder_buttons(self):
            #this returns a list of lists of button elements
            return self.encoder_buttons

        def get_midi_channel(self):
            #this returns the MIDI channel for the BCR2000
            return MIDI_CHANNEL
