#!/usr/bin/env python
import init_and_LED

import motion                           #from libmotors
from starting_block import add_jack_and_delay, time_elapsed, manage_time_elapsed
# the robot is "constructed" in structure_Grobot.py
from structure import *

from time import sleep

STARTING_POINT = None #set in init_color()
STARTING_HEADING = None


############################ TOP LEVEL ACTION DEFINITION #######################
# remainder: definition != execution

def log(message):
    print message


robot.add_sequence("main_sequence")
robot.add_parallel(robot.move, [1000])
robot.wait()
robot.add_parallel(robot.move, [-1000])   
robot.wait()
robot.sequence_done()

robot.start_sequence("main_sequence")
robot.wait_sequence()
robot.stop() 
