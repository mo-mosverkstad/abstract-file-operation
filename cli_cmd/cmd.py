from time import sleep
import os, datetime

CKDISK = 'chkdsk'
CHOICE = 'choice'
CLEARSCREEN = 'cls'
CMD = 'cmd'
DATE = 'date'

def checkdisk():
    print('0% checked')
    for i in range(20,120,20):
        sleep(5)
        print(f'{i}% checked of the disk')


def choice():
    i = input('[Y/N]?')
    del i

def clearscreen():
    os.system('cls')
 
def licensecommand():
    print('Microsoft Windows [version 10.0.16299.309]')
    print('(c) 2017 Microsoft Corporation. all rights reserved.')
    print('')

def date():
    print('Current date: ' + str(datetime.datetime.now()))
