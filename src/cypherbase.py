from file_mgmt import *

def __base_bitwise_cypher(text,method,key = '',file=None):
    exec(f'from {method} import {method}')
    if file != None:
        lines= readfile(file)
    else:
        lines = text
    result = []
    for line in lines:
        for char in line:
            if key != '':
                key = ','+ str(key)
            new = str(ord(char))
            exec('result.append(chr('+str(method)+'('+str(new)+str(key)+')))')
    result = ''.join(result)
    if file == None:
        return result
    else:
        writefile(f'enc {file}',result.split('\n'))

def base_bitwise_cypher(txt,method,key='',file_or_not = False):
    if file_or_not:
        __base_bitwise_cypher([],method,key,txt)
    else:
        return __base_bitwise_cypher(txt,method,key)


'''
binary_result = base_bitwise_cypher(['aaaaabbbbb'],'tester')
for c in binary_result:
    #print(hex(ord(c)))
    print(c)
'''