def add(a,b):
    return a+b

def rev(a):
    c=0
    while(a>0):
        r=a%10
        c=(c*10)+r
        a//=10
    return(c)