import os
import shutil

DELETE = 'del'
DELETE_SUBTREE = 'deltree'

def readfile(file):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    result = list()
    for line in lines:
        result.append(line)
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