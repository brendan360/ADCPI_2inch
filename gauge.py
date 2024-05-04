#!/usr/bin/python3
######
#IMPORTS
######
from __future__ import absolute_import, division, print_function, unicode_literals
import time
import os


######
# SET UPS
######

######setting up adc board
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
#Analogue input,Display Name,value,warninglow,alertlow,warninghigh,alerthigh,rangelow,rangehigh,measurment,alertcount    "°C"
gaugeItems={
  "FUEL_PRESSURE":["1","Fuel Pres.", 0, 10,15,99,110,0,150,"Kpa", 0],
  "BOOST":["2","Fuel Pres.", 0, 10,15,99,110,0,150,"psi", 0],
  "BLOCK_TEMP":["3","Fuel Pres.", 0, 10,15,99,110,0,150,"°C", 0],
  "COOLANT_PRESSURE":["4","Fuel Pres.", 0, 10,15,99,110,0,150,"Kpa", 0],
  "COOLANT_TEMP":["5","Fuel Pres.", 0, 10,15,99,110,0,150,"°C", 0],
  "OIL_PRESSURE":["6","Fuel Pres.", 0, 10,15,99,110,0,150,"Kpa", 0],
  "OIL_TEMP":["7","Fuel Pres.", 0, 10,15,99,110,0,150,"°C", 0],
  "WIDEBAND02":["8","Fuel Pres.", 0, 10,15,99,110,0,150,"A/F", 0]
}

######
#
######


######
#
######


  

######
# MAIN
######
  
print(adc.read_voltage(1))
print(gaugeItems["FUEL_PRESSURE"][0])
