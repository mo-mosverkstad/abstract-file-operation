from msvcrt import getch
while True:
    key = str(getch())[2:-1]
    print(key)