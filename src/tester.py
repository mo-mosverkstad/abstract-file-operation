def tester(c):
    c = int(c)
    return (c >> 4) | (c << 4 & 0b11110000)
