#!/usr/bin/env python
from msvcrt import getch
import sys
sys.path.insert(0, 'C:\\Users\\hp\\Desktop\\Mostemppärm\\temp\\libs')
from libscore import *
sys.path.insert(0, 'C:\\Users\\hp\\Desktop\\Mostemppärm\\temp\\scc')
from wrapper import scc_wrapper


flag = True
status = 'password'
status_dict = {'password'         : sys_password, 
               'home'             : home_page, 
               'cypher_abstracted': scc_wrapper,
               'help'             : system_help}
               
while flag:
    flag, status = status_dict[status]()