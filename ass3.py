#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q:1 Program make a simple calculator
# This function adds two numbers 
def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user 
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")


# In[14]:


#Question: 02
n = [1, 2, 3, 4,'str',5,'ab',6]
for num in n:
    if type(num) == int:
        print("It is numeric Value")
    else:
        print("It is a string")


# In[ ]:


#Question: 035
list = []
num = int(input("How many number"))
for n in range(num):
    number = int(input("Enter number"))
    list.append(number)
    print("list =", list)
    print("lenght of the list =",len(list))


# In[ ]:




