s1=int(input("Enter the subject s1 Marks:"))
s2=int(input("Enter the Subject s2 Marks:"))
s3=int(input("Enter the Subject s3 Marks:"))
if (s1>=35 and s2>=35 and s3>=35):
    print("\t the student passed in all subjects")
    total=s1+s2+s3
    print("Total Marks are:",total)
    avg=total/3
    print("Average Marks are:",avg)
else:
    print("Student failed in the exam")
print("\t Thank you")
