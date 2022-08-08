biryani=int(input("enteer the biryani price:"))
manchuriya=int(input("enter the manchuriya cost:"))
frnds=int(input("no of frnds were went to kfc:"))
q=int(input("no of biryanies are ordered:"))
p=int(input("no of manchurias are ordered:"))
totalAmount=biryani*q+manchuriya*p
share=totalAmount/frnds
print("total amount at KFC:",totalAmount)
print("sharing amount by each frnd:",share)