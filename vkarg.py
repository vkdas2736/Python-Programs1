def search(itemname):
    pcost=int(input("enter the product cost:"))
    q=int(input("enter the no of quantites:"))
    return pcost,q
def payAmount(billAmnt,phnno):
    print("verify phono")
    print("pay bill")
    status=True
    return status
def placeOrder():
    print("Select  your product and quantity")
    pcost=int(input("enter the product cost:"))
    q=int(input("enter the no of quantites:"))
    pcost,q=search("enter the item name:")
    billAmnt=pcost*q
    print("bill amount is:",billAmnt)
    print("Pay Bill amount is :")
s=payAmount(billAmnt,80765)
print("your payment is sucess")
print("your order is ready")

