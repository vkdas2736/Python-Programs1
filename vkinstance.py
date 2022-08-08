class Test():
    def calTotal(self,a,b):
        self.c=a+b
        print("Sum is :",self.c)
    def calAvg(self):
        calAvg=self.c/2
        print("average is:",calAvg)
t1=Test()
t1.calTotal(8,9)
t1.calAvg()

