def task14_18(x):
    print ('*'*x)
    z = 0
    while z <= (x-3):
        print('*'+' '*(x-2)+'*')
        z += 1
    print('*'*x)
print(task14_18(3))