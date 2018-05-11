from sys import stdout
import os

def help():
    f = open('info.inf', 'r')
    reading = f.readlines()
    f.close()
    counter = 0
    for i in reading:
        counter += 1
        print(i.strip())
        if counter > 27:
            input('--Press return for more--')
            os.system('CLS')
            counter = 0
help()