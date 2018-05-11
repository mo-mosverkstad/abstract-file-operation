#!/usr/bin/env python
from msvcrt import getch
import os

password = '1687621156'

def sleep_infintity_seconds():
    while True:
        pass

def sys_password():
    print('Please enter password to go in to Mos system')
    for i in range(3):
        if input('Please enter the password here >>>') == password:
            print('Welcome to Mos system 1.0!')
            print()
            return (True, 'home')
        else:
            print('Please try it again!')
    print('I don\'t let you go in to my system!')
    return (False, '')
 
def home_page():
    print('Press 1 for --Not fixed--')
    print('Press 2 for Abstracted mashine of text cypher')
    print('Press 3 for ...ext.')
    print('Press H for For help')
    print('Press E for For exit this system')
    while True:
        key = getch().decode() # Note: The function getch returns type of byte not string
        if key == '1':
            return (True, 'Graphical_calc')
        elif key == '2':
            return (True, 'cypher_abstracted')
        elif key == 'E':
            return (False, '')
        elif key == 'H':
            return (True, 'help')
        

def system_help():
    print('When you sign into the system you come to the meny.')
    print('Then you follow the instruction on the meny')
    print('1. --Not fixed-- ')
    print('  IMPORTANT: DO NOT PRESS 1, IT WILL CRASH!')
    print('2.SCC 1.1')
    print('SCC is short for simple cypher coding')
    print('This system will make easier to make a new cypher type')
    print('When you get in this system you are in root that prompt will be SCC:>')
    print('You can type exit anywhere for exiting this system')
    print('In root you can type:')
    print('prof: that you can go into profile mode')
    print('edit: you can edit the cypher mode')
    print('enc ...: you encrypt a text')
    print('dec ...: you decrypt a encrypted text')
    print('In profile you can type:')
    print('new:')
    print('  In new you create a new type of a cypher')
    print('  First you will see Please input algorithm type')
    print('  You had to write in algorithm type')
    print('  It have 2 algorithm types: mapping, transposition')
    print('  Then you had to press algorithm name')
    print('edit:')
    print('  important: you can\'t edit a built-in cypher type')
    print('  First you had to answer the system yes or no to edit')
    print('  If you answer yes you had to tell this system witch algorithm name that you want to edit')
    print('  Then you write in the descryption.')
    print('  After that you had to type in how you want to enc or dec')
    print('  You will first generate plainlist and enclist')
    print('  for example:')
    print('    when you use caesar the plainlist is [a,b,c,d,e,f, ....,z] and encList is [c,d,e,f,g, ....,z,a,b] if key is 3')
    print('	   when you use reverse the plainlist is [0,1,2,3,4,5,6,7] and encList is [7,6,5,4,3,2,1,0] if text had 8 chars(bytes if you use UTF-8)')
    print('  Also you had to code this plainlist and encList')
    print('  delete:')
    print('    You had to type delete to delete something')
    key = getch().decode()
    while key != '\r':
        key = getch().decode()
    os.system('cls')
    print('	When you are going to delete system will ask you to be sure to delete right thing')
    print('In edit mode you had to generate plainlist and encList')
    print('It had some varible that called self.key, self.whole_list(only can be used in mapping)')
    print('You use it just like normal coding. Just only very very small difference(varibles and you can\'t define a function)')
    print('If you want to add a newline you just write ; because you don \'t use this symbol in regular coding')
    print('You can get help when you key in "help"')
    return (True, 'home')