#!/usr/bin/python3


######
# SET UPS
######
from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals
import time
import os

try:
    from ADCPi import ADCPi
except ImportError:
    print("Failed to import ADCPi from python system path")
    print("Importing from parent folder instead")
    try:
        import sys
        sys.path.append('..')
        from ADCPi import ADCPi
    except ImportError:
        raise ImportError(
            "Failed to import library from parent folder")


adc = ADCPi(0x68, 0x69, 12)


######
# VARIABLES
######



######
#
######
print(adc.read_voltage(1))


######
#
######





######
#
######

