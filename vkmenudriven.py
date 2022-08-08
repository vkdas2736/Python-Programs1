print("\twelcome to the MY HOTEL ")
print("1.enter the idly")
print("2.enter the puri")
print("3.enter dosa")
print("4.enter vada")
print("5.enter your choice")
ch=int(input("enter your choice:"))
q=int(input("Enter the Quantity:"))
if ch==1:
    amnt=40
    pass
elif ch==2:
    amnt=50
    pass
elif ch==3:
    amnt=60
    pass
elif ch==4:
    amnt=80
    pass
else:
    print("sorry! your item is not available ....")

bill=q*amnt
print("your bill amount is:",bill)
