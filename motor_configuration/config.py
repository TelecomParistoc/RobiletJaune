# RobiletJaune motors config

from motordriver import *

# Coding wheels
set_coding_wheel_left_orientation(1)
set_coding_wheel_right_orientation(0)

#PID
print "Linear coeffs:"
print "P: ", get_linear_P()
#set_linear_I(0)
print "I: ", get_linear_I()
#set_linear_D(0)
print "D: ", get_linear_D()
print "Angular coeffs:"
print "P: ", get_angular_P()
#set_angular_I(0)
print "I: ", get_angular_I()
#set_angular_D(0)
print "D: ", get_angular_D()

#Speed
#set_linear_cruise_speed(100)
print "Linear cruise speed :", get_linear_cruise_speed()
#set_linear_max_acceleration(100)
print "Linear max acceleration :", get_linear_max_acceleration()
print "Angular cruise speed :", get_angular_cruise_speed()
print "Angular max acceleration :", get_angular_max_acceleration()

