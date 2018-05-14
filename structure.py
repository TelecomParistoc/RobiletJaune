# -*- coding: utf-8 -*-
import init_and_LED
from robot import Robot		#robot is an installed package
import motordriver
from AX12 import AX12
import gpio

from time import sleep
from threading import Thread
import math



############################# PARAMETERS #######################################

ROBOT_WIDTH                 = 250       # mm

LOW_TORQUE                  = 10       # in range [0, 100]

# IMPORTANT: functions in gpio bcm numbers (except gpio_index_of_wpi_pin!)

#converts the wPi pin number to the BCM pin number
#see the output of "gpio readall" on a raspi


jack_pin_bcm = gpio.gpio_index_of_wpi_pin               (10)
gpio.set_pin_mode(jack_pin_bcm, gpio.INPUT)
#gpio.OUTPUT -> easier to test with hand (gpio write 5 0 ou 1)
# ie we don't test with the real jack, we just simulate it
#with the real jack, it must be gpio.INPUT )

##################     PIN INITIALIZATION           ############################

pump_pin_bcm          = gpio.gpio_index_of_wpi_pin    (1)
gpio.set_pull_up_down(  pump_pin_bcm,           gpio.PULL_UP)
gpio.set_pin_mode(      pump_pin_bcm,           gpio.OUTPUT)

front_sensors_pin_list_bcm = list(map(gpio.gpio_index_of_wpi_pin,   [3, 4]))
rear_sensors_pin_list_bcm = [] #list(map(gpio.gpio_index_of_wpi_pin,    [2, 0]))

for pin in front_sensors_pin_list_bcm + rear_sensors_pin_list_bcm:
    gpio.set_pull_up_down(pin, gpio.PULL_DOWN)
    gpio.set_pin_mode(pin, gpio.INPUT)

##################     CONSTRUCTION OF THE ROBOT    ############################

#contains the (name, id) of the used AX12
AX12_list = [("atom_pusher", 129)]

robot = Robot()
for name, id in AX12_list:
    robot.add_object(AX12(id), name)

###################     ACTION FUNCTIONS    ####################################


def grobot_time_elapsed():
    '''
    called when the time is over to stop Grobot from moving
    '''
    print "switching AX12 off..."
    for name, _ in AX12_list:
        getattr(robot, name).turn(0)
	getattr(robot, name).set_torque(0)
    gpio.digital_write(pump_pin_bcm, 0)
    robot.emergency_stop()

def is_obstacle_forwards():
    for sensor in front_sensors_pin_list_bcm:
        if gpio.digital_read(sensor) == 1:
            return True
    return False

def is_obstacle_backwards():
    for sensor in rear_sensors_pin_list_bcm:
        if gpio.digital_read(sensor) == 1:
            return True
    return False

def pump(duration=2.):
    #duration is in seconds
    print("Pump start")
    #we don't use pwm
    gpio.digital_write(pump_pin_bcm, 1)
    sleep(duration)
    gpio.digital_write(pump_pin_bcm, 0)
    print("pump stop")

def push_atom(active = True):
    if(active):
        robot.atom_pusher.move(100)
    else:
        robot.atom_pusher.move(50)
