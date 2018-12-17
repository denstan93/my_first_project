class time:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def time1(self, time1):
        time1 = int(input('Введите кол-во дней: '))
        c = time1 + self.day
        month30 = [4, 6, 9, 11]
        month31 = [1, 3, 5, 7, 8, 10, 12]
        month28 = [2]
        while True:
            if self.year % 4 == 0:
                    if self.month > 12:
                        self.year += 1
                        self.month = 1
                    if self.month in month30:
                        if c > 30:
                            c = c - 30
                            self.month += 1
                        else:
                            self.day = c
                            break
                    elif self.month in month31:
                        if c > 31:
                            c = c - 31
                            self.month += 1
                        else:
                            self.day = c
                            break
                    elif self.month in month28:
                        if c > 29:
                            c = c - 29
                            self.month += 1
                        else:
                            self.day = c
                            break
            else:
                if self.month > 12:
                    self.year += 1
                    self.month = 1
                if self.month in month30:
                    if c > 30:
                        c = c - 30
                        self.month += 1
                    else:
                        self.day = c
                        break
                elif self.month in month31:
                    if c > 31:
                        c = c - 31
                        self.month += 1
                    else:
                        self.day = c
                        break
                elif self.month in month28:
                    if c > 28:
                        c = c - 28
                        self.month += 1
                    else:
                        self.day = c
                        break
data = time(12,17,1995)
print(data.month,data.day,data.year)
data.time1(1)
print(data.month,data.day,data.year)