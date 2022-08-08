EmpAnnualsalary=eval(input("Enter the Annual Salary:"))
EmppermonthSalary=EmpAnnualsalary/30
print("Employee per month salary is :",EmppermonthSalary)
if EmpAnnualsalary>=21000:
    Experience=eval(input("Employees Experience:"))
    LoanAmnt=int(input("Enter the Loan amount :"))
    TimePeriod=int(input("Enter the time period :"))
    if Experience>2:
        print("You are Eligible for Loan!")
        print("\t1.Home Loan")
        print("\t2.Education Loan")
        print("\t3.Personal Loan")
        print("\t4.Other Loan")
        ch=int(input("Enter Your choice:"))
        if ch==1:
            r=11.6
            print("Rate of Interest for Home loan is :",r)
            pass
        elif ch==2:
            r=6.8
            print("Rate of Interest for the Education Loan is :",r)
            pass
        elif ch==3:
            r=12.4
            print("Rate of Interest for Personal Loan is :",r)
            pass
        elif ch==4:
            r=13.6
            print("Rate of Interest for Other Loans is :",r)
            pass
        Amount=LoanAmnt*TimePeriod*r/100
        print("Simple Interest Amount is :",Amount)
        FinalAmount=LoanAmnt+Amount
        print("Final AMount is :",FinalAmount)
        emi=int(input("NO of months taken for Emi :"))
        CalEmi=FinalAmount/emi
        print("CAlcualtion of Emi Amount:",CalEmi)

        pass
    else:
        print("Request is rejected Due to less Experience")
    pass
else:
    print("Loan Requested rejected due to Less Salary.")
    print("To get Loan Minimum Annual Salary should be More than 250000.")
