# RobiletJaune motors config

from motordriver import *

# Coding wheels
set_coding_wheel_left_orientation(1)
set_coding_wheel_right_orientation(0)

set_wheels_gap(202)

#PID
print "Linear coeffs:"
set_linear_P(800)
print "P: ", get_linear_P()
set_linear_I(200)
print "I: ", get_linear_I()
set_linear_D(1000)
print "D: ", get_linear_D()
print "Angular coeffs:"
set_angular_P(100)
print "P: ", get_angular_P()
set_angular_I(5)
print "I: ", get_angular_I()
set_angular_D(7000)
print "D: ", get_angular_D()

#Speed
set_linear_cruise_speed(30)
print "Linear cruise speed :", get_linear_cruise_speed()
set_linear_max_acceleration(30)
print "Linear max acceleration :", get_linear_max_acceleration()
set_angular_cruise_speed(200)
print "Angular cruise speed :", get_angular_cruise_speed()
set_angular_max_acceleration(200)
print "Angular max acceleration :", get_angular_max_acceleration()

write_motors_flash()
