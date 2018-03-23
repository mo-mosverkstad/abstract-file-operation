from file_mgmt import *

def base_bitwise_cypher(text,key,method,file=None):
    if file != None:
        lines= readfile(file)
    else:
        lines = text
