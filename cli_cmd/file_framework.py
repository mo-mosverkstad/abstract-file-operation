def is_backward_directory(d):
    c = 0
    all = True
    for i in d.split('\\'):
        if i == '..':
            all = all and True
        else:
            all = all and False
    if all:
        for i in d.split('\\'):
            c += 1
    return (all, c)

def backward_change(d, steps):
    d1 = d.split('\\')
    d1 = d1[:-steps]
    d = '\\'.join(d1)
    return d