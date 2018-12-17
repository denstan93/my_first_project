def task14_25(z):
    #z = int(x/2)
    i = 1
    x = 1
    print(' '*(z+1)+'*')
    while i <= z:
        i+=2
        print(' '*z+'*'*i)
        z-=x
        x+=1
        if z <= 0:
            break
        if z == 2:
            break
"""    while i >= 0:
        i-=2
        z+=2
        print(' '*z+'*'*i+' '*z)
"""

print(task14_25(9))