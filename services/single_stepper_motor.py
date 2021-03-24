"""
____________________________________________________
Author: Supuni Kaveendya
Date: 01/03/2021
Version : 1.0
Name: Stepper motor controller
Properties: Rotate stepper motor in any direction to specific angle
_______________________________________________________
"""

import sys
from time import sleep

import RPi.GPIO as GPIO


class TurnOneWheel:
    def __init__(self, motor_channel):
        # assign GPIO pins for motor
        self.motor_channel = motor_channel
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        # for defining more than 1 GPIO channel as input/output use
        GPIO.setup(self.motor_channel, GPIO.OUT)
        self.current_angle = 0
        self.current_direction = ''

    def spin_one_period_clockwise(self, t):
        # speed should be in between 1-100
        # this function will spin a motor in clockwise
        GPIO.output(self.motor_channel, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
        sleep(t)
        GPIO.output(self.motor_channel, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
        sleep(t)
        GPIO.output(self.motor_channel, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
        sleep(t)
        GPIO.output(self.motor_channel, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
        sleep(t)

    def spin_one_period_anticlockwise(self, t):
        # speed should be in between 1-100
        # this function will spin a motor in anti-clockwise
        GPIO.output(self.motor_channel, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
        sleep(t)
        GPIO.output(self.motor_channel, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
        sleep(t)
        GPIO.output(self.motor_channel, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
        sleep(t)
        GPIO.output(self.motor_channel, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
        sleep(t)

    def moveSteps(self, motor_direction, speed, angle):

        t = 1 / speed
        t = round(t, 2)

        step_value = 1.8
        steps = angle / step_value
        self.current_direction = motor_direction

        for i in range(steps):
            if motor_direction == 'c':
                print('motor running clockwise\n')
                self.spin_one_period_clockwise(t=t)
            else:
                print('motor running anti-clockwise\n')
                self.spin_one_period_anticlockwise(t=t)
            self.current_angle = i * step_value

    def runner(self, motor_direction, speed, angle):
        # motor direction should be "a" for anticlockwise and "c" for clockwise
        # speed should be in between 1-100
        # this function is to control motor in both ways
        if motor_direction == 'c' or motor_direction == 'a':
            self.moveSteps(motor_direction=motor_direction, speed=speed, angle=angle)
        else:
            print('motor stopped')
            sys.exit(0)
