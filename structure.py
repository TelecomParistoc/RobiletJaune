# -*- coding: utf-8 -*-
from robot import Robot		#robot is an installed package
import motordriver
from AX12 import AX12
import gpio

from time import sleep
from threading import Thread
import math



############################# PARAMETERS #######################################

ROBOT_WIDTH                 = 305       # mm

LOW_TORQUE                  = 10       # in range [0, 100]

# IMPORTANT: functions in gpio bcm numbers (except gpio_index_of_wpi_pin!)

#converts the wPi pin number to the BCM pin number
#see the output of "gpio readall" on a raspi



#gpio.OUTPUT -> easier to test with hand (gpio write 5 0 ou 1)
# ie we don't test with the real jack, we just simulate it
#with the real jack, it must be gpio.INPUT )


##################     CONSTRUCTION OF THE ROBOT    ############################

#contains the (name, id) of the used AX12
AX12_list = []

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
    gpio.digital_write(shaker_pin_bcm, 0)
    robot.emergency_stop()

