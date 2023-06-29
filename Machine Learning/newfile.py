l1 = [[1002,68],[1500,95],[1403,87],[1450,85],[1312,80],[4032,300],[1241,74],[1623,97],[1186,72],[1234,81],[1089,69],[1200,74],[1800,101],[2000,110],[1700,95]]



def cost(w, b, list1):  #find the value of sq error cost function
    errorSq=0
    for i in range(0,len(list1)):
        errorSq = errorSq+((w*list1[i][0]+b-list1[i][1])**2)/(2*len(list1))
    return errorSq

def costDerivative(w, b, list1):  #find the derivatives
    wrt_w = 0
    wrt_b = 0
    for i in range(0,len(list1)):
        wrt_w = wrt_w + ((w * list1[i][0] + b - list1[i][1]) * list1[i][0])/len(list1)
        wrt_b = wrt_b+ (w * list1[i][0] + b - list1[i][1])/(len(list1))
    return wrt_w, wrt_b


def minCost(w, b, list1, l_rate = 0.00000009, threshold = 0.00001): #minimize the cost function by varying parameters using the gradient descent method, cannot take w and b as between 10.01 and 9.99, if alpha taken as 5 --> diverges
    x=0
    temp_b = temp_w = 2
    temp_cost = cost(temp_w, temp_b, list1)
    while abs(temp_b-b) >= threshold or abs(temp_w-w) >= threshold :
        temp_w = w
        temp_b = b
        derivatives = costDerivative(temp_w, temp_b, list1)
        w = w - l_rate * derivatives[0]
        b = b - l_rate * derivatives[1]
        print(derivatives)
        print(w,temp_w,b,temp_b)
        #print(cost(w, b, list1))
        x=x+1
        print(x)
    return w,b

minCost(1,1,l1) 



