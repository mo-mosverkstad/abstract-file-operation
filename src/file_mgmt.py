def readfile(file,sysFile = False):
    ext = '.py' if sysFile else '.txt'
    f = open(file+ext,'r')
    lines = f.readlines()
    f.close()
    result = list()
    for line in lines:
        result.append(line.strip())
    return result

def writefile(file,txt,sysfile = False):
    ext = '.py' if sysfile else '.txt'
    f = open(f'{file}{ext}','w')
    for line in txt:
        f.write(line+'\n')
    f.close()
