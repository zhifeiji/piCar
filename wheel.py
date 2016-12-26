#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


__author__ = "hdq"
__date__ = "$2016-12-26 13:08:15$"
#import RPi.GPIO as GPIO

class Wheel:
    in1 = ''#引脚编号
    in2 = ''#引脚编号
    ena = ''#使能引脚
    
    pin1 = False #IN1的值
    pin2 = True #IN2的值
    
    #构造函数
    def __init__(self,in1,in2,ena):
        self.in1 = in1
        self.in2 = in2
        self.ena = ena
        self.init_pin()
    
    #初始化引脚
    def init_pin(self):
        print "init_pin"
        #GPIO.setup(self.ena,GPIO.OUT)
        #GPIO.setup(self.in1,GPIO.OUT)
        #GPIO.setup(self.in2,GPIO.OUT)
        #GPIO.output(self.ena,True)
        print "set ena:",self.ena," OUT"
        print "set pin1:",self.in1," OUT"
        print "set pin2:",self.in2," OUT"
        print "set ena:",self.ena," True"
    
    #制动
    def stop(self):
        print "stop"
        self.pin1 = False
        self.pin2 = False
        self.setpin()
    
    #前进
    def forward(self):
        print "forword"
        self.pin1 = False
        self.pin2 = True
        self.setpin()
        
    #后退
    def backoff(self):
        print "backoff"
        self.pin1 = True
        self.pin2 = False
        self.setpin()
    
    #给引脚赋值
    def setpin(self):
        #GPIO.output(self.in1,self.pin1)
        #GPIO.output(self.in2,self.pin2)
        print "set ",self.in1," ",self.pin1
        print "set ",self.in2," ",self.pin2

if __name__ == "__main__":
    print "wheel"
