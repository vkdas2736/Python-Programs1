pizzaCost=eval(input("Enter the Pizza Cost:"))
d=10
billAmnt=pizzaCost*d/100
r=pizzaCost-billAmnt
q=int(input("Enter the quantity:"))
totalAmnt=q*r
print("enter the discount Amount:",d)
print("enter the bill amount:",r)
print("total amount:",totalAmnt)
