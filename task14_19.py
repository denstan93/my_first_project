def task14_19(x):
    z = 0
    m = 0
    if x % 2 == 0:
        while z < x/2:
            print(('*'+' ')*x)
            print((' '+'*')*x)
            z += 1
    else:
        while m <= int(x/2):
            while m <= int(x / 2):
                print(('*' + ' ') * x)
                break
            while m < int(x / 2):
                print((' ' + '*') * x)
                break
            m += 1
print(task14_19(4))