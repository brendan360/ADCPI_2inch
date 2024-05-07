#!/usr/bin/python3
######
#IMPORTS
######
from __future__ import absolute_import, division, print_function, unicode_literals
import time
import os
import math

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
 
gaugeItems={
#   NAME,          value, display name warninglow,alertlow,warninghigh,alerthigh,rangelow,rangehigh,measurment,alertcount 
  "FUEL_PRESSURE":["1","Fuel Pres.", 0, 10,15,99,110,0,150,"Kpa", 0],               #
  "BOOST":["2","Fuel Pres.", 0, 10,15,99,110,0,150,"psi", 0],                       #
  "BLOCK_TEMP":["3","Fuel Pres.", 0, 10,15,99,110,0,150,"°C", 0],
  "COOLANT_PRESSURE":["4","Fuel Pres.", 0, 10,15,99,110,0,150,"Kpa", 0],            #
  "COOLANT_TEMP":["5","Fuel Pres.", 0, 10,15,99,110,0,150,"°C", 0],
  "OIL_PRESSURE":["6","Fuel Pres.", 0, 10,15,99,110,0,150,"Kpa", 0],                #
  "OIL_TEMP":["7","Fuel Pres.", 0, 10,15,99,110,0,150,"°C", 0],
  "WIDEBAND02":["8","Fuel Pres.", 0, 10,15,99,110,0,150,"A/F", 0]
}

######
# Sensor Constants
######
CONST_fuel_minVoltage =.5
CONST_fuel_maxVoltage =4.5
CONST_fuel_minPressure =0
CONST_fuel_maxPressure =1000

CONST_coolant_minVoltage =.5
CONST_coolant_maxVoltage =4.5
CONST_coolant_minPressure =0
CONST_coolant_maxPressure =1000

CONST_oil_minVoltage =.5
CONST_oil_maxVoltage =4.5
CONST_oil_minPressure =0
CONST_oil_maxPressure =1000

CONST_boost_minVoltage =.4
CONST_boost_maxVoltage =4.65
CONST_boost_minPressure =20
CONST_boost_maxPressure =300

CONST_blockTemp_balanceResistor = 1000.0
CONST_blockTemp_beta = 3446
CONST_blockTemproomTemp = 293.15  #in K)
CONST_blockTempresistorRoomTemp = 2480.0  

CONST_coolantTemp_balanceResistor = 1000.0
CONST_coolantTemp_beta = 3446
CONST_coolantTemproomTemp = 293.15
CONST_coolantTempresistorRoomTemp = 2480.0

CONST_oilTemp_balanceResistor = 10000.0
CONST_oilTemp_beta = 3446
CONST_oilTemproomTemp = 293.15
CONST_oilTempresistorRoomTemp = 2480.0

CONST_AFR_minVoltage=.68
CONST_AFT_maxVoltage=1.36

######
#Calculator functions
######
def FUNCT_fuel_pres():
    voltage=adc.read_voltage(int(gaugeItems["FUEL_PRESSURE"][0]))
    gaugeItems["FUEL_PRESSURE"][2]= (voltage - CONST_fuel_minVoltage)/(CONST_fuel_maxVoltage -CONST_fuel_minVoltage)*(CONST_fuel_maxPressure- CONST_fuel_minPressure) + CONST_fuel_minPressure
    print(gaugeItems["FUEL_PRESSURE"][2])

def FUNCT_coolant_pres():
    voltage=adc.read_voltage(int(gaugeItems["COOLANT_PRESSURE"][0]))
    gaugeItems["COOLANT_PRESSURE"][2]= (voltage - CONST_coolant_minVoltage)/(CONST_coolant_maxVoltage -CONST_coolant_minVoltage)*(CONST_coolant_maxPressure- CONST_coolant_minPressure) + CONST_coolant_minPressure
    print(gaugeItems["COOLANT_PRESSURE"][2])
            
def FUNCT_oil_pres():
    voltage=adc.read_voltage(int(gaugeItems["OIL_PRESSURE"][0]))
    gaugeItems["OIL_PRESSURE"][2]= (voltage - CONST_oil_minVoltage)/(CONST_oil_maxVoltage -CONST_oil_minVoltage)*(CONST_oil_maxPressure- CONST_oil_minPressure) + CONST_oil_minPressure
    print(gaugeItems["OIL_PRESSURE"][2])

def FUNCT_boost_pres():
    voltage=adc.read_voltage(int(gaugeItems["BOOST"][0]))
    boostKpa= (voltage - CONST_boost_minVoltage)/(CONST_boost_maxVoltage -CONST_boost_minVoltage)*(CONST_boost_maxPressure- CONST_boost_minPressure) + CONST_boost_minPressure
    gaugeItems["BOOST"][2]=((boostKpa-100.3)*0.145038)
    print(gaugeItems["BOOST"][2])

def FUNCT_block_temp():
    voltage=adc.read_voltage(int(gaugeItems["BLOCK_TEMP"][0]))
    voltage=CONST_blockTemp_balanceResistor/voltage
    steinhart = voltage /CONST_blockTempresistorRoomTemp 
    steinhart = math.log(steinhart) 
    steinhart /=CONST_blockTemp_beta
    steinhart += 1.0 / (20 + 273.15)
    steinhart = 1.0 / steinhart
    steinhart -= 273.15
    print(steinhart)

######
# MAIN
######
while True:
   FUNCT_block_temp()
   FUNCT_boost_pres()
   time.sleep(.5)

      
#FUNCT_fuel_pres()
#FUNCT_coolant_pres()
#FUNCT_oil_pres()



