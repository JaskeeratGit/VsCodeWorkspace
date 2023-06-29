#find smallest item first then put it into the left most position

l1 = [7,8,5,4,9,2]
for j in range(0,len(l1)-1):
    min1 = j
    for i in range(j+1,len(l1)):
        if l1[i]<l1[min1]:
            min1 = i
    if min1!=j:
        temp = l1[j]
        l1[j]=l1[min1]
        l1[min1]=temp
print(l1)

            
            

        
    


        