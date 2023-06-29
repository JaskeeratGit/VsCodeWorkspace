import numpy as np
import random as r


"""

f = w1x1 + w2x2+ w3x3 + b
l1 = [[x1(footage), x2(age), x3(#rooms), price]]
w = [w1, w2, w3] 
x = [x1, x2, x3]

"""

"""
def cost(w,b,l):
    cost1 = 0
    for i in range(0,len(l)):
        cost1 = cost1 + ((w*l[i][0]+b-l[i][1])**2)/(2*len(l))
    return cost1
"""
def derivates(w,b,l):
    wrt_w = 0
    wrt_b = 0
    for i in range(0,len(l)):
        wrt_b = wrt_b + (w*l[i][0]+b-l[i][1])/len(l)
        wrt_w = wrt_w + (w*l[i][0]+b-l[i][1])*l[i][0]/len(l)
    return wrt_w, wrt_b


def main(w,b,l_rate):
    list1 = []
    #b_test = r.randint(1,10)
    b_test = r.randint(1,10)
    print("w_test = 3, b_test = ",b_test)
    for j in range(0,10):
        x = (r.randint(0,10)*r.randint(1,10))
        u = 3*x + b_test
        list1.append([x,u])
        
    tempb = tempw = 999
    y=0
    while abs(w-tempw)>0.000001 or abs(b-tempb)>0.000001:   #Implementing gradient descent
        y = y + 1
        tempw = w
        tempb = b
        w = w - l_rate*derivates(w,b,list1)[0]
        b = b - l_rate*derivates(tempw,b,list1)[1]
    #print(list1)
    #print(w,b)
    
    while True:
        inp = eval(input("Please enter the footage of the house: "))
        f = w*inp + b
        print("The predicted price of the house is: ",f)


main(100,100,0.001)
