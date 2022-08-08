Accno=11221
amount=5000
def withdraw():
    global amount
    print("Account number is:",Accno)
    balEnq()
    print("Your Amount is:",amount)
    wAmnt=int(input("Enter the amount to withdraw:"))
    print("withdraw amount is:",wAmnt)
    amount=amount-wAmnt
    balEnq()
    print("Your Amount is:",amount) 
def deposit():
    global amount
    print("Account number is:",Accno)
    balEnq()
    print("Your Amount is:",amount)
    dAmnt=int(input("Enter the Deposit Amount is:"))
    print("Deposit amount is:",dAmnt)
    amount=amount+dAmnt
    balEnq()
    print("Your Amount is:",amount)
def balEnq():
    print("your balance is:",amount)
withdraw()
deposit()
