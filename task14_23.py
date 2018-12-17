def task14_23(x):
    while True:
        if x % 2 == 0 or x % 3 == 0:
            return False
        else:
            return True
print(task14_23(11))