#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "hdq"
__date__ = "$2016-12-26 12:53:26$"

from wheel import Wheel

class Move:
    left_pin1 = 12
    left_pin2 = 11
    right_pin1 = 15
    right_pin2 = 13
    ena_pin = 40
    
    left_wheel=None
    right_wheel=None
    
    def __init__(self):
        self.left_wheel = Wheel(self.left_pin1,self.left_pin2,self.ena_pin)
        self.right_wheel = Wheel(self.right_pin1,self.right_pin2,self.ena_pin)
        
    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()
        
    def forward(self):
        self.left_wheel.forward()
        self.right_wheel.forward()
        
    def backoff(self):
        self.left_wheel.backoff()
        self.right_wheel.backoff()

    def turn_left(self):
        self.left_wheel.stop()
        self.right_wheel.forward()
        
    def turn_right(self):
        self.left_wheel.forward()
        self.right_wheel.stop()


if __name__ == "__main__":
    print "move func"
