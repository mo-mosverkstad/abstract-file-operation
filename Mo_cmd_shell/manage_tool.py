from time import sleep
import os, datetime

TOOL_CKDISK = 'chkdsk'
TOOL_CLEARSCREEN = 'cls'
TOOL_VERSION = 'version'
TOOL_DATE = 'date'
TOOL_DIR = 'dir'
TOOL_CD = 'cd'
CHOICE = 'choice'



def tool_checkdisk(status, inputs_item_list):
    print('0% checked')
    for i in range(20,120,20):
        sleep(5)
        print(f'{i}% checked of the disk')
    return status


def choice():
    i = input('[Y/N]?')
    del i

def tool_clearscreen():
    os.system('cls')
 
def tool_version():
    print('Microsoft Windows [version 10.0.16299.309]')
    print('(c) 2017 Microsoft Corporation. all rights reserved.')
    print('')

def tool_date():
    print('Current date: ' + str(datetime.datetime.now()))

def dir(status, inputs):
    DIRECTORY = 1
    TEXTFILE = 2
    MODE_DIRECTORY = 'd-----   '
    MODE_ROOT_DIRECTORY = 'd-r---'
    MODE_TEXTFILE = '-a----   '
    print('')
    print(f'     Folder: {status}')
    print('')
    the_list = os.listdir(status)
    print('Mode  ' + '   ' + 'Name')
    for item_name in the_list:
        content = item_name.split('.')
        if len(content) == DIRECTORY:
            mode = MODE_DIRECTORY
        elif len(content) == TEXTFILE:
            mode = MODE_TEXTFILE
        print(mode+'   '+item_name)
    return status

def changedirector(status,inputs):
    status1 = status
    for item in inputs[0].split('\\'):
        if item == '..':
            status1 = '\\'.join(status1.split('\\')[:-1])
        else:
            status1 = status1 + '\\' + item

    try:
        a = os.listdir(status1)
        return status1
    except:
        return status