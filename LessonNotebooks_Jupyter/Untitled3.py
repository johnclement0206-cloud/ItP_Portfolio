#!/usr/bin/env python
# coding: utf-8

# In[5]:


temperature = 31
if temperature >= 30:
    print("Hot Day")
else:
    print("Cold Day")


# In[8]:


a = 10; b = 20; c = a + 10
print(a == b)
print(a < b)
print(a != b)


# In[12]:


x = 4; y = 5
print(x > 5 and y < 10)
print(x < 5 or y < 10)
print(not(x == 10))


# In[14]:


score = 85
if score >= 80 and score <= 100:
    print("Excellent.")


# In[8]:


import random
import string

username = "admin"
password = "1234"
userName = "John"
age = "19"

userInput = input("Enter username: ")
passInput = input("Enter password: ")

random_code = random.randint(1000, 9999)

if userInput == username and passInput == password:
    nameInput = input("Enter your name: ")
    if nameInput == userName:
        ageInput = input("Enter your age: ")
        if ageInput == age:
            print("Please confirm you are not a robot. Enter the following code.")
            print(f"Your verification code is: {random_code}")
            codeInput = int(input("Enter the verification code: "))
            if codeInput == random_code:
                print("Access granted.")
            else:
                print("Get out of my swamp!")
        else:
            print("Faker.")
    else:
        print("Who are you?")
        
else:
    print("Access denied.")


# In[15]:


import random
import string

username = "admin"
password = "1234"
userName = "John"
age = "19"

userInput = input("Enter username: ")
passInput = input("Enter password: ")

CHARPOOL = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

random_code = ''.join(random.choices(CHARPOOL, k=5))

if userInput == username and passInput == password:
    print(f"Your verification code is: {random_code}")
    nameInput = input("Enter your name: ")
    if nameInput == userName:
        ageInput = input("Enter your age: ")
        if ageInput == age:
            print("Please confirm you are not a robot. Enter the verification code.")
            codeInput = input("Enter the verification code: ")
            if codeInput == random_code:
                print("Access granted.")
            else:
                print("Get out of my swamp!")
        else:
            print("Faker.")
    else:
        print("Who are you?")
else:
    print("Access denied.")


# In[ ]:




