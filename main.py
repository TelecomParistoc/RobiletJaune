#!/usr/bin/env python
import motion                           
#from libmotors
from starting_block import add_jack_and_delay, time_elapsed, manage_time_elapsed
# the robot is "constructed" in structure.py
from structure import *

from time import sleep

STARTING_POINT = None #set in init_color()
STARTING_HEADING = None

PATH_DIR="/home/pi/RobiletJaune/paths"

########################  JACK MANAGEMENT ####################

# delay = 10 = maximum time the robot waits before aborting
#manage_jack = add_jack_and_delay(robot, 6666)

#init_and_LED.turn_orange_on()
#gpio.assign_callback_on_gpio_down(jack_pin_bcm, lambda: (manage_jack(False),
#                                                init_and_LED.turn_green_on()))
#gpio.assign_callback_on_gpio_up(jack_pin_bcm, lambda: manage_jack(True))

#robot.wait_sequence() # We wait for jack beeing pushed/pulled

############################ TOP LEVEL ACTION DEFINITION #######################
# remainder: definition != execution

robot.start_collision_detection(is_obstacle_forwards, is_obstacle_backwards)

def log(message):
    print message

#robot.moveTo(1000,0,-1)

robot.setPosition(203, 1600)
robot.set_heading(0)

'''robot.add_sequence("main sequence")
robot.add_parallel(robot.moveTo, [1000, 0, -1])
robot.wait()
robot.sequence_done()

robot.start_sequence("main sequence")
robot.wait_sequence()
robot.stop()
'''
robot.color="green"


robot.add_sequence("main_sequence")
robot.load_add_path(PATH_DIR + "/activate_experience.json", False)
robot.add_parallel(pump, [1], False)
robot.wait()
robot.sequence_done()

robot.start_sequence("main_sequence")
robot.wait_sequence()
robot.stop()
