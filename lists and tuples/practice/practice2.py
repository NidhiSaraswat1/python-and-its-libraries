a =[1,23,4,43,234,5,6554,2345]
def checkEven(a):
    x =[]
    for i in range(len(a)):
        b = a[i]
        if(b%2==0):
            x.append(b)
    return x         
print(checkEven(a))