import numpy as np
import math
def sigmoid(z):
    if type(z) == int or type(z) == float:
        g = 1/(1+math.exp(-z))
    else:
        g = []
        for i in range(0,len(z)):
            g.append(1/(1+math.e**(-z[i])))
    return g
print(sigmoid(np.array([[[1,2,1,1],[1,2,3,4]]])))


import wget

img_url = "https://cdn.britannica.com/41/123141-050-E6229449/Air-New-Zealand-Boeing-747-400.jpg"
image = wget.download(img_url)
print(image)




