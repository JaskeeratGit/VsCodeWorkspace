"""
split list into half
divide and conquer
large datasets

"""


def function(list):
    mergesort(list, 0, len(list)-1)

def mergesort(list, firsti, lasti):
    if firsti<lasti:
        midi = (firsti + lasti) //2
        mergesort(list, firsti, midi)
        mergesort(list, midi+1, lasti)
        mergefunc(list, firsti, midi, lasti)

def mergefunc(list, firsti,midi,lasti):
    Left=list[firsti:midi+1]
    Right=list[midi+1:lasti+1]
    Left.append(999999)
    Right.append(999999)

    i = j =0
    for k in range(firsti, lasti+1):
        if Left[i]<=Right[j]:
            list[k] = Left[i]
            i=i+1
        else:
            list[k]=Right[j]
            j=j+1

function([1,3,5,6,2,34,132])