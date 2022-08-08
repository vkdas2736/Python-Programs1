print("\t welcome to MAA HOTEL")
print("1.Idly")
print("2.Puri")
print("3.Dosa")
print("4.Vada")
ch=int(input("Enter the choice :"))
if ch>=1 and ch<=4:
    if ch==1:
        Cost = 40
        print("Cost of Plate Idly is : ", Cost)
        pass
    elif ch==2:
        Cost = 50
        print("Cost of single puri is :", Cost)
        pass
    elif ch==3:
        dosa=input("Enter the Type of Dosa:")
        if dosa=="masala dosa":
            Cost=80
            print("Cost of masala dosa is :",Cost)
            pass
        elif dosa=="normal dosa":
             Cost=60
             print("Cost of normal dosa is :",Cost)
             pass
        else:
            Cost=75
            print("Cost of onion dosa is :",Cost)
    elif ch==4:
        Cost = 80
        print("Plate Vada C(ost is :", Cost)
        pass
    q = int(input("Enter the Quantity:"))
    billAmnt = q * Cost
    print("Your Bill Amount is  :", billAmnt)
    print("Thank You!....")
    if (billAmnt>=300):
        pay=billAmnt*10/100
        bilAmnt=billAmnt-pay
        print("you have to pay amount is :",bilAmnt)
        print("\t Thank YOu !...")
else:

    print("Sorry! Your Item is Not Available!!!")
    print("\t Thank you !........")



