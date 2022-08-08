pcost=eval(input("Enter the product cost:"))
q=int(input("Enter the Quantity :"))
cardname=input("Enter the  card :")
billamount=pcost*q
print("total bill amount is:",billamount)
if billamount>=5000 or cardname=='citybank' :
    pamnt=billamount*20/100
    ramnt=billamount-pamnt
    print("Total amount you have to pay:",ramnt)
else:
    qamnt=billamount*5/100
    namnt=billamount-qamnt
    print("pay amount is:", namnt)
print("\t visit again thank you")
