#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# -*- coding: utf-8 -*-
__author__ = "hdq"
__date__ = "$2016-12-26 12:45:46$"

from move import Move
import sys 

reload(sys)  
sys.setdefaultencoding('utf8')  

if __name__ == "__main__":
    print "Hello World"
    print "************init************"
    move = Move()
    print "************stop************"
    move.stop()
    print "************forward************"
    move.forward()
    print "************backoff************"
    move.backoff()
    print "************turn_left************"
    move.turn_left()
    print "************turn_right************"
    move.turn_right()
