import os, sys
import shutil
from msvcrt import getch

DELETE = 'del'
DELETE_SUBTREE = 'deltree'
EDIT = 'edit'

def editor(place, file):
    txtlines = readfile(place+'\\'+file)
    new = []
    n = 0
    for txt in txtlines:
        new.append(__edit(txt.strip(),n))
        n+=1
    writefile(place+'\\'+file,new)
    return place

def __edit(txt, i):
    DEL = '\\x08'
    RET = '\\r'
    END = '\\x1b'
    line = txt
    while True:
        print(str(i) + ' -> ' +line)
        key = str(getch())[2:-1]
        if key == DEL:
            line = line[:-1]
        elif key in [END, RET]:
            break
        else:
            line = line + key
        os.system('cls')
    return line + '\n'


def readfile(file):
    f = open(file,'r')
    lines = f.readlines()
    result = list()
    for line in lines:
        result.append(line)
    f.close()
    return result

def writefile(file,txt):
    f = open(f'{file}','w')
    for line in txt:
        f.write(line)
    f.close()

def copy_cmd(inputs):
    file = inputs[4:].split('to')
    if len(file) != 2:
        print('Copy failed')
    else:
        copy(file[0].strip(),file[1].strip())

def copy(org, new):
    file = readfile(org)
    writefile(new,file)

def delete(where, what):
    os.remove(f'{where}\\{what}')

def delete_subtree(place,folder):
    shutil.rmtree(place + '\\' + folder, ignore_errors=True)

def new(where, what):
    f = open(where+'\\'+what, 'w')
    f.write('')
    f.close()



#copy C:\\hp\\new.txt to C:\\hp\\BIN\\new.txt
#file = 'C:\\Users\\hp\\Desktop\\Mos temp pärm\myfile.txt'
#editor(file)