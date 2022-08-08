print("\tWelcome to NAA BANK")
print("1.Education")
print("2.Home")
print("3.Gold")
print("4.personal")
ch=int(input("Enter your choice :"))
if ch==1:
    r=6.8
    print("Rate of Interest for Education Loan is: ",r,"%")
    pass
elif ch==2:
    r=9.4
    print("Rate of Interest for Home Loan is: ", r, "%")
    pass
elif ch==3:
    r=12.6
    print("Rate of Interest for Gold Loan is: ", r, "%")
    pass
else:
    r=14.2
    print("Rate of Interest for Personal Loan is: ", r, "%")
amt=eval(input("Enter Loan amount:"))
t=int(input("Enter Time Period :"))
iAmnt=amt*t*r/100
finalAmt=amt+iAmnt
print("Interest Amount is :",iAmnt)
print("Final Amount is:",finalAmt)
