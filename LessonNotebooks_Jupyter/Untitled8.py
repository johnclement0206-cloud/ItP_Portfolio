#!/usr/bin/env python
# coding: utf-8

# In[3]:


pin = ''

while pin != "1234":
    pin = input("Enter your Pin: ")
print("Access Granted.")


# In[5]:


attempts = 0
MAX_ATTEMPTS = 3

while attempts < MAX_ATTEMPTS:
    login = input("Enter login: ")
    password = input("Enter password: ")
    if login == "admin" and password == "12345":
        print("Access granted.")
        break
    attempts += 1
    remaining = MAX_ATTEMPTS - attempts
    if remaining > 0:
        print(f"Incorrect credentials. {remaining} attempt(s) remaining.")
else:
    print("Access denied.")


# In[6]:


cups = 3
while cups > 0:
    print("Serving coffee...")
    cups -= 1
print("No more coffee left!")


# In[8]:


while True:
    name = input("Enter name (type stop to exit): ")
    if name == "stop":
        break
    print("Hello", name)


# In[21]:


num = 0

while num <= 10:
    num = int(input("Enter a number that is greater than 10: "))
    if num > 10:
        print("This number is greater than 10!")
        break
    print("This number is not greater than 10.")


# In[ ]:




