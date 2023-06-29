l1 = [9,8,7,6,5,4]
[8,9,7,6,5,4]
[8,7,9,6,5,4]
[8,7,6,9,5,4]
#.....

#look at each element from the left and keep swapping until no other is less than it
for i in range(1,len(l1)):
    for j in  range(i-1,-1,-1):
        #print(j)
        if l1[j]>l1[j+1]:
            temp = l1[j] 
            l1[j] = l1[j+1]
            l1[j+1] = temp
            print(l1)
        else:
            break
            
        

