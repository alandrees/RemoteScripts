import Live
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import *

class BSliderElement(EncoderElement):
    ' Class representing a slider on the controller '


    def __init__(self, msg_type, channel, identifier):
        assert (msg_type is not MIDI_NOTE_TYPE)
        EncoderElement.__init__(self, msg_type, channel, identifier,Live.MidiMap.MapMode.absolute)
