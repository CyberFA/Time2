class Time:
    def __init__(self, h , m , s):
        self.h = h 
        self.m = m 
        self.s = s

    def Hour(self):
        if self.h >=0 and self.h<24:
            self.h = self.h

        else:
            self.h = "{:02d}".format(0)
        return self.h
    def Min(self):
        if self.m >=0 and self.m <60:
            self.m = self.m
        else:
            self.m = "{:02d}".format(0)
        return self.m
    def Second(self):
        if self.s >=0 and self.s < 60:
            self.s = self.s
        else:
            self.s = "{:02d}".format(0)
        return self.s
    def ShowTime(self):
        return f"{'Hour':^10} | {'Min':^10}\n{'-'*25}\n{self.Hour():^10} | {self.Min():^10}"

class Time2(Time):
    def __init__(self,h,m,s):
        super().__init__(h,m,s)
    
    def Hour(self):
        if self.h>=0 and self.h<12:
            hour = str(self.h)
            hour = hour  + ' AM'
        elif self.h >=12 and self.h<24:
            hour = str(self.h) 
            hour = hour + ' PM'
        else:
            hour = "{:02d}".format(0)
        return hour
#t = Time(24,40,58)
#print(t.ShowTime())            
t = Time2(28,55,30)
#print(t.ShowTime())
print(t.ShowTime())

#
