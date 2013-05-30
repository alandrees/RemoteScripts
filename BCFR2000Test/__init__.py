# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-
import Live
from BCFR2000 import BCFR2000

def debug_print(message):
    ' Special function for debug output '
    print message


if isinstance(__builtins__, dict):
    __builtins__['debug_print'] = debug_print
else:
    setattr(__builtins__, 'debug_print', debug_print)

def create_instance(c_instance):
    return BCFR2000(c_instance);
