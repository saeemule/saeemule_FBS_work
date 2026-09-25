class Time:
    def __init__(self, hr, min, sec):
        self.setHr(hr)
        self.setMin(min)
        self.setSec(sec)

    def setHr(self, hr):
        self.hr = hr

    def setMin(self, min):
        self.min = min

    def setSec(self, sec):
        self.sec = sec

    def getHr(self):
        return self.hr

    def getMin(self):
        return self.min

    def getSec(self):
        return self.sec

    def __add__(self, other):
        totalsec = self.sec + other.sec
        totalmin = self.min + other.min
        totalhr = self.hr + other.hr
        return Time(totalhr, totalmin, totalsec)

    def __str__(self):
        return f"{self.hr} : {self.min} : {self.sec}"

t1 = Time(2, 45, 50)
t2 = Time(3, 20, 30)
print(t1+t2)