import Live
#from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ButtonElement import ButtonElement
from launchpadbuttoncomponent import LaunchpadButtonComponent
import launchpadmode

MODE_OBJECT = 0
MODE_BUTTONS = 1
ON_VALUE = 127
OFF_VALUE = 0
class LaunchpadModeSelectorComponent():

    def __init__(self, mode = 0):
        #initialize the object
        #ControlSurfaceComponent.__init__(self)
        self._mode_objects = dict()
        self._mode = 0
        self._buttons_held = []
        return None
    
    def _button_callback(self, value = None, button = None):
        if(value != None and button != None):
            if(value == ON_VALUE):
                self._buttons_held.append(button.message_identifier())
            elif (value == OFF_VALUE ):
                self._buttons_held.remove(button.message_identifier())                
        self.update_mode()
        return None
        
    def number_of_modes(self):
        return len(self._mode_objects)
            
    def bind_mode(self, mode_object, button, mode_value, set):
        #check if mode is already added... amongst other sanity checks
        if(hasattr(mode_object.__class__, "enable") and hasattr(mode_object.__class__, "disable"), hasattr(mode_object.__class__, "activator")):
            self._mode_objects.update({mode_value: [mode_object,(button,)]})
            self.set_mode_buttons(mode_value,self._mode_objects[mode_value][MODE_BUTTONS])
            if(set == mode_value):
                self.set_mode(mode_value)
            return True
        return False
        
    def set_mode(self, mode):
        if (mode > 0 and self._mode_objects.has_key(mode)):
            if (self._mode != mode and mode != 0):
                    if(self._mode != 0):
                        self.get_mode()[MODE_OBJECT].disable(self.get_mode()[MODE_BUTTONS])
                    self._mode = mode
                    self.get_mode()[MODE_OBJECT].enable(self.get_mode()[MODE_BUTTONS])
        return True
    
    def get_mode(self): #return the currently enabled mode
        return self._mode_objects[self._mode]
        
    def set_mode_buttons(self, mode_value, buttons): #set the buttons to trigger the given mode
        if(buttons != None):
            if(isinstance(buttons, tuple)):
                if ((len(buttons) - 1) in range(16)):
                    for button in buttons:
                        if(isinstance(button, ButtonElement)):
                            identify_sender = True
                            button.add_value_listener(self._button_callback, identify_sender)
        return None
        
    
    def destroy_modes(self): #destroys all the modes
        for i in self._mode_objects:
            for button in self._mode_objects[i][MODE_BUTTONS]:
                button.disconnect()
        return True
    
    def update_mode(self):
        if(len(self._buttons_held) > 0):
            for key in self._mode_objects.keys():
                if(self._mode_objects[key][MODE_OBJECT].activator() == self._buttons_held):
                    if(key != self._mode):
                        self.set_mode(key)
                        break
        return True
    
    def update(self):
        return None