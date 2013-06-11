import Live
#from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ButtonElement import ButtonElement
from launchpadbuttoncomponent import LaunchpadButtonComponent
import launchpadmode

from _AbletonPlus2.abletonlog import write_log

MODE_OBJECT = 0
MODE_BUTTONS = 1

PRESS_VALUE = 127
RELEASE_VALUE = 0

class LaunchpadModeSelectorComponent():
    """Controls and manages the mode selection.  Will eventually be implemented as a state machine."""

    def __init__(self, mode = 0):
        """class initialization"""
        #ControlSurfaceComponent.__init__(self)
        self._mode_objects = dict()
        self._mode = 0
        self._buttons_held = []
        self._momentary_modes = []
        return None
    
    def _button_callback(self, value = None, button = None):
        """gets called when a button bound to a mode object gets pressed/released"""
        if(value != None and button != None):
            if(value == PRESS_VALUE):
                self._buttons_held.append(button.message_identifier())
            elif (value == RELEASE_VALUE ):
                self._buttons_held.remove(button.message_identifier())
        self.update_mode()
        return None

    def number_of_modes(self):
        return len(self._mode_objects)
            
    def bind_mode(self, mode_object, button, mode_value, set,toggle = 0):
        """bind a mode using the mode object which inherits the mode object"""
        #check if mode is already added, and has the required member functions
        if(hasattr(mode_object.__class__, "enable") and hasattr(mode_object.__class__, "disable"), hasattr(mode_object.__class__, "activator")):
            self._mode_objects.update({mode_value: [mode_object,(button,)]})
            self.set_mode_buttons(mode_value,self._mode_objects[mode_value][MODE_BUTTONS])
            if mode_object.is_momentary():
                self._momentary_modes.append(mode_object)               
            if(set == mode_value):
                self.set_mode(mode_value)
            return True
        return False
        
    def set_mode(self, mode):
        """set the current mode to mode"""
        if (mode > 0 and self._mode_objects.has_key(mode)):
            if (self._mode != mode and mode != 0):
                if(self._mode != 0):
                    self.get_mode()[MODE_OBJECT].disable(self.get_mode()[MODE_BUTTONS], mode)
                old_mode = self._mode
                self._mode = mode
                self.get_mode()[MODE_OBJECT].enable(self.get_mode()[MODE_BUTTONS], old_mode)
        return True
    
    def get_mode(self):
        """return the currently enabled mode object"""
        return self._mode_objects[self._mode]
        
    def set_mode_buttons(self, mode_value, buttons): #set the buttons to trigger the given mode
        """set the buttons which trigger a mode"""
        if(buttons != None):
            if(isinstance(buttons, tuple)):
                if ((len(buttons) - 1) in range(16)):
                    for button in buttons:
                        if(isinstance(button, ButtonElement)):
                            identify_sender = True
                            button.add_value_listener(self._button_callback, identify_sender)
        return None
        
    
    def destroy_modes(self): #destroys all the modes
        """destroy the modes... used for cleanup"""
        for i in self._mode_objects:
            for button in self._mode_objects[i][MODE_BUTTONS]:
                button.disconnect()
        return True
    
    def update_mode(self):
        """this function does the logic to check if there are any changes to the mode depending on the currently held buttons"""
        if(len(self._buttons_held) > 0 ):
            for key in self._mode_objects.keys():
                if(self._mode_objects[key][MODE_OBJECT].activator() == self._buttons_held):
                    if(key != self._mode):
                        self.set_mode(key)
                        break
        elif (self.get_mode()[MODE_OBJECT].is_momentary()) and (len(self._buttons_held) == 0):
            oldmode = self.get_mode()[MODE_OBJECT].get_old_mode()
            if oldmode != 0:
                self.set_mode(oldmode)
        return True
    
    def update(self):
        return None
