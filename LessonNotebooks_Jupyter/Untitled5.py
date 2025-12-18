#!/usr/bin/env python
# coding: utf-8

# In[11]:


import time


print("Please do not lie on the following queries.")
time.sleep(1)
age = str(input("Input your age: "))
time.sleep(1)
has_license = input("Do you have a driver's license?: ")
print("Loading...")
time.sleep(2)
if age >= "18" and (has_license == "yes" or "Yes" or "y" or "Y" or "YES"):
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")


# In[16]:


import time
import sys

color = input("Enter signal color: ")

if color == "red" or "RED" or "Red" or "r":
    print("Stop!")
    time.sleep(1)
    print("Ready your engines...")
    time.sleep(1)
    print("Get ready...")
    time.sleep(1)
    print("Go!")
    sys.exit(/
elif color == "yellow" or "YELLOW" or "Yellow" or "y":
    print("Get ready...")
    time.sleep(1)
    print("Go!")
elif color == "green" or "GREEN" or "Green" or "g":
    print("What are you doing? Go!")
    sys.exit(0)
else:
    print("Invalid color.")
    sys.exit(0)


# In[18]:


age = int(input("Enter your age: "))

if age < 13:
    print("Child Ticket - $5")
elif age < 60:
    print("Adult Ticket - $10")
else:
    print("Senior Ticket - $6")


# In[21]:


units = int(input("Enter electicity units used: "))

if units >= 100:
    bill = units * 5
elif units >= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print(f"Your bill is {bill} Riyals.")


# In[ ]:




