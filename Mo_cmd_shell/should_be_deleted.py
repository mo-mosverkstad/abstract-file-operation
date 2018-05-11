import os, sys
from help_print import help

from manage_tool import *
from manage_file import *

SHELL_EXIT = "exit"
def shell_exit(status, inputs_item_list):
    sys.exit()
    return status

cmd_map = {SHELL_EXIT: shell_exit,
           TOOL_CKDISK: tool_checkdisk,
           EDIT: editor,
           TOOL_DIR:dir,
           TOOL_CD:changedirector}

def split_inputs(inputs):
    DELIMITOR_SPACE = ' '
    inputs_item_list = list()
    for item in inputs.split(DELIMITOR_SPACE):
        if len(item) > 0: inputs_item_list.append(item)
    return inputs_item_list

def show_invalid_cmd(status, inputs_item_list):
    print("Invalid command")
    return status

def mo_cmd_shell():
    PROMPT = '>'
    DELIMITOR = '\\'
    status = 'C:' + DELIMITOR
    while True:
        inputs = input(status + PROMPT)
        #inputs_item_list = [item for item in inputs.split(DELIMITOR_SPACE) if len(item) > 0]
        inputs_item_list = split_inputs(inputs)
        cmd_func = cmd_map.get(inputs_item_list[0], show_invalid_cmd)
        status = cmd_func(status, inputs_item_list[1:])



            
mo_cmd_shell()