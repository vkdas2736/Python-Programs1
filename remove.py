a=[10,20,30,30,40,40,50]
def remove_duplicate(duplist):
    noduplist=[]
    for element in duplist:
        if element not  in noduplist:
            noduplist.append(element)
            return noduplist
print(remove_duplicate(a))
