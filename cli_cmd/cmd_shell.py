import os, cmd, file_management
from file_framework import *
from help_print import help

def cmd_shell():
    DIRECTORY = 1
    TEXTFILE = 2
    MODE_DIRECTORY = 'd-----   '
    MODE_ROOT_DIRECTORY = 'd-r---'
    MODE_TEXTFILE = '-a----   '
    listfiles = ['dir', 'ls']
    PROMPT = '>'
    DELIMITOR = '\\'
    INPUTS_HELP = 'help'
    status = 'C:' + DELIMITOR
    while True:
        inputs = input(status + PROMPT)
        if inputs in listfiles:
            the_list = os.listdir(status)
            print('Mode  ' + '   ' + 'Name')
            for item_name in the_list:
                content = item_name.split('.')
                if len(content) == DIRECTORY:
                    mode = MODE_DIRECTORY
                elif len(content) == TEXTFILE:
                    mode = MODE_TEXTFILE
                print(mode+'   '+item_name)
        elif inputs.startswith('cd '):
            directory = inputs[3:]
            all, counter = is_backward_directory(directory)
            if all:
                status = backward_change(status, counter)
            else:
                change_director = False
                try:
                    a = os.listdir(status+DELIMITOR+directory)
                    change_director = True
                except:
                    change_director = False
                if change_director:
                    status = status+DELIMITOR+directory

        elif inputs == INPUTS_HELP:
            help()

        elif inputs == cmd.CKDISK:
            cmd.checkdisk()

        elif inputs == cmd.CHOICE:
            cmd.choice()

        elif inputs == cmd.CLEARSCREEN:
            cmd.clearscreen()

        elif inputs == cmd.CMD:
            cmd.licensecommand()

        elif inputs.startswith('copy'):
            file_management.copy_cmd(inputs)

        elif inputs == cmd.DATE:
            cmd.date()

        elif inputs.startswith(file_management.DELETE_SUBTREE):
            file_management.delete_subtree(status,[item for item in inputs.split(' ') if len(item) > 0][1])

        elif inputs.startswith(file_management.DELETE):
            file_management.delete(status,[item for item in inputs.split(' ') if len(item) > 0][1])


        else:
            if inputs.strip() != '':
                print('CommandError:')
                print(f'  "{inputs}" is not command.')
                print('   Type help for more infomation.')
        '''
        elif inputs.startswith('touch '):
            file = inputs[6:]
            f = open(file, 'w')
        '''





            
cmd_shell()