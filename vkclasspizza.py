class pizza():
    pizzacost=int(input("Enter the pizza cost:"))
    def order_details(self,name,discount,q):
        self.name=name
        self.discount=discount
        self.q=q
        pass
    def caltotalamount(self):
        self.billamnt=pizza.pizzacost*self.discount/100
        self.r=pizza.pizzacost-self.billamnt
        self.totalamount=self.r*self.q
        pass
    def display(self):
        print("enter the pizza cost is:",pizza.pizzacost)
        print("Enter the Customer name:",self.name)
        print("enter the discount percentage :",self.discount)
        print("Enter the quantity : ",self.q)
        print("total amount of the pizzas:",self.totalamount)
        pass
p1=pizza()
print("\t Sankarmatam customer order details::::")
p1.order_details('vamsi',10,5)
p1.caltotalamount()
p1.display()