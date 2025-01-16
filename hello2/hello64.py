tup = (1,4,6,8,34,762,65,84,67)

find = int(input("Enter num you wan to find: "))
i=0
while i<len(tup) :
    if(tup[i] == find) :
        print("found at idx ",i)
        break
    else :
        print("finding")
    i+=1