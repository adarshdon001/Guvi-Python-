#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1 . Python program to check whether the given number is even or not.

a=int(input("Enter any number:"))
if a%2==0:
    print("The Entered Number is Even")
else:
    print("The Entered Number is Odd")


# In[2]:


#Python program to convert the temperature in degree centigrade to Fahrenheit.
a=float(input())
f=(a*1.8)+32

print("Fahrenheit =",round(f,2))


# In[4]:


#Python program to find the product of a set of real numbers.
a=[1,2,3,4]
product=1
for i in a:
    #product=i*product
    product *= i

print("Product of Real numbers:",product)


# In[7]:


#Python program to find the factorial of a number using recursion.
def fact(n):
    if n==1 or n== 0:
        return 1
    else:
        return n*fact(n-1)

n=fact(7)
print ("Factorial of 7 is:",n)


# In[ ]:


#Python program to implement linear search.
a=[1,2,5,7,3,4,6,8,9,0]

find =int(input("Enter the number to find:"))

for i in a:
    if i == find:
        print(f"The index position of {find} is :",a.index(i))


# 

# In[ ]:


#Python program to implement binary search.

a= [0,2,4,5,7,9,11,20]

n=20
low=0
high=len(a)-1
mid=0

while low <= high:
    mid=(low + high)//2
    
    if a[mid] > n:
        high = mid-1
    
    elif a[mid] < n:
        low = mid+1
        
        
    elif a[mid] == n:
        print("N is present in ",mid,"th Index")
        break
else:
    print("Not in list")


# In[ ]:





# In[ ]:


#Python program to find the largest number in a list without using built-in functions

a=[1,2,7,15,10,6,12,21]
m=0
for i in a:
    if m >= i:
        continue
                
    else:
        m=i
        
print("Largest number in the list:",m)


# In[ ]:


#Python program to delete an element from a list by index\

list=[4,5,7,2,7,23]
print("Old list:",list)

del list[2]
print("New list after deleting 3rd position:",list)


# In[ ]:


#Python program to print all the items in a dictionary

dic={'a':1,'b':2,'c':3}
print("Items in the Dictionary are")
for i,j in dic.items():
    print(i,j)


# In[ ]:


#Python program to find the average of 10 numbers using while loop

number=[11,4,15,6,7,3,70,8,1,5]
count=0
add=0
for i in number:   
    while (count<10):
        count = count+ 1
        add=i+add
        break      

print("Everage of 10 numbers is :",add/len(number))  


# In[ ]:




