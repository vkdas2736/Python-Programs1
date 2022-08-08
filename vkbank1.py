class BankAlert:
    branchid=1254214
    def assign(self,cid,amount,wamnt,damnt):
        self.cid=cid
        self.amount=amount
        self.wamnt=wamnt
        self.damnt=damnt
        pass
    def withdraw(self):
        print("enter the withdraw amount:",self.wamnt)
        pass
    def damount(self):
        print("enter the deposit amount:",self.damnt)
        pass
    def caltamount(self):
        self.p=self.amount-self.wamnt
        self.q=self.p+self.damnt
        pass
    def display(self):
        print("after calculation withdraw amount  is:",self.p)
        print("calculation of toal amount is:",self.q)
        pass
b1=BankAlert()
b1.assign(112485,50000,5400,7000)
b1.damount()
b1.caltamount()
b1.display()