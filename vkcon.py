class Employee:
    def __init__(self,eid,name,salary,oc='FRESHER'):
        self.eid=eid
        self.name=name
        self.salary=salary
        self.oc=oc

    def display(self):#"by using default and parametarized constructrors usage
        # constructor is a special type of method which is used to initilize instance variables at the
      #0  at the time object creaTION
        print("Employee id is :",self.eid)
        print("Employee name is:",self.name)
        print("Employee salary is:",self.salary)
        print("Employee wheather experienced or Fresher :",self.oc)
        pass
print("\t Employeee-1 Information is ")
e1=Employee(13265,"vamsi",50000)
e1.display()
e2=Employee(11214,"Krishna",50000)
e2.display()
