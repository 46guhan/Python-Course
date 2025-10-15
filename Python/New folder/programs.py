##basic programs

#factorial of a num
'''
a=int(input("enter the number:"))
i=a
b=a-1
while(b>0):
    c=a*b
    a=c
    b-=1
print("the fibonecci of ",int(i),"=",c)
'''

#find simple intrest
'''
p=int(input("principal="))
t=int(input("time="))
r=int(input("intrest rate="))

si=(p*t*r)/100
print("simple interst=",si)

#find compound interest

amount=p*(1+(r/100))**t
ci=amount-p
print("compound interst=",ci)
'''

#check amstrong number
'''
a=int(input("enter the num:"))
b=0
while(a>0):
    c=a%10
    b=(c**3)+b
    a//=10
print(b)
'''
#find area of circle
'''
import math
r=int(input("radious="))
pi=math.pi

a=pi*(pow(r,2))
b=pi*(r**2)
print("area of circle=",a,b)
'''
#print prime num in range
""" 
x=[]
for i in range(2):
    x.append(int(input('enter the numbers:')))
    m=max(x)
    for a in x:
        while(a<m):
            a+=1
            print(a)
 """  

# fibonanacy
""" 
n=10
a = 0
b = 1      
for i in range(2,n):
    c=a+b
    a=b
    b=c
print(c)
 """

# square sum
""" 
n = 5
res = n * (n + 1) * (2 * n + 1) // 6
print(res)

n = 5
total = 0

for i in range(1, n + 1):
    total += i * i
print(total)

n = 5
total = 0

for i in range(1, n + 1):
    total += i ** 3
print(total)
 """

# Largest Element in an Array
""" 
a = [23,41,5,234,75,6,0,756]
a.sort()
print(a[-1])
print(max(a))
 """

# Interchange first and last elements

""" 
my_list = [1, 2, 3, 4, 5]
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)

a = [10, 20, 30, 40, 50]
a[0], a[4] = a[4], a[0]
print(a)
 """

# Length of a List in Python
""" 
a=[10, 20, 30, 40, 50]
count=0
for i in a:
    count+=1
print(count)
 """

# sum of elements in List
""" 
a = [10, 20, 30, 40, 50]
res = 0 

for i in a:
    res += i 
print(res)
 """

# multipication of elements in List
""" 
a = [2, 4, 8, 3]
res = 1

for val in a:
	res = res * val
print(res)
 """

# Remove Multiple Elements from List
""" 
a= [10, 20, 30, 40, 50, 60, 70, 80, 90]
b= [20, 40, 60]
for i in b:
    if i in a:
        a.remove(i)
print(a)
 """

# Remove empty Lists from List
""" 
a=[5, 6, [], 3, [], [], 9]
res = []
for i in a:
    if i != []:
        res.append(i)
print(res)
 """

# Count occurrences of an element in a list
""" 
a= [10, 20, 30, 20, 40, 50, 20]
count=0
for i in a:
    if i==20:
        count+=1
print(count)
 """

# print duplicates from a list of integers
""" 
a= [1, 2, 3, 4, 3, 2, 5, 6, 7, 8, 7]
res = []
for i in a:
    if a.count(i) > 1:
        if i not in res:
            res.append(i)
print(res)
 """

# Sum of number digits in List
""" 
a= [12, 67, 98, 34]
res = []
for i in a:
    sum = 0
    while i > 0:
        digit = i % 10
        sum += digit
        i //= 10
    res.append(sum)
print(res)
 """

# Sort the values of first list using second list
""" 
a= [10, 11, 12, 13, 56]
b= [4, 3, 1, 0, 2]
res = [0] * len(a)
for i in range(len(b)):
    res[b[i]] = a[i]
print(res)
 """

# Bubble Sort
""" 
a = [23,41,5,234,75,6,0,756]
n = len(a)
for i in range(n):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
 """
# Array Rotation
""" 
n=2
a = [1,2,3,4,5]
for i in range(n):
    first = a[0]
    for j in range(len(a)-1):
        a[j] = a[j+1]
    a[-1] = first
    print(a)

n=3
a = [1,2,3,4,5]
for i in range(n):
    a.append(a.pop(0))
print(a)

n=2
a=[1,2,3,4,5]
c=a[n:]+a[:n]
print(c)
 """

