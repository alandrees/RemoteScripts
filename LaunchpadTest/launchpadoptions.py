import Live
#from _AbletonPlus.Options import Options
from launchpadmode import Modes

MODE_XY = 1
MODE_DRUM = 2

options = {
    'abletonplus' : {'master':True,'callbacks':[{},{},{}]},
    'constrain':True,
    'hold':True,
    'width':8,
    'height':8,
    'defaultgridmode':MODE_XY,
    'disabledmodes': 2+4+8+16,
    'highlightfollowslaunch':False,
    'defaultmode': Modes.SESSION_MODE
    }


"""
Note: not all options are implemented yet, infact this is last on my todo list (well some of them... some are easy to implement)

master:
AbletonPlus definition as to if the control surface is defined as a master.

constrain:
will the highlight box be constrained to the scene/track dimensions
already established in the software (True) or can it go out to the maximum (outside the grid less one track/scene)

hold:
this should be true until I can figure out a way to make the launch on release (so you can hold the button down
and launch for timing purposes)

width:
define the width of the highlight, in tracks

height:
define the height of the highlight, in scenes

defaultgridmode:
a value of 1 will set up the controller to use the x-y layout on startup, otherwise it will use the drum layout

disabledmodes:
-1 - no modes disabled
 0 - init mode
 1 - session mode
 2 - user mode 1
 4 - user mode 2
 8 - mixer mode
 16 - options mode
 
 add them together to disable multiple modes
 
 highlightfollowslaunch:
 if this is set to True, when you launch a clip in session mode, that track will be highlighted
 """
