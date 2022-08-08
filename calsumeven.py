num=int(input("Enter the num Value :"))
sum=0
for x in range(num+1):
    print(x,end="\t")
    if (x%2==0):
        sum=sum+x
print("\nSum of All Numbers:",sum)
print("\n Thank you")
