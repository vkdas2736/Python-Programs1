class student:
    cid=11214
    nwdays=160
    def __init__(self,name):
        self.name = name
        print("inside init")
    def stduent_marks(self,maths, phy, che):
        self.math = maths
        self.phy = phy
        self.chemistry = che
    def average(self):
        print("name of the student",self.name)
        print("average marks ", (self.math+self.phy+self.chemistry)/3)
    def assign(self,sid,sname,npdays):
        self.npdays = npdays
        self.sid = sid
        pass
    def calattendance(self):
        self.ap=self.npdays/student.nwdays*100
        pass
    def display(self):
        print("college id is:",student.cid)
        print("no of working days:",student.nwdays)
        print("student id is:",self.sid)
        print("student name is:",self.sname)
        print("no of present day:",self.npdays)
        print("student sttendance percentage is:",self.ap)
s1 = student("vamsi")
s1.stduent_marks(80,70,90)
s1.average()
s2 = student("anil")
s2.cid =1415
print(s2.name,s2.cid)
print(s1.name,s1.cid)
# s1.assign(1001,'vamsi',154)
# s1.calattendance()
# s1.display()
