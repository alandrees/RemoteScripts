# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-


def debug_print(message):
    ' Special function for debug output '
    print message


if isinstance(__builtins__, dict):
    __builtins__['debug_print'] = debug_print
else:
    setattr(__builtins__, 'debug_print', debug_print)

def create_instance(c_instance):
    """ Dummy function, this is needed so that the framework
      is recognised as a module
  """
    return 0



# local variables:
# tab-width: 4
