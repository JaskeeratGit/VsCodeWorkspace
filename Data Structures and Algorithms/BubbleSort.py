l1 = [3,2,4,1]
#first 2, then next 2, then next 2, then again and again until done after each loop last element will be sorted in the list

for i in range(0,len(l1)-1):
    for j in range(0,len(l1)-i-1):
        if l1[j]>l1[j+1]:
            temp = l1[j]
            l1[j] = l1[j+1]
            l1[j+1] = temp
            print(l1)



