class Test:
    def show(self):
        self.a=50
        self.b=100
        pass
class Demo(Test):
    def CalTotal(self):
        self.c=self.a+self.b
        pass
    def display(self):
        print("Calculation of total is ,",self.c)
d1=Demo()
d1.show()
d1.CalTotal()
d1.display()