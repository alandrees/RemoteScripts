import Live

from _Framework.ButtonElement import *
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from launchpadbuttoncomponent import LaunchpadButtonComponent

#mode identifiers
MODE_XY = 1
MODE_DRUM = 2 

class LaunchpadButtonMatrix():
    
    def __init__(self, w, h,hold,mode):
        #ButtonMatrixElement.__init__(self)
        self._matrix = ButtonMatrixElement()
        self._matrix.name = 'Launchpad_Main_Grid'
        self._width = w
        self._height = h
        self._hold = hold
        self.setup_button_arrays()
        self.set_grid_mapping_mode(mode)
    
    def setup_button_arrays(self):
        self._xy_button_array = []
        for row in range(self._height):
            button_row = []
            for column in range(self._width + 1):
                button = LaunchpadButtonComponent(self._hold, MIDI_NOTE_TYPE, 0, column + (row * 16))
                button.name = str(column) + ',' + str(row) + '_Button'
                button_row.append(button)
            self._xy_button_array.append(button_row)
        
        self._xy_button_array_v = []
        for column in range(self._width + 1):
            button_column = []
            for row in range(self._height):
                button = LaunchpadButtonComponent(self._hold, MIDI_NOTE_TYPE, 0, column + (row * 16))
                button.name = str(column) + ',' + str(row) + '_Button'
                button_column.append(button)
            self._xy_button_array_v.append(button_column)
            

        self._drum_button_array = []
        for row in range(self._height):
            button_row = []
            for column in range(self._width):
                if(column >= 0 and column <= 3):
                    button = LaunchpadButtonComponent(self._hold, MIDI_NOTE_TYPE, 0, (64 - (row * 4)) + column )
                    button.name = str(column) + ',' + str(row) + '_Button'
                elif(column >= 4):
                    button = LaunchpadButtonComponent(self._hold, MIDI_NOTE_TYPE, 0, (96 - (row * 4)) + (column - 4) )
                    button.name = str(column) + ',' + str(row) + '_Button'
                button_row.append(button)
            self._drum_button_array.append(button_row)
        for row in range(self._height):
            button_row = self._drum_button_array[row]
            button = LaunchpadButtonComponent(self._hold, MIDI_NOTE_TYPE, 0, row + 100)
            button.name = str(column) + ',' + str(row) + '_Button'
            button_row.append(button)
    
    def get_active_mapping_array(self):
        if(self.get_active_mapping_mode() == MODE_XY):
            return self._xy_button_array
        elif(self.get_active_mapping_mode() == MODE_DRUM):
            return self._drum_button_array
    
    def get_active_mapping_mode(self):
        return self._mapping_mode
    
    def set_grid_mapping_mode(self, mode):
        if(mode == 1):
            self._matrix._send_midi((176, 0, 1))
            #put it in the matrix
            self._mapping_mode = mode
        elif(mode == 2):
            self._matrix._send_midi((176,0, 2))
            #put it in the matrix
            self._mapping_mode = mode
        return self._mapping_mode
    
    def get_mapping_mode(self, mode):
        if(mode == 1):
            return self._xy_button_array
        elif(mode == 2):
            return self._drum_button_array
        elif(mode == 3):
            return self._xy_button_array_v